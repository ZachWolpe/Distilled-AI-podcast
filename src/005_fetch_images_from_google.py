"""
---------------------------------------------------------------------------
005_fetch_images_from_google.py

Fetch images from Google.

Documentation:
    https://icrawler.readthedocs.io/_/downloads/en/latest/pdf/

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import load_yaml_config_from_argparse
from icrawler.builtin import GoogleImageCrawler
from dotenv import load_dotenv
from PIL import Image
import shutil
import time
import os


def google_image_search(keyword='Nikola Tesla', max_num=5, save_loc='./'):
    """
    Documentation:
        https://icrawler.readthedocs.io/_/downloads/en/latest/pdf/
    """
    print('>>>>>> launching job...., save_loc: ', save_loc)
    google_Crawler = GoogleImageCrawler(storage={'root_dir': save_loc})
    google_Crawler.crawl(keyword=keyword, max_num=max_num)
    print('>>>>>> FINISH job')



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

    print('save:loc', save_loc)
    exit

    for idx, keyword in enumerate(stage_5_config['keywords']):
        batch_directory = save_loc + f'batch_{idx}/'
        print('::batch_directory : ', batch_directory)

        # create batch_dir
        os.makedirs(batch_directory, exist_ok=True)

        google_image_search(
            keyword=keyword,
            max_num=stage_5_config['n_images_per_keyword'],
            save_loc=batch_directory
        )

        # move to main directory
        print('SAVE COMPLETE -----> -----> MOVE TO MAIN DIR.')
        break
    #     for file in os.listdir(batch_directory):
    #         if file.endswith(('.png', '.jpg', '.jpeg')):
    #             old_path = batch_directory + f'/{file}'
    #             new_path = save_loc + f'/{file}'
    #             # os.rename(old_path, new_path)
    #             # updated
    #             # move to new dir
    #             shutil.move(old_path, new_path)
    #     try:
    #         shutil.rmtree(batch_directory)
    #     except Exception as e:
    #         _error = f"""

    #             Unable to rmtree (directory)
    #             old_path : {old_path}
    #             new_path : {new_path}

    #             Exception: {e}
    #         """
    #         print(_error)

    # # read and resize image
    # for img_file in os.listdir(save_loc):
    #     if img_file.endswith(('.png', '.jpg', '.jpeg')):
    #         img_path = os.path.join(save_loc, img_file)
    #         resized_image = resize_image(img_path)
    #         resized_image.save(img_path)  # Overwrite the original image with the resized one

    # end_time = time.time()
    # print('Images downloaded successfully.')

    # # Calculate and print execution time
    # execution_time = end_time - start_time
    # print(f'Execution time: {execution_time:.2f} seconds')
