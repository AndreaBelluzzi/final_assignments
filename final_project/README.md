# Video Generator for fMRI data #

Have you ever wanted to create cool videos to show off your fMRI data? This is the place for you!

Taking advantage of the possibility of running python scripts on MRIcroGL, I created 3 simple functions to generate 3D render animations. Each step of the animation is saved locally as a screenshot (bitmap format). The function 'scree2video' will merge all the images to generate a short video.

**prerequisites**

MRIcroGL - https://github.com/rordenlab/MRIcroGL
 general tutorial - https://www.nitrc.org/plugins/mwiki/index.php/mricrogl:MainPage


## Script ##

**MRIcroGL animation**
- animation1.py
- animation2.py
Contains the 3 functions: animation, pause, clipping; with examples of animations that can be created

**Generate video from screenshot**
- screen2video.ipynb
Upload screenshots and generate a video with the desired format, codec, resolution and framerate


__________________________________
For a longer explanation, see:
https://drive.google.com/drive/folders/1cVgVRRR7wg-gUYVBV367WklFXm3uaaI6?usp=drive_link
