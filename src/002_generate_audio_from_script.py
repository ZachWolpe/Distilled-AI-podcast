"""
---------------------------------------------------------------------------
002_generate_audio_from_script.py

Resource:
    https://replicate.com/cjwbw/parler-tts/
    https://huggingface.co/datasets/ylacombe/parler-tts-mini-v1-a_speaker_similarity

: zachcolinwolpe@gmail.com
: 12.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import read_script, load_yaml_config_from_argparse
from prompts.prompts import prompt_generate_audio_from_script
from dotenv import load_dotenv
from openai import OpenAI
import replicate
import time
import os
import re


# use openAI or replicate ------------------------------------------------------->>
OPEN_AI_TTS = True
REPLICATE_TTS = False

if OPEN_AI_TTS and REPLICATE_TTS:
    raise ValueError("Select one TTS engine, both currently activated.")

if not OPEN_AI_TTS and not REPLICATE_TTS:
    raise ValueError("Select one TTS engine, none currently selected.")
# use openAI or replicate ------------------------------------------------------->>


def remove_brackets_and_words(text):
    # Use regex to remove text within square brackets
    return re.sub(r'\[.*?\]', '', text).strip()


if __name__ == "__main__":
    print('Generating audio...')
    start_time = time.time()  # Start timing execution
    load_dotenv()  # Load environment variables from .env file

    # load config
    config = load_yaml_config_from_argparse()
    stage_2_config = config['stage_2_generate_audio_from_script']

    # load and clean script
    output_loc = config['stage_1_generate_script_from_pdf']['output_dir']
    path_to_script = output_loc + config['stage_1_generate_script_from_pdf']['output_name']
    script = read_script(path_to_script)
    clean_script = remove_brackets_and_words(script)
    clean_script_name = stage_2_config['clean_script_name']
    with open(f"{output_loc}/{clean_script_name}", "w") as file:
        file.write(clean_script)

    AUDIO_FILE_NAME = stage_2_config['audio_output_name']
    AUDIO_OUTPUT_PATH = f"{output_loc}/{AUDIO_FILE_NAME}"

    # load API keys
    if OPEN_AI_TTS:
        # use Open AI TTS API
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

        client = OpenAI()
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=clean_script
            )
        response.stream_to_file(AUDIO_OUTPUT_PATH)

    else:
        # Use Replicate (Parler-TTS) API
        REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

        # query replicate API
        _query = {
            "prompt": clean_script,
            "description": prompt_generate_audio_from_script.prompt_001()
        }
        output = replicate.run(
            "cjwbw/parler-tts:bf38249a8cc143b97b5108570d1c81b8321881dd91fe7837877e7dfa3a0fad27",
            input=_query,
            )
        with open(AUDIO_OUTPUT_PATH, "wb") as file:
            file.write(output.read())

    end_time = time.time()
    print('Audio generated and saved successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
