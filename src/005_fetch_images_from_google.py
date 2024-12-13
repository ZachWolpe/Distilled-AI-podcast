"""
---------------------------------------------------------------------------
005_fetch_images_from_google.py

Fetch images from Google.

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import load_yaml_config_from_argparse
from icrawler.builtin import GoogleImageCrawler
from dotenv import load_dotenv
from PIL import Image
import time
import os


def google_image_search(keyword='Nikola Tesla', max_num=5, save_loc='./'):
    google_Crawler = GoogleImageCrawler(storage={'root_dir': save_loc})
    google_Crawler.crawl(keyword=keyword, max_num=max_num)


def resize_image(img, width=1080, height=1920):
    with Image.open(img) as image:
        resized_image = image.resize((width, height), Image.ANTIALIAS)
        return resized_image


if __name__ == "__main__":
    print('Fetching images from Google...')
    start_time = time.time()
    load_dotenv()

    # load config and query prompt
    config = load_yaml_config_from_argparse()
    stage_1_config = config['stage_1_generate_script_from_pdf']
    stage_5_config = config['stage_5_fetch_images_from_google']

    save_loc = stage_1_config['output_dir'] + stage_5_config['image_dir']
    os.makedirs(save_loc, exist_ok=True)
    google_image_search(
        keyword=stage_5_config['keyword'],
        max_num=5,
        save_loc=save_loc
    )

    # read and resize image
    for img_file in os.listdir(save_loc):
        if img_file.endswith(('.png', '.jpg', '.jpeg')):
            img_path = os.path.join(save_loc, img_file)
            resized_image = resize_image(img_path)
            resized_image.save(img_path)  # Overwrite the original image with the resized one

    end_time = time.time()
    print('Images downloaded successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')
