"""
---------------------------------------------------------------------------
002_generate_audio_from_reel_script.py

Resource:
    https://replicate.com/cjwbw/parler-tts/
    https://huggingface.co/datasets/ylacombe/parler-tts-mini-v1-a_speaker_similarity

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

import google.generativeai as genai
from prompt_engine import write_to_file, read_script, load_yaml_config_from_argparse
from prompts.prompts import prompt_generate_audio_from_script
from dotenv import load_dotenv
from pathlib import Path
from openai import OpenAI
from dotenv import load_dotenv
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


def clean_reel_script(script):
    """
    Clean the reel script by removing:
    1. Scene descriptions in parentheses
    2. Timing information and "Voiceover:" markers
    3. Hashtags at the end

    Args:
        script (str): The original reel script text

    Returns:
        str: Cleaned script with only the narration text
    """
    # Remove scene descriptions and timing/voiceover markers
    # Matches anything between ** and **
    script = re.sub(r'\*\*.*?\*\*', '', script)

    # Remove "(Slightly more serious tone)" type descriptions
    script = re.sub(r'\([^)]*\)', '', script)

    # Remove hashtags at the end
    script = re.sub(r'#\w+', '', script)

    # Remove extra whitespace and blank lines
    lines = [line.strip() for line in script.split('\n') if line.strip()]
    cleaned_script = '\n\n'.join(lines)

    return cleaned_script


def add_podcast_plug(script, podcast_plug="\n\nGet the full story in the latest eposide of the Spark podcast! Available now on Spotify."):
    return script + podcast_plug


if __name__ == "__main__":
    print('Generating audio...')
    start_time = time.time()  # Start timing execution
    load_dotenv()  # Load environment variables from .env file

    # load config
    config = load_yaml_config_from_argparse()
    stage_3_config = config['stage_3_generate_reel_script_from_script']
    stage_7_config = config['stage_7_generate_audio_from_reel_script']
    stage_7_config['clean_reel_script_name']
    stage_7_config['audio_reel_output_name']

    # load and clean script
    output_loc = config['stage_1_generate_script_from_pdf']['output_dir']

    # Load the reel script
    path_to_reel_script = output_loc + stage_3_config['output_name']
    with open(path_to_reel_script, 'r') as file:
        reel_script = file.read()

    # clean script
    processed_reel_script = clean_reel_script(reel_script)
    processed_reel_script = add_podcast_plug(processed_reel_script)
    with open(f"{output_loc}/{stage_7_config['clean_reel_script_name']}", 'w') as file:
        file.write(processed_reel_script)

    # TTS
    AUDIO_OUTPUT_PATH = f"{output_loc}/{stage_7_config['audio_reel_output_name']}"

    # load API keys
    if OPEN_AI_TTS:
        # use Open AI TTS API
        OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

        client = OpenAI()
        response = client.audio.speech.create(
            model="tts-1",
            voice="alloy",
            input=processed_reel_script
            )
        response.stream_to_file(AUDIO_OUTPUT_PATH)

    else:
        # Use Replicate (Parler-TTS) API
        REPLICATE_API_TOKEN = os.getenv('REPLICATE_API_TOKEN')

        # query replicate API
        _query = {
            "prompt": processed_reel_script,
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
