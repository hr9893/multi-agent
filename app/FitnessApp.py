import streamlit as st
from app.GroqService import GroqService
from app.WorkoutHistoryService import WorkoutHistoryService


class FitnessApp:

    def __init__(self):
        self.groq_service = GroqService()
        self.workout_history_service = WorkoutHistoryService()

    def run(self):

        st.title("🏋️ Fitness Plan Generator")

        fitness_goal = st.selectbox(
            "Fitness Goal:",
            [
                "Build muscle",
                "Lose fat",
                "General fitness",
                "Improve endurance"
            ]
        )

        experience_level = st.selectbox(
            "Experience Level:",
            [
                "Beginner",
                "Intermediate",
                "Advanced"
            ]
        )

        available_days = st.slider(
            "Choose days:",
            min_value=1,
            max_value=7
        )

        available_equipment = st.selectbox(
            "Select Available Equipment:",
            [
                "No equipment",
                "Home dumbbells",
                "Full gym"
            ]
        )

        injuries = st.text_input(
            "Enter if any injuries:"
        )
        if st.button("Generate Plan", type="primary"):

            fitness_data = {
                "fitness_goal": fitness_goal,
                "experience_level": experience_level,
                "available_days": available_days,
                "available_equipment": available_equipment,
                "injuries": injuries
            }

            try:

                with st.spinner("Generating Fitness Plan..."):

                    response = self.groq_service.generate_response(
                        fitness_data
                    )

                self.workout_history_service.save_plan(
                    fitness_data,
                    response
                )

                st.subheader("Generated Fitness Plan")

                st.write(response)

                st.download_button(
                    label="📥 Download Plan",
                    data=response,
                    file_name="fitness_plan.txt",
                    mime="text/plain"
                )

            except Exception as e:

                print(
                    f"Exception occurred while getting the response from LLM: {e}"
                )

        self._render_workout_history()

    def _render_workout_history(self):

        st.divider()

        st.header("📚 Workout History")

        history = self.workout_history_service.get_history()

        if not history:
            st.info("No saved workout plans yet.")
            return

        if st.button("🗑️ Clear History"):
            self.workout_history_service.clear_history()
            st.success("Workout history cleared.")
            st.rerun()

        options = [
            f"{index + 1}. {entry.get('timestamp', 'Unknown date')} - "
            f"{entry.get('fitness_goal', 'Unknown goal')}"
            for index, entry in enumerate(history)
        ]

        selected_option = st.selectbox(
            "Select a saved workout plan:",
            options
        )

        selected_index = options.index(selected_option)
        selected_entry = history[selected_index]

        st.subheader("Plan Details")

        st.write(f"**Fitness Goal:** {selected_entry.get('fitness_goal')}")
        st.write(f"**Experience Level:** {selected_entry.get('experience_level')}")
        st.write(f"**Available Days:** {selected_entry.get('available_days')}")
        st.write(f"**Available Equipment:** {selected_entry.get('available_equipment')}")
        st.write(f"**Injuries:** {selected_entry.get('injuries')}")
        st.write(f"**Generated At:** {selected_entry.get('timestamp')}")

        st.markdown("**Workout Plan:**")
        st.write(selected_entry.get("plan", ""))

        st.download_button(
            label="📥 Download Saved Plan",
            data=selected_entry.get("plan", ""),
            file_name="fitness_plan.txt",
            mime="text/plain"
        )
