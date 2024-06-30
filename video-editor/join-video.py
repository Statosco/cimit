from moviepy.editor import VideoFileClip, concatenate_videoclips

def concatenate_videos(video_list, output_file):
    clips = [VideoFileClip(video) for video in video_list]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec="libx264", audio_codec="aac")

# Example usage:
video_files = [
    "water\w1.mp4",
    "water\w2.mp4",
    "water\w3.mp4",
    "water\w4.mp4",
    "water\w4.mp4",
    "water\w6.mp4",
    "water\w7.mp4",
    "water\w8.mp4",
    "water\w9.mp4",
    "water\w10.mp4",
    "water\w11.mp4",
    "water\w12.mp4",
    "water\w13.mp4",
    "water\w14.mp4",
    "water\w15.mp4",
    "water\w16.mp4",
    "water\w17.mp4",
    "water\w18.mp4",
    "water\w19.mp4",
    "water\w20.mp4",
    "water\w21.mp4",
    "water\w22.mp4",
    "water\w23.mp4",
    "water\w24.mp4",
    "water\w25.mp4",
    "water\w26.mp4",
    "water\w27.mp4",
    "water\w28.mp4",
    "water\w29.mp4",
    "water\w30.mp4",
    "water\w31.mp4",
    "water\w32.mp4",
    "water\w33.mp4",
    "water\w34.mp4",
    "water\w36.mp4",
    "water\w37.mp4",
    "water\w38.mp4",
    "water\w39.mp4",
    "water\w40.mp4",
    "water\w41.mp4",
    "water\w42.mp4",
    "water\w43.mp4",
    "water\w44.mp4",
    "water\w45.mp4",
    "water\w46.mp4",
    "water\w47.mp4",
    "water\w48.mp4",
    "water\w49.mp4",
    "water\w50.mp4",
    "water\w51.mp4",
    "water\w52.mp4",
    "water\w53.mp4",
    "water\w54.mp4",
    "water\w55.mp4",
    "water\w56.mp4",
    "water\w57.mp4",
    "water\w58.mp4",
    "water\w59.mp4",
    "water\w60.mp4",
    "water\w61.mp4",
    "water\w62.mp4",
    "water\w63.mp4",
    "water\w64.mp4",
    "water\w65.mp4",
    "water\w66.mp4",
    "water\w67.mp4",
  
    # Add more video files as needed
]

output_file_path = "wate_chalenge.mp4"

concatenate_videos(video_files, output_file_path)