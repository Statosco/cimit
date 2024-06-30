from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_list, output_file):
    clips = [VideoFileClip(video) for video in video_list]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

# Example usage:
video_files = [
    "tik2/a1.mp4",
    "tik2/a2.mp4",
    "tik2/a3.mp4",
    "tik2/a4.mp4",
    "tik2/a5.mp4",
    "tik2/a6.mp4",
    "tik2/a7.mp4",
    "tik2/a8.mp4",
    "tik2/a9.mp4",
    "tik2/a0.mp4",
    "tik2/z1.mp4",
    "tik2/z2.mp4",
    "tik2/z3.mp4",
    "tik2/z4.mp4",
    "tik2/z5.mp4",
    "tik2/z6.mp4",
    "tik2/z7.mp4",
    "tik2/z8.mp4",
    "tik2/z9.mp4",
    "tik2/z0.mp4",
 
    # Add more video files as needed
]

output_file_path = "name.mp4"

concatenate_videos(video_files, output_file_path)