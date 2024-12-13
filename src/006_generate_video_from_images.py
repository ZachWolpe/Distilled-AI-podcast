"""
---------------------------------------------------------------------------
006_generate_video_from_images.py

Generate video from images.

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import load_yaml_config_from_argparse
from dotenv import load_dotenv
import replicate
import random
import time
import os


def list_files_in_directory(directory):
    """List all files in the given directory."""
    return [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]


if __name__ == "__main__":
    print('Generate video from images...')
    start_time = time.time()
    load_dotenv()

    # load config and query prompt
    config = load_yaml_config_from_argparse()
    stage_1_config = config['stage_1_generate_script_from_pdf']
    stage_4_config = config['stage_4_generate_reel_images']
    stage_5_config = config['stage_5_fetch_images_from_google']

    # load all images paths
    AI_generated_images_path = stage_1_config['output_dir'] + stage_4_config['image_dir']
    google_images_path = stage_1_config['output_dir'] + stage_5_config['image_dir']

    # List files in AI generated images directory
    ai_generated_files = list_files_in_directory(AI_generated_images_path)
    google_images_files = list_files_in_directory(google_images_path)

    # keep 2 samples
    sampled_ai_generated_files = random.sample(ai_generated_files, 2) if len(ai_generated_files) >= 2 else ai_generated_files
    sampled_google_images_files = random.sample(google_images_files, 2) if len(google_images_files) >= 2 else google_images_files

    sampled_ai_generated_files_full_path = [os.path.join(AI_generated_images_path, file) for file in sampled_ai_generated_files]
    sampled_google_images_files_full_path = [os.path.join(google_images_path, file) for file in sampled_google_images_files]

    _files = sampled_ai_generated_files_full_path + sampled_google_images_files_full_path

    # create model input
    _input = {}
    for idx, file in enumerate(_files):
        # convert to uri
        file_uri = open(file, "rb")
        _input[f'image_{idx+1}'] = file_uri
        # print('>> ', file_uri)

    # inference
    output = replicate.run(
        "fofr/tooncrafter:0486ff07368e816ec3d5c69b9581e7a09b55817f567a0d74caad9395c9295c77",
        input=_input
    )

    # save file
    OUTPUT_PATH = stage_1_config['output_dir']
    for index, item in enumerate(output):
        with open(f"{OUTPUT_PATH}raw_reel_clip_{index}.mp4", "wb") as file:
            file.write(item.read())

    end_time = time.time()
    print('Video created successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
