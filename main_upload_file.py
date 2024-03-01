from download_video import download_video
from openai_api import call_openai_api
import subprocess
import argparse

def run_diarization_command(id):
    command = ["python", "whisper-diarization/diarize_parallel.py", "-a", f"audio/{id}"]
    try:
        subprocess.run(command, check=True)
    except subprocess.CalledProcessError as e:
        print("Error:", e)


        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, help='File name of the audio')
    parser.add_argument('api_key', type=str, help='The openai api key.')
    parser.add_argument('prompt', type=str, nargs='?', default='multi-speakers', help='Prompt for summarization.')
    args = parser.parse_args()

    id = args.file_name
    run_diarization_command(id)
    call_openai_api(id, args.prompt, args.api_key)


    # url = "https://www.youtube.com/watch?v=ImrKxlLJCEY"
    # url = "https://www.youtube.com/watch?v=gRTBRV2_S5Q"
