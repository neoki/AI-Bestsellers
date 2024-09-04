import logging
from .utils import generate_text


def perform_literary_critique(manuscript):
    logging.info("Performing literary critique...")
    prompt = f"Perform a detailed literary critique of the following manuscript, focusing on plot, character development, pacing, and commercial potential:\n\n{manuscript}\n\nCritique:"
    
    critique = generate_text(prompt, max_tokens=3000)  # Adjust max_tokens if necessary
    return critique

