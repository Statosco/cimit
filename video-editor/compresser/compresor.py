import os
import subprocess

def cut_video(input_file, output_folder, chunk_duration):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    command = [
        "ffmpeg",
        "-i", input_file,
        "-c", "copy",
        "-map", "0",
        "-f", "segment",
        "-segment_time", str(chunk_duration),
        "-reset_timestamps", "1",
        os.path.join(output_folder, "output%03d.mp4")
    ]
    subprocess.run(command)

def cut_multiple_videos(input_folder, output_folder, chunk_duration):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Get a list of all video files in the input folder
    video_files = [f for f in os.listdir(input_folder) if f.endswith((".mp4", ".mkv", ".avi", ".mov"))]

    # Cut each video file
    for video_file in video_files:
        input_path = os.path.join(input_folder, video_file)
        output_subfolder = os.path.join(output_folder, video_file.split(".")[0])
        cut_video(input_path, output_subfolder, chunk_duration)

if __name__ == "__main__":
    input_folder_path = "input_videos"
    output_folder_path = "output_cut_videos"
    chunk_duration_seconds = 10

    cut_multiple_videos(input_folder_path, output_folder_path, chunk_duration_seconds)
