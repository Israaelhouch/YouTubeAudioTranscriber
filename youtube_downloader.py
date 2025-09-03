import yt_dlp

def get_video_info(url):
    """
    Extracts video information without downloading.

    Args:
        url (str): The URL of the video or playlist.

    Returns:
        dict: The video information dictionary, or None if an error occurs.
    """
    ydl_opts = {'quiet': True, 'noplaylist': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info_dict = ydl.extract_info(url, download=False)
            if 'entries' in info_dict:
                return info_dict['entries'][0]
            return info_dict
        except Exception:
            return None

def get_audio_url(info_dict):
    """
    Finds the URL for the best audio stream from video information.

    Args:
        info_dict (dict): The video information dictionary from get_video_info.

    Returns:
        str: The URL of the audio stream, or None if not found.
    """
    if info_dict and 'formats' in info_dict:
        # Sort formats by audio bitrate to find the highest quality
        best_audio = sorted(
            [f for f in info_dict['formats'] if f.get('acodec') != 'none'],
            key=lambda x: x.get('audio_bitrate', 0),
            reverse=True
        )
        if best_audio:
            return best_audio[0]['url']
    return None

def download_audio_from_url(audio_url, output_path='temp_audio.m4a'):
    """
    Downloads audio from a specific URL using yt-dlp.

    Args:
        audio_url (str): The direct URL of the audio stream.
        output_path (str): The desired local path to save the file.

    Returns:
        str: The local path of the downloaded file, or None if the download fails.
    """
    ydl_opts = {
        'outtmpl': output_path,
        'quiet': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            ydl.download([audio_url])
            return output_path
        except Exception as e:
            print(f"Error downloading audio: {e}")
            return None