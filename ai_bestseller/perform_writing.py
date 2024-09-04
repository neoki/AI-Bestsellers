import logging
from .utils import generate_text
import os


def perform_writing(idea, folder_name, num_chapters=10):
    chapters = []
    chapter_content = ""
    
    for i in range(num_chapters):
        prompt = f"Write chapter {i+1} for the novel with the following idea:\n{idea['Summary']}\n\nPrevious content:\n{chapter_content}\n\nChapter {i+1}:"
        chapter_content = generate_text(prompt)
        chapter_filename = os.path.join(folder_name, f"Chapter_{i+1}.txt")
        
        # Save the chapter to a file
        with open(chapter_filename, "w", encoding="utf-8") as chapter_file:
            chapter_file.write(f"Chapter {i+1}\n\n{chapter_content}")
        
        logging.info(f"Chapter {i+1} saved to {chapter_filename}")
        
        # Pause and wait for user input
        user_input = input(f"Chapter {i+1} has been generated and saved. Press 'Y' to continue to the next chapter or any other key to stop: ").strip().lower()
        if user_input != 'y':
            logging.info("Writing process stopped by the user.")
            break
        
        chapters.append(chapter_content)
    
    return chapters
