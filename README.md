# Spark Podcast 💣


Summaries of &amp; discussion about great stories, primarily (auto)-biographies. Particular of great engineers throughout history. Written and read by AI.


Podcast available on [Spotify](https://podcasters.spotify.com/pod/show/distilled-audio).


#### Stack:

- [Gemini](https://ai.google.dev/)
- [ChatGPT-TTS](https://platform.openai.com/docs/guides/text-to-speech)
- [Replicate (Parler-TTS)](https://replicate.com/cjwbw/parler-tts)
- OpenCV
- Python


----
# Project Structure

- The core directory hosts the entire project, links, instructions, and resources.
- Everything in the `src` directory can run independently, and will eventually be packaged into a docker container to run on `EC2`.


----
# Project Architecture

![Module 1](https://github.com/ZachWolpe/Distilled-AI-podcast/blob/main/assets/architecture/module%201-a.png)
![Module 2](https://github.com/ZachWolpe/Distilled-AI-podcast/blob/main/assets/architecture/module%202.png)
![Module 3](https://github.com/ZachWolpe/Distilled-AI-podcast/blob/main/assets/architecture/module%203.png)

---
# Build

### 1. Create and activate the conda environment:

##### Option 1: Using the environment file directly:

```bash
conda env create -f environment.yml
conda activate spark-podcast
```

##### Option 2: Using the setup script:
    
```bash
chmod +x ./config/setup.sh
./config/setup.sh
```

Activate the environment

```bash
conda activate spark-podcast
```


### 2. Link `.env` file:

```bash
source .env
```

### 3. Generate the podcast script:

```bash
python src/001_generate_podcast_script.py --yaml_path './src/runtime.yml'
```



### N. (Optional) Run the test suite.

```bash
python src/prompt_engine.py --yaml_path './src/runtime.yml'
```










----
# DevOps Architecture

<Coming Soon>


---
# Core Resources

#### Excellent LLM Resources:

- [HuggingChat](https://huggingface.co/chat/)
- [https://www.promptingguide.ai/](https://www.promptingguide.ai/)
- [OpenGVLab - VisionLLM](https://github.com/OpenGVLab/VisionLLM/tree/main/VisionLLM)
- [Parler-TTS](https://github.com/huggingface/parler-tts)
- [Anything LLM](https://anythingllm.com/)
- [groq](https://groq.com/)
- [firecrawl](https://www.firecrawl.dev/)
- [Llama Parse](https://github.com/run-llama/llama_parse)
- [NotebookLlama](https://github.com/meta-llama/llama-recipes/tree/main/recipes/quickstart/NotebookLlama)


Compare LLMs:

- [🏆 Chatbot Arena LLM Leaderboard](https://lmarena.ai/)
- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)


#### Text To Speech (TTS) Resources:

- [Eleven Labs API](https://elevenlabs.io/api)
- [TTS Arena: Benchmarking TTS Models in the Wild](https://huggingface.co/spaces/TTS-AGI/TTS-Arena)
- [ChatTTS](https://chattts.com/)
- [Parler-TTS](https://github.com/huggingface/parler-tts)
- [GPT-4 TTS](https://platform.openai.com/docs/guides/text-to-speech)




#### What is `RAG`

- [Databricks blog - what is RAG?](https://www.databricks.com/glossary/retrieval-augmented-generation-rag)
- [IMB blog - what is RAG?](https://research.ibm.com/blog/retrieval-augmented-generation-RAG)
- [Nvidia blog - what is RAG?](https://blogs.nvidia.com/blog/what-is-retrieval-augmented-generation/)
- [AWS blog - what is RAG?](https://aws.amazon.com/de/what-is/retrieval-augmented-generation/)




----
# Booklist


| **Title**                                    | **Author**                                  | **Subject**                                                                                 |
|----------------------------------------------|---------------------------------------------|---------------------------------------------------------------------------------------------|
| **Nikola Tesla: My Inventions**              | Nikola Tesla                                | Tesla’s life, inventions, and thoughts on technology.                                       |
| **Steve Jobs**                               | Walter Isaacson                             | The life of Steve Jobs, based on authorized interviews.                                     |
| **Elon Musk: Tesla, SpaceX, and the Quest for a Fantastic Future** | Ashlee Vance                 | Biography of Elon Musk's innovations and vision.                                            |
| **Autobiography of Andrew Carnegie**         | Andrew Carnegie                             | Carnegie’s industrialist journey and philanthropy.                                          |
| **Henry Ford: My Life and Work**             | Henry Ford                                  | Ford’s reflections on revolutionizing the automobile industry.                              |
| **I Am a Mathematician**                     | Norbert Wiener                              | The journey of the father of cybernetics in engineering and mathematics.                    |
| **The Wright Brothers**                      | David McCullough                            | Story of Wilbur and Orville Wright and the invention of flight.                             |
| **Leonardo da Vinci**                        | Walter Isaacson                             | Biography of Leonardo da Vinci’s inventive genius.                                          |
| **Einstein: His Life and Universe**          | Walter Isaacson                             | Life and scientific contributions of Albert Einstein.                                       |
| **Edison: A Biography**                      | Matthew Josephson                           | A study of Thomas Edison’s transformative inventions.                                       |
| **Alexander Graham Bell: Reluctant Genius**  | Charlotte Gray                              | The story of Bell’s invention of the telephone and humanitarian efforts.                    |
| **James Watt: Making the World Anew**        | Ben Russell                                 | Exploration of James Watt’s role in the Industrial Revolution.                              |
| **Ada Lovelace: The Making of a Computer Scientist** | Christopher Hollings, Ursula Martin, Adrian Rice | Biography of Ada Lovelace, the first computer programmer.                            |
| **The Innovators: How a Group of Hackers, Geniuses, and Geeks Created the Digital Revolution** | Walter Isaacson | Stories of tech pioneers, including Alan Turing and Bill Gates.                             |
| **Empire of the Air: The Men Who Made Radio**| Tom Lewis                                   | Stories of radio pioneers Guglielmo Marconi, Lee de Forest, and Edwin Armstrong.            |
| **Frank Lloyd Wright: A Biography**          | Meryle Secrest                              | Biography of Frank Lloyd Wright and his engineering feats in architecture.                  |
| **Howard Hughes: His Life and Madness**      | Donald L. Barlett, James B. Steele          | Life of Howard Hughes, entrepreneur and aviation pioneer.                                   |
| **Building St. Paul’s**                      | James W.P. Campbell                         | Biography of Sir Christopher Wren and his architectural achievements.                       |
| **Skunk Works: A Personal Memoir of My Years at Lockheed** | Ben R. Rich, Leo Janos           | Innovations at Lockheed and stealth technology development.                                 |
| **Becoming Hewlett and Packard: A Personal Biography of the Founders** | Steve W. Hoover                     | Biography of HP’s founders and their partnership.                                           |
| **The Man Behind the Microchip: Robert Noyce and the Invention of Silicon Valley** | Leslie Berlin                      | Life of Robert Noyce, co-founder of Intel and semiconductor pioneer.                        |
| **Only the Paranoid Survive**                | Andrew S. Grove                             | Memoir of Intel’s former CEO and his leadership insights.                                   |
| **The HP Way: How Bill Hewlett and I Built Our Company** | David Packard                        | Story of HP’s founders and their business philosophy.                                       |
| **The Idea Factory: Bell Labs and the Great Age of American Innovation** | Jon Gertner                | History of Bell Labs and its contributions to technology.                                   |
| **The Master Switch: The Rise and Fall of Information Empires** | Tim Wu                           | Exploration of information empires and their impact on society.                             |
| **The Code Breaker: Jennifer Doudna, Gene Editing, and the Future of the Human** | Walter Isaacson | Biography of Jennifer Doudna and the CRISPR gene-editing revolution.




---
```
: 13.12.2024
: zachcolinwolpe@gmail.com
```
----