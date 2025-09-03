import requests
import time
import json

def upload_file(filename, api_key):
    """
    Uploads a local file to AssemblyAI's servers.
    ... (rest of the function is unchanged)
    """
    def read_file(filename, chunk_size=5_242_880):
        with open(filename, 'rb') as f:
            while True:
                data = f.read(chunk_size)
                if not data:
                    break
                yield data

    upload_endpoint = "https://api.assemblyai.com/v2/upload"
    headers = {"authorization": api_key}
    
    response = requests.post(upload_endpoint, headers=headers, data=read_file(filename))
    
    if response.status_code == 200:
        return response.json()['upload_url']
    else:
        print(f"Error uploading file: {response.text}")
        return None

def transcribe_audio(audio_url, api_key):
    """
    Starts a new transcription job with sentiment analysis.
    ... (rest of the function is unchanged)
    """
    transcript_endpoint = "https://api.assemblyai.com/v2/transcript"
    headers = {
        "authorization": api_key,
        "content-type": "application/json"
    }
    
    data = {
        "audio_url": audio_url,
        "sentiment_analysis": True
    }
    
    response = requests.post(transcript_endpoint, json=data, headers=headers)
    
    if response.status_code == 200:
        return response.json()['id']
    else:
        print(f"Error starting transcription: {response.text}")
        return None

def poll_transcription(transcript_id, api_key, output_filename="results.json"):
    """
    Waits for a transcription job to complete and saves the result to a JSON file.
    
    Args:
        transcript_id (str): The ID of the transcription job.
        api_key (str): Your AssemblyAI API key.
        output_filename (str): The name of the file to save the results to.
        
    Returns:
        tuple: A tuple containing the result dictionary and an error message (if any).
    """
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    headers = {"authorization": api_key}
    
    while True:
        response = requests.get(polling_endpoint, headers=headers)
        result = response.json()
        
        if result['status'] == 'completed':
            # Add a new block to save the results to a file
            with open(output_filename, 'w') as f:
                json.dump(result, f, indent=4)
            print(f"Transcription results saved to {output_filename}")
            return result, None
            
        elif result['status'] == 'error':
            return None, result['error']
        
        print("Waiting for transcription to complete...")
        time.sleep(5)