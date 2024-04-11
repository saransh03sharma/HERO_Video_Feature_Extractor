from moviepy.editor import VideoFileClip

def is_mp4_file_valid(file_path):
    try:
        video_clip = VideoFileClip(file_path)
        # Attempt to read the duration of the video.
        duration = video_clip.duration
        # If the duration is successfully retrieved, the file is likely valid.
        return True, duration
    except Exception as e:
        # An exception occurred, indicating potential corruption or an unsupported format.
        return False, str(e)

# Specify the path to the MP4 file you want to check
mp4_file_path = "/video/https:____www.behance.net__videos__632fffaf-f8ae-4c75-bcaf-91ea4f8ddfb6__Daily-Projects-with-Klarens-Malluta.mp4"

# Check if the MP4 file is valid
is_valid, duration = is_mp4_file_valid(mp4_file_path)

if is_valid:
    print(f"The MP4 file is valid. Duration: {duration} seconds")
else:
    print(f"The MP4 file is not valid. Error: {duration}")
