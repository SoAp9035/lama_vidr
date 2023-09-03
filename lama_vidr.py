import os
import subprocess
import cv2
import random
import string
from ffmpy import FFmpeg

# Input and output values (INPUT YOUR VIDEO AND MASK)
current_directory = os.path.dirname(os.path.abspath(__file__))
video_path = r"YOUR_VIDEO"
frames_directory = os.path.join(current_directory, "frames")
output_frames_directory = os.path.join(current_directory, "output_frames")
mask_path = r"YOUR_MASK_IMG"
output_video_path = os.path.join(current_directory, f"output_videos\\video_{''.join(random.choices(string.ascii_lowercase, k=3))}.mp4")

# Calculate video framerate
cap = cv2.VideoCapture(video_path)  # Create VideoCapture object

frame_rate = cap.get(cv2.CAP_PROP_FPS)  # Get the framerate

print("frame rate:", frame_rate)

cap.release()  # Release the VideoCapture object

# !!! IF YOUR RESULT VIDEO DURATION IS NOT TRUE. DELETE '#' AND CHANGE IT TO YOUR VIDEO FRAME RATE !!! 
#frame_rate = 30

# DELETE OLD PHOTOS
def foto_del(dizin):
    dosyalar = os.listdir(dizin)
    
    for dosya in dosyalar:
        if dosya.endswith(".png"):
            dosya_yolu = os.path.join(dizin, dosya)
            os.remove(dosya_yolu)

# Call the function to delete the photos
foto_del(frames_directory)
foto_del(output_frames_directory)

# Split the video into frames
output_pattern = os.path.join(frames_directory, 'frame%05d.png')

ff = FFmpeg(
    inputs={video_path: None},
    outputs={output_pattern: None}
)

ff.run()

input_frames = os.listdir(frames_directory)
for frame in input_frames:
    subprocess.call('simple_lama "{}" "{}" "{}"'.format(os.path.join(frames_directory, frame),
                                                  mask_path,
                                                  os.path.join(output_frames_directory, frame)))

# Merge processed frames into a single video (CHANGE THIS IF YOUR VIDEO IS NOT WORKING)
input_pattern = os.path.join(output_frames_directory, 'frame%05d.png')

ff = FFmpeg(
    inputs={input_pattern: '-framerate {}'.format(frame_rate)},
    outputs={output_video_path: '-pix_fmt yuv420p'}
)

ff.run()
