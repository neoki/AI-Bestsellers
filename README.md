
# AI-Bestsellers

![logo](logo.png)

**AI-Bestsellers** is an advanced AI-based tool designed to write complete books. It is highly adaptable to any literary genre or writing style, making it ideal for generating novels, short stories, essays, or any kind of text.

### Features:
- **Adaptable to any literary genre**: From science fiction to romance or even cybersecurity technical books.
- **Custom length**: Specify the number of chapters, word count, or other content length parameters.
- **Automated critique**: Includes a built-in module that acts as a literary critic to enhance the quality of the generated text.
- **Easy model integration**: Though the default setup uses GPT, it’s easy to modify the code to work with other language models.
- **User-friendly GUI coming soon**: A graphical interface will soon be added to make the application even easier to use.

## Installation

### Python

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/AI-Bestsellers.git
   cd AI-Bestsellers
   ```

2. Set up a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your OpenAI API key (or the key of any other language model service you're using).

5. Run the AI to start writing books:

   ```bash
   python launch_writer.py --max-bacon 5
   ```

   The AI will generate the book based on the provided prompt and specifications. You can tweak parameters like the number of chapters, style, and length.

### Docker

Alternatively, you can run AI-Bestsellers using Docker.

1. Build the Docker image:

   ```bash
   docker build -t ai-bestsellers .
   ```

2. Run the container:

   ```bash
   docker run -it --env OPENAI_API_KEY=<your_api_key> ai-bestsellers
   ```

   This will start the AI, and you can interact with it by passing prompt and other options to generate the books as desired.

## Roadmap

- A GUI for easier use without command line interaction.
- More fine-tuned models for specific genres.
- Expand the project to handle non-English book generation.
- Pretrained models to mimic specific literary authors or styles.

---

This project is an adaptation and expansion of the original work done in [AI-Scientist](https://github.com/SakanaAI/AI-Scientist). Major thanks to the original contributors.
