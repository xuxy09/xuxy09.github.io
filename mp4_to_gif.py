from moviepy.editor import VideoFileClip

def convert_mp4_to_gif(input_file, output_file):
    clip = VideoFileClip(input_file)
    clip = clip.resize(height=360)
    clip.write_gif(output_file,)

# Specify the input MP4 file path and output GIF file path
name = "images/cvpr22vfit_after.mp4"
input_file_path = name
output_file_path = name[:-4] + ".gif"

# Convert the MP4 to GIF
convert_mp4_to_gif(input_file_path, output_file_path)