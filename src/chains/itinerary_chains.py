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
itnineary_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a helpful travel assistant. Create a day trip itinerary for {city} "
        "based on user's interests: {interests}. Provide a brief, bulleted itinerary."
    ),
    (
        "human",
        "Create an itinerary for my day trip."
    )
])


def generate_itineary(city: str, interests: list[str]) -> str:
    """
    Generate a day trip itinerary for a given city based on user interests.

    Args:
        city (str): The name of the city to generate the itinerary for.
        interests (list[str]): A list of user interests (e.g., food, history, adventure).

    Returns:
        str: The generated itinerary as a string.
    """
    # Format prompt with user inputs
    messages = itnineary_prompt.format_messages(
        city=city,
        interests=', '.join(interests)
    )

    # Get LLM response
    response = llm.invoke(messages)

    return response.content.strip()
