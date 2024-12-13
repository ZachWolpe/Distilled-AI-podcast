"""
---------------------------------------------------------------------------
004_generate_reel_images.py

Generate images for the reel.

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import load_yaml_config_from_argparse
from dotenv import load_dotenv
import replicate
import time
import os


def generate_images_stablilty_ai(prompt="An astronaut riding a rainbow unicorn, cinematic, dramatic"):
    input = {
        "width": 720,
        "height": 1280,
        "prompt": prompt,
        "refine": "expert_ensemble_refiner",
        "apply_watermark": False,
        "num_inference_steps": 25
    }

    output = replicate.run(
        "stability-ai/sdxl:7762fd07cf82c948538e41f63f77d685e02b063e37e496e96eefd46c929f9bdc",
        input=input
    )
    return output


def save_image(output, sav_loc, img_name='output.png'):
    for index, item in enumerate(output):
        with open(f"{sav_loc}/{img_name}", "wb") as file:
            file.write(item.read())


def process_prompt(subject, prompts):
    processed_prompts = []
    for prompt in prompts:
        formatted_prompt = prompt.replace("[SUBJECT]", subject)
        image_output = formatted_prompt
        processed_prompts.append(image_output)
    return processed_prompts


if __name__ == "__main__":
    print('Generating images...')
    start_time = time.time()
    load_dotenv()

    # load config
    config = load_yaml_config_from_argparse()
    stage_1_config = config['stage_1_generate_script_from_pdf']
    stage_3_config = config['stage_3_generate_reel_script_from_script']
    stage_4_config = config['stage_4_generate_reel_images']
    stage_5_config = config['stage_5_fetch_images_from_google']

    # prepare prompts
    processed_prompts = process_prompt(
        subject=stage_4_config['subject'],
        prompts=stage_4_config['prompts']
    )

    # save location
    sav_loc = stage_1_config['output_dir'] + stage_4_config['image_dir']
    os.makedirs(sav_loc, exist_ok=True)

    # generate images
    for idx, _prompt in enumerate(processed_prompts):
        output = generate_images_stablilty_ai(_prompt)
        save_image(
            output=output,
            sav_loc=stage_1_config['output_dir'] + stage_4_config['image_dir'],
            img_name=f"image_{idx}.png")
        print(f' > image generated and saved to disc : {idx}')

    end_time = time.time()
    print('Images generated and saved successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
