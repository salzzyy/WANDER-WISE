from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from src.config.config import GROQ_API_KEY


# Initialize the LLM client
llm = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.3-70b-versatile",
    temperature=0.3,
)


# Define the itinerary prompt template
itinerary_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are an expert travel assistant who creates personalized, fun, and practical day trip itineraries. "
            "For the city {city}, design a day trip based on the user's interests: {interests}. "
            "Provide a detailed, chronologically organized itinerary, including morning, afternoon, and evening activities. "
            "Include approximate timings, recommended places, local food experiences, cultural or adventurous activities, and any fun tips or insights. "
            "Make it engaging, easy to follow, and tailored to the user's preferences.",
        ),
        ("human", "Please generate a complete and exciting day trip itinerary for me."),
    ]
)


def generate_itinerary(city: str, interests: list[str]) -> str:
    """
    Generate a day trip itinerary for a given city based on user interests.

    Args:
        city (str): The name of the city to generate the itinerary for.
        interests (list[str]): A list of user interests (e.g., food, history, adventure).

    Returns:
        str: The generated itinerary as a string.
    """
    # Format prompt with user inputs
    messages = itinerary_prompt.format_messages(
        city=city, interests=", ".join(interests)
    )

    # Get LLM response
    response = llm.invoke(messages)

    return response.content.strip()
