import os

from strands import Agent, tool
from strands.models import BedrockModel
from httpx import AsyncClient

from dotenv import load_dotenv

from src.models import WeatherApiOutput, WeatherOutput, WeatherToolOutput

load_dotenv()


BEDROCK_MODEL = BedrockModel(
    model_id=os.environ.get("BEDROCK_MODEL_ARN", ""),
    region_name="us-east-1",
    max_tokens=4000,
)

@tool
async def get_weather(city: str) -> WeatherToolOutput:
    """
    Fetches the current weather information for a given city.
    """

    async with AsyncClient() as client:
        response = await client.get(f"https://wttr.in/{city}?format=j2")
        data = response.json()
        
        parsed_data = WeatherApiOutput.model_validate(data)
        return WeatherToolOutput(
            temperature=parsed_data.current_condition[0].temp_C if parsed_data.current_condition else 0.0,
            humidity=parsed_data.current_condition[0].humidity if parsed_data.current_condition else 0,
            condition=parsed_data.current_condition[0].weatherDesc[0].value if parsed_data.current_condition and parsed_data.current_condition[0].weatherDesc else ""
        )

def main():
    agent = Agent(
        model=BEDROCK_MODEL,
        tools=[get_weather]
    )

    prompt = """
    You are a weather agent. Pick a city of your choice
    and provide the weather information for that city.
    """
    response = agent(
        prompt=prompt,
        structured_output_model=WeatherOutput
    )

    weather_output = response.structured_output
    if weather_output is None:
        print("No structured output received.")
        return
    print(weather_output.model_dump_json(indent=4))


if __name__ == "__main__":
    main()
