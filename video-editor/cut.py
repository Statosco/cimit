from moviepy.video.io.VideoFileClip import VideoFileClip
import os

def cut_video(input_file, output_folder, chunk_duration):
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    clip = VideoFileClip(input_file)

    # Calculate the total duration of the video
    total_duration = clip.duration

    # Calculate the number of chunks
    num_chunks = int(total_duration / chunk_duration)

    # Cut the video into chunks
    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = (i + 1) * chunk_duration

        # Ensure the end time does not exceed the total duration
        if end_time > total_duration:
            end_time = total_duration

        # Extract the subclip
        subclip = clip.subclip(start_time, end_time)

        # Save the subclip with explicitly set fps
        output_path = os.path.join(output_folder, f"output_chunk_{i + 1}.mp4")
        subclip.write_videofile(output_path, codec="libx264", audio_codec="aac", fps=clip.fps)

if __name__ == "__main__":
    input_file_path = "SIDEMEN ABANDONED IN IRELAND CHALLENGE.mp4"
    output_folder_path = "sidemen"
    chunk_duration_seconds = 60

    cut_video(input_file_path, output_folder_path, chunk_duration_seconds)
