import streamlit as st
from src.core.planner import TravelPlanner
from dotenv import load_dotenv

# Configure Streamlit page
st.set_page_config(page_title="AI Travel Planner", page_icon="🌍", layout="centered")

# App title and description
st.title("🗺️ AI Travel Itinerary Planner")
st.write(
    "Plan your perfect **day trip itinerary** in seconds! 🌟\n\n"
    "Just enter a **city** and your **interests** (e.g., food, history, adventure) "
    "and let AI create a personalized travel plan for you."
)

# Load environment variables
load_dotenv()

# User input form
with st.form("planner_form"):
    city = st.text_input("🏙️ Enter the city name for your trip:")
    interests = st.text_input("🎯 Enter your interests (comma-separated):", placeholder="e.g., food, history, art, adventure")
    submitted = st.form_submit_button("✨ Generate Itinerary")

    if submitted:
        if city and interests:
            try:
                planner = TravelPlanner()
                planner.set_city(city)
                planner.set_interests(interests)
                itineary = planner.create_itineary()

                st.subheader("📄 Your AI-Generated Itinerary")
                st.markdown(itineary)
            except Exception as e:
                st.error(f"⚠️ Something went wrong: {e}")
        else:
            st.warning("⚠️ Please fill in both **City** and **Interests** to continue.")
