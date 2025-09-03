# main.py

import os
from dotenv import load_dotenv
from youtube_downloader import get_video_info, get_audio_url, download_audio_from_url
from transcriber import upload_file, transcribe_audio, poll_transcription


load_dotenv()
API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

def main(video_url):
    """
    Main function to orchestrate the video transcription process.
    """
    if not API_KEY:
        print("Error: ASSEMBLYAI_API_KEY not found. Please set it in your .env file.")
        return

    print("1. Extracting audio URL from YouTube...")
    video_info = get_video_info(video_url)
    audio_url_from_youtube = get_audio_url(video_info)
    
    if not audio_url_from_youtube:
        print("Failed to get audio URL.")
        return

    print("2. Downloading audio file locally...")
    local_audio_path = download_audio_from_url(audio_url_from_youtube)
    
    if not local_audio_path:
        print("Failed to download audio.")
        return

    print("3. Uploading file to AssemblyAI...")
    uploaded_url = upload_file(local_audio_path, API_KEY)
    os.remove(local_audio_path) # Clean up the local file

    if not uploaded_url:
        print("Failed to upload audio.")
        return

    print("4. Starting transcription job...")
    transcript_id = transcribe_audio(uploaded_url, API_KEY)
    
    if not transcript_id:
        print("Failed to get transcription ID.")
        return

    print(f"5. Polling for results (ID: {transcript_id})...")
    results, error = poll_transcription(transcript_id, API_KEY, "transcription_results.json")
    
    if error:
        print(f"An error occurred: {error}")
    else:
        print("\nTranscription Complete!")
        # Print a nicely formatted summary of the sentiment analysis results
        for sentiment in results.get('sentiment_analysis_results', []):
            print(f"\nText: {sentiment.get('text')}")
            print(f"Sentiment: {sentiment.get('sentiment')}")
            print(f"Confidence: {sentiment.get('confidence'):.2f}")
            print(f"Time: {sentiment.get('start')}ms - {sentiment.get('end')}ms")

if __name__ == "__main__":

    youtube_video_url = "https://www.youtube.com/watch?v=mYUyaKmvu6Y"
    main(youtube_video_url)