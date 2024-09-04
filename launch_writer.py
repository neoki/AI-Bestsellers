import logging
import openai
import warnings
import argparse
import os
import json
import multiprocessing
from datetime import datetime
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Configurar logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Importaciones de módulos personalizados
from ai_bestseller.generate_ideas import generate_ideas
from ai_bestseller.perform_writing import perform_writing
from ai_bestseller.perform_editing import perform_editing
from ai_bestseller.perform_literary_critique import perform_literary_critique

# Función para procesar cada idea
def do_idea(base_dir, results_dir, idea):
    # Generate a timestamp and create a unique folder for the idea
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    idea_name = f"{timestamp}_{idea['Title']}"
    folder_name = os.path.join(results_dir, idea_name)
    os.makedirs(folder_name, exist_ok=True)
    logging.info(f"Created folder: {folder_name}")
    
    chapters = []  # Initialize chapters as an empty list

    try:
        # Writing the chapters
        logging.info(f"Starting writing for idea: {idea_name}")
        chapters = perform_writing(idea, folder_name)
        
        if not chapters:
            logging.info("No chapters were generated due to user stopping the process.")
            return False

        # Editing the manuscript
        logging.info("Editing the manuscript...")
        edited_manuscript = perform_editing(chapters)
        logging.info(f"Edited manuscript length: {len(edited_manuscript)}")

        # Performing literary critique
        logging.info("Performing literary critique...")
        critique = perform_literary_critique(edited_manuscript)
        logging.info(f"Critique length: {len(critique)}")

        # Saving the final manuscript
        manuscript_path = os.path.join(folder_name, "manuscript.txt")
        with open(manuscript_path, "w", encoding="utf-8") as f:
            f.write(edited_manuscript)
        logging.info(f"Saved manuscript to: {manuscript_path}")

        # Saving the critique
        critique_path = os.path.join(folder_name, "critique.txt")
        with open(critique_path, "w", encoding="utf-8") as f:
            f.write(critique)
        logging.info(f"Saved critique to: {critique_path}")

        return True
    except Exception as e:
        logging.error(f"Failed to process idea {idea_name}: {str(e)}", exc_info=True)
        return False



# Función de trabajador para procesamiento en paralelo
def worker(queue, base_dir, results_dir):
    while True:
        idea = queue.get()
        if idea is None:
            break
        success = do_idea(base_dir, results_dir, idea)
        print(f"Completed idea: {idea['Title']}, Success: {success}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Bestseller Writer")
    parser.add_argument("--output_dir", type=str, default="results", help="Output directory")
    parser.add_argument("--parallel", type=int, default=0, help="Number of parallel processes to run. 0 for sequential execution.")
    parser.add_argument("--num_ideas", type=int, default=3, help="Number of ideas to generate")
    args = parser.parse_args()

    base_dir = "templates"
    results_dir = args.output_dir
    os.makedirs(results_dir, exist_ok=True)
    logging.info(f"Results directory: {results_dir}")

    # Generar ideas utilizando GPT-4o a través de la API de OpenAI
    ideas = generate_ideas(num_ideas=args.num_ideas)
    logging.info(f"Generated {len(ideas)} ideas")

    # Guardar las ideas generadas
    with open(os.path.join(base_dir, "ideas.json"), "w") as f:
        json.dump(ideas, f, indent=4)
    logging.info(f"Ideas saved to {os.path.join(base_dir, 'ideas.json')}")

    # Ejecutar en paralelo si se especifica
    if args.parallel > 0:
        logging.info(f"Running {args.parallel} parallel processes")
        queue = multiprocessing.Queue()
        for idea in ideas:
            queue.put(idea)

        processes = []
        for _ in range(args.parallel):
            p = multiprocessing.Process(
                target=worker,
                args=(queue, base_dir, results_dir)
            )
            p.start()
            processes.append(p)

        for _ in range(args.parallel):
            queue.put(None)

        for p in processes:
            p.join()

        logging.info("All parallel processes completed.")
    else:
        for idea in ideas:
            logging.info(f"Processing idea: {idea['Title']}")
            success = do_idea(base_dir, results_dir, idea)
            logging.info(f"Completed idea: {idea['Title']}, Success: {success}")

    logging.info("Bestseller generation complete!")
