"""
---------------------------------------------------------------------------
008_put_raw_files_to_s3.py

: zachcolinwolpe@gmail.com
: 13.12.24
---------------------------------------------------------------------------
"""

from prompt_engine import load_yaml_config_from_argparse
from dotenv import load_dotenv
import boto3
import time
import os


if __name__ == "__main__":
    print('Uploading files to S3...')
    start_time = time.time()

    # load env
    load_dotenv()
    s3_bucket = os.getenv('EPISODE_S3_BUCKET')

    # load config
    config = load_yaml_config_from_argparse()
    stage_1_config = config['stage_1_generate_script_from_pdf']
    files_to_upload = stage_1_config['output_dir']

    # Initialize S3 client
    s3_client = boto3.client('s3')

    # create path in s3 bucket called: files_to_upload

    # Upload all OUTPUT files ------------------------------------------------------------------------>>
    for filename in os.listdir(files_to_upload):
        print(f' > uploading file: {filename}')
        if os.path.isfile(os.path.join(files_to_upload, filename)):
            # s3_client.upload_fileobj(filename, s3_bucket, Key=(files_to_upload + '/'))

            with open(os.path.join(files_to_upload, filename), "rb") as f:
    
                if files_to_upload.startswith('./'):
                    files_to_upload = files_to_upload[2:]

                if files_to_upload.endswith('/'):
                    files_to_upload = files_to_upload[:-1]

                # upload to S3
                # s3_client.upload_fileobj(f, s3_bucket, Key=(files_to_upload + '/' + filename))
    # Upload all OUTPUT files ------------------------------------------------------------------------>>

    # Upload all INPUT files ------------------------------------------------------------------------->>
    path_to_pdf = stage_1_config['path_to_pdf']  # pdf input
    pdf_name = os.path.basename(path_to_pdf)
    config_file = 'runtime.yml'  # upload config file for documentation

    # Upload pdf file to S3
    with open(path_to_pdf, "rb") as f:
        print(f' > uploading file: {pdf_name}')
        s3_client.upload_fileobj(f, s3_bucket, Key=(files_to_upload + '/' + pdf_name))

    # Upload config file to S3
    with open(config_file, "rb") as f:
        print(f' > uploading file: {config_file}')
        s3_client.upload_fileobj(f, s3_bucket, Key=(files_to_upload + '/' + config_file))
    # Upload all INPUT files ------------------------------------------------------------------------->>

    end_time = time.time()
    print(f'Files uploaded from {files_to_upload} to S3:{s3_bucket} successfully.')

    # Calculate and print execution time
    execution_time = end_time - start_time
    print(f'Execution time: {execution_time:.2f} seconds')


# Linux commands:
# REMOVE:
# aws s3 rm s3://<S3-BUCKET>/episodes --recursive
# LIST:
# aws s3 ls s3://<S3-BUCKET>
