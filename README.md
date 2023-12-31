# lama_vidr | Lama video object remover

lama_vidr is a code written using lama to remove unwanted objects or watermarks in a video. (Super slow)

## Samples

<div align="center">
  <img src="sample_videos/Samples for github/sample1.gif" width="256" height="256"/>
  <img src="sample_videos/Samples for github/sample1_fixed.gif" width="256" height="256"/>
</div>

<div align="center">
  <img src="sample_videos/Samples for github/sample2.gif" width="256" height="256"/>
  <img src="masks/mask14_768x768.png" width="256" height="256"/>
  <img src="sample_videos/Samples for github/sample2_fixed.gif" width="256" height="256"/>
</div>

## Installation

To install lama_vidr, you can follow these steps:
- Create a directory on your local machine.
- Open the command prompt and go to the directory you just created.
- Run the following commands to clone the lama_vidr repository: 
```
git clone https://github.com/SoAp9035/lama_vidr.git
cd lama_vidr
pip install -r requirements.txt
```

## Usage

To use lama_vidr, follow these steps:
- Open the lama_vidr.py file.
- Define the path of the video and the mask.
- Run the script.

## Source

- ffmpy: [https://github.com/Ch00k/ffmpy](https://github.com/Ch00k/ffmpy)
- simple-lama-inpainting: [https://github.com/enesmsahin/simple-lama-inpainting](https://github.com/enesmsahin/simple-lama-inpainting)
