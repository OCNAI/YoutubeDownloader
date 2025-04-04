import os
import yt_dlp
import imageio_ffmpeg

# ========== CONFIGURATION ==========
# Resolution options: 2160 (4K), 1440 (2K), 1080 (Full HD), 720 (HD), etc.
DESIRED_RESOLUTION = "2160"

# File extension for final merged output
FILE_EXTENSION = "mp4"

# Set your download location here
DOWNLOAD_LOCATION = ""
DOWNLOAD_LOCATION = DOWNLOAD_LOCATION.replace("\\", "/")
# ===================================

# Create download folder if it doesn't exist
try:
    if not os.path.exists(DOWNLOAD_LOCATION):
        os.makedirs(DOWNLOAD_LOCATION)
except Exception as e:
    print("Error creating specified folder. Using fallback 'Downloaded videos'")
    DOWNLOAD_LOCATION = "Downloaded videos"
    os.makedirs(DOWNLOAD_LOCATION, exist_ok=True)

# Get ffmpeg binary from imageio
ffmpeg_path = imageio_ffmpeg.get_ffmpeg_exe()

def download_video(url: str, resolution: str, file_extension: str, output_path: str):
    ydl_opts = {
        'format': f'bestvideo[ext={file_extension}][height<={resolution}]+bestaudio[ext=m4a]/best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s'),
        'merge_output_format': file_extension,
        'ffmpeg_location': ffmpeg_path
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("\n✅ Download and merge complete!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url_input = input("Paste the YouTube video URL: ").strip()
    if not url_input:
        print("❌ No URL entered. Exiting.")
    else:
        download_video(url_input, DESIRED_RESOLUTION, FILE_EXTENSION, DOWNLOAD_LOCATION)
