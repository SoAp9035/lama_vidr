@echo off

set /p video_path="Video path: "
set /p mask_path="Mask path: "

python lama_vidr.py "%video_path%" "%mask_path%"