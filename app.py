from openai import OpenAI
import streamlit as st

def get_openai_response(prompt):
    client = OpenAI()
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": """You are a professional travel agent creating a personalized travel itinerary for a client."""},
                {
                    "role": "user",
                    "content": prompt
                }
            ],

        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {e}"

# Streamlit app
def main():
    st.title("Travel Itinerary Generator Chatbot")
    st.write("Welcome! I can help you plan a personalized travel itinerary based on your preferences.")

    # Sidebar for user inputs
    with st.sidebar:
        st.header("Your Travel Preferences")
        destination = st.text_input("Enter your travel destination")
        budget = st.selectbox("Select your budget", ["Low", "Moderate", "Luxury"])
        trip_duration = st.number_input("Enter the duration of your trip (in days)", min_value=1, step=1)
        purpose = st.text_input("Enter the purpose of your trip (e.g., leisure, adventure, business)")
        preferences = st.text_area("Enter any specific preferences (e.g., food, culture, nature)")

    if st.button("Generate Itinerary"):
        if not destination or not purpose:
            st.error("Please fill in all required fields.")
        else:
            with st.spinner("Generating your travel itinerary..."):
                # Initial prompt
                prompt = (
                    f"The user provided the following details: \n"
                    f"Destination: {destination}\n"
                    f"Budget: {budget}\n"
                    f"Trip Duration: {trip_duration} days\n"
                    f"Purpose: {purpose}\n"
                    f"Preferences: {preferences}\n"
                    f"Generate a detailed day-by-day travel itinerary based on these inputs."
                )

                # Fetch response from OpenAI
                itinerary = get_openai_response(prompt)

                # Display the response
                if "Error" in itinerary:
                    st.error(itinerary)
                else:
                    st.success("Here is your personalized travel itinerary:")
                    st.text(itinerary)

if __name__ == "__main__":
    main()
