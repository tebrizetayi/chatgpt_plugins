import openai
import re
from fastapi import FastAPI

# Set up the OpenAI API key
openai.api_key = "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"

# Create an instance of a FastAPI application
app = FastAPI()

# Define a route that accepts POST requests to generate a response
@app.post("/generate_response")
def generate_response(message: str):
    # Use OpenAI's GPT-3 to generate a response to the message
    prompt = f"Conversation with user:\nUser: {message}\nBot:"
    print(prompt)
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated response from the OpenAI API response
    answer = response.choices[0].text.strip()

    # Clean up the response by removing newlines and extra whitespace
    answer = re.sub(r"\s+", " ", answer)

    # Return the response
    return {"answer": answer}
