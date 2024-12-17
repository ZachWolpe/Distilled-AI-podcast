#!/bin/bash

# grant access to terminal
# chmod +x ./execute_run.sh

# execute pipeline...
# ... existing code ...

log_and_execute() {
    script_path=$1
    echo "Executing script: ${script_path}...."
    python "${script_path}"
    echo "Script executed successfully."
}

# execute pipeline...
# log_and_execute "src/001_generate_podcast_script.py"
# log_and_execute "src/002_generate_audio_from_script.py"
# log_and_execute "src/003_generate_reel_script.py"
# log_and_execute "src/004_generate_reel_images.py"
log_and_execute "src/005_fetch_images_from_google.py"
# log_and_execute "src/006_generate_video_from_images.py"
# log_and_execute "src/007_generate_audio_from_reel_script.py"
# log_and_execute "src/008_put_raw_files_to_s3.py"
# fin!
# fin!