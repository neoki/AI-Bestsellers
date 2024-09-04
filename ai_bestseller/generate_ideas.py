import logging
from .utils import generate_text  # Asumiendo que hemos movido generate_text a un archivo utils.py


def generate_ideas(num_ideas=3):
    logging.info(f"Generating {num_ideas} ideas")
    prompt = "Generate unique and captivating ideas for bestselling novels. Each idea should include a brief plot summary, main characters, and setting:\n\n1."
    
    raw_ideas = generate_text(prompt, max_tokens=512)
    logging.info(f"Raw ideas generated, length: {len(raw_ideas)}")
    
    # Process and format the ideas
    ideas = raw_ideas.split("\n\n")
    formatted_ideas = []
    for i, idea in enumerate(ideas[:num_ideas], 1):
        formatted_idea = {
            "Title": f"Novel Idea {i}",
            "Summary": idea.strip()
        }
        formatted_ideas.append(formatted_idea)
        logging.info(f"Processed idea {i}: {formatted_idea['Title']}")
    
    return formatted_ideas

