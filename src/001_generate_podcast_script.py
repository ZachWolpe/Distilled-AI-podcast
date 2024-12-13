"""
---------------------------------------------------------------------------
001_generate_podcast_script.py



: zachcolinwolpe@gmail.com
: 12.12.24
---------------------------------------------------------------------------
"""

import google.generativeai as genai
from prompt_engine import write_to_file, load_yaml_config_from_argparse
from prompts.prompts import prompt_generate_podcast_script_from_pdf
from dotenv import load_dotenv
import time
import os


class dummy_query:
    text = "dummy-text-script"


def generate_script(path_to_book_pdf, system_prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    sample_pdf = genai.upload_file(path_to_book_pdf)
    response = model.generate_content([system_prompt, sample_pdf])
    return response


if __name__ == "__main__":
    print('Generating script...')
    start_time = time.time()  # Start timing execution
    load_dotenv()  # Load environment variables from .env file
    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')  # Access environment variables
    genai.configure(api_key=GEMINI_API_KEY)  # configure API access

    # load config and query prompt
    config = load_yaml_config_from_argparse()
    system_prompt = prompt_generate_podcast_script_from_pdf.prompt_001()
    path_to_book_pdf = config['stage_1_generate_script_from_pdf']['path_to_pdf']

    # query Gemini
    response = generate_script(path_to_book_pdf, system_prompt)
    script = response.text

    # save response
    save_loc = config['stage_1_generate_script_from_pdf']['output_dir']
    os.makedirs(save_loc, exist_ok=True)
    write_to_file(text=script,
                  path=save_loc + config['stage_1_generate_script_from_pdf']['output_name'])

    end_time = time.time()
    print('Script generated and saved successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
