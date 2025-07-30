
from moviepy.editor import ImageClip

def create_video_from_image(image_path, output_path, duration=5):
    clip = ImageClip(image_path).set_duration(duration)
    clip.write_videofile(output_path, fps=24)
