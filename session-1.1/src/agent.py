import os

from strands import Agent
from strands.models import BedrockModel

from dotenv import load_dotenv

load_dotenv()


BEDROCK_MODEL = BedrockModel(
    model_id=os.environ.get("BEDROCK_MODEL_ARN", ""),
    region_name="us-east-1",
    max_tokens=2000,
)

def main():
    agent = Agent(model=BEDROCK_MODEL)

    text_file = "dummy_file.txt"
    text_file_contents = ""
    with open(text_file, "r") as file:
        text_file_contents = file.read()


    prompt = f"""
    You are a summarization agent. Given a text file contents,
    your task is to summarize the contents of the text file.

    ---
    Text file contents:
    {text_file_contents}
    """

    result = agent(prompt)
    print(result.message)

if __name__ == "__main__":
    main()
