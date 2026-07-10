import os

from strands import Agent
from strands.models import BedrockModel

from dotenv import load_dotenv

from src.models import Itinerary

load_dotenv()


BEDROCK_MODEL = BedrockModel(
    model_id=os.environ.get("BEDROCK_MODEL_ARN", ""),
    region_name="us-east-1",
    max_tokens=4000,
)

def main(source_city: str, destination_city: str):
    agent = Agent(model=BEDROCK_MODEL)

    prompt = f"""
    You are a travel agent. Use your own knowledge to
    generate a travel itinerary from {source_city} to {destination_city}.
    """
    response = agent(
        prompt=prompt,
        structured_output_model=Itinerary
    )

    travel_itinerary = response.structured_output
    if travel_itinerary is None:
        print("No structured output received.")
        return
    print(travel_itinerary.model_dump_json(indent=4))

    

if __name__ == "__main__":
    main("New Delhi", "Vrindavan")
