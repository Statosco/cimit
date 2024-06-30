#you need to install moviepy to be avvle to run the script

from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.compositing.concatenate import concatenate_videoclips

def remove_frames(input_file, output_file, interval_seconds, removal_seconds):
    clip = VideoFileClip(input_file)
    clips = []

    for i in range(0, int(clip.duration), interval_seconds):
        start_time = i
        end_time = i + interval_seconds - removal_seconds
        subclip = clip.subclip(start_time, end_time)
        clips.append(subclip)

    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

# Example usage:
input_file_path = "ep11.mp4"
output_file_path = "output11.mp4"
interval_seconds = 5
removal_seconds = 2

remove_frames(input_file_path, output_file_path, interval_seconds, removal_seconds)






