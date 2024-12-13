"""
---------------------------------------------------------------------------
003_generate_reel_script.py

Summarise script for a reel.

: zachcolinwolpe@gmail.com
: 12.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import write_to_file, load_yaml_config_from_argparse
from prompts.prompts import prompt_generate_reel_from_script
import google.generativeai as genai
from dotenv import load_dotenv
import time
import os


# use openAI or replicate ------------------------------------------------------->>
OPEN_AI_TTS = True
REPLICATE_TTS = False

if OPEN_AI_TTS and REPLICATE_TTS:
    raise ValueError("Select one TTS engine, both currently activated.")

if not OPEN_AI_TTS and not REPLICATE_TTS:
    raise ValueError("Select one TTS engine, none currently selected.")
# use openAI or replicate ------------------------------------------------------->>


if __name__ == "__main__":
    print('Generating audio...')
    start_time = time.time()  # Start timing execution
    load_dotenv()  # Load environment variables from .env file

    # load config
    config = load_yaml_config_from_argparse()
    stage_2_config = config['stage_2_generate_audio_from_script']
    stage_3_config = config['stage_3_generate_reel_script_from_script']

    # load clean script
    clean_script_loc = f"{config['stage_1_generate_script_from_pdf']['output_dir']}/{stage_2_config['clean_script_name']}"
    with open(clean_script_loc, "r") as file:
        clean_script = file.read()

    # generate & save reel prompt
    reel_prompt = prompt_generate_reel_from_script.get_reel_script_prompt(clean_script)
    with open(f"{config['stage_1_generate_script_from_pdf']['output_dir']}/{stage_3_config['real_prompt_name']}", "w") as file:
        file.write(reel_prompt)

    # Gemini API: generate reel script
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(reel_prompt)
    reel_script = response.text

    # save response
    save_loc = config['stage_1_generate_script_from_pdf']['output_dir']
    os.makedirs(save_loc, exist_ok=True)
    write_to_file(
        text=reel_script,
        path=save_loc + stage_3_config['output_name'])

    end_time = time.time()
    print('Reel script generated and saved successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
