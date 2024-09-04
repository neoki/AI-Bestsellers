import logging
from .utils import generate_text


def perform_editing(chapters):
    logging.info("Editing the manuscript...")
    edited_chapters = []
    for i, chapter in enumerate(chapters):
        prompt = f"Edit and improve the following chapter for clarity, pacing, and engaging storytelling:\n\n{chapter}\n\nEdited version:"
        edited_chapter = generate_text(prompt)
        edited_chapters.append(edited_chapter)
        logging.info(f"Chapter {i+1} edited.")
    
    edited_manuscript = "\n\n".join(edited_chapters)
    return edited_manuscript
