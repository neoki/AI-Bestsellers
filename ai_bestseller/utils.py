import os
import logging
from openai import OpenAI

# Initialize the OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_text(prompt, max_tokens=6000):
    logging.info(f"Generating text with prompt: {prompt[:50]}...")
    
    response = client.chat.completions.create(
        model="gpt-4",  # Use "gpt-4o" if available
        messages=[
            {"role": "system", "content": "You are a renowned science fiction writer who specializes in creating bestselling novels."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=max_tokens,
        temperature=0.7,
    )
    
    generated_text = response.choices[0].message.content.strip()  # Corrected access method
    logging.info(f"Generated text of length: {len(generated_text)}")
    return generated_text

