# Py-Image-Artist
A cute 12th-grade project in python. I'm using PIL (Python Image Library) to create a collage, which consists of non-overlapping randomly -positioned, -rotated, and -resized images. The huge html file is the debugging log that my IDLE produced while I was working on the file. 

<img src="https://github.com/IliyaShofman/Py-Image-Artist/blob/main/beach%20party.png" width=750px />

## How to run:
Beach Party Instructions
```
>>> from test import *
>>> photos = ('C:\\...\\photos\\pineapple.png', 'C:\\...\\photos\\sunglass.png', 'C:\\...\\photos\\martini.png')
>>> multi_gen(photos, 4) 
#photos = tuple w/ filenames, 4 = number of repetitions of each picture in photos
```
You could change the background color in the ```test.py``` file, and replace the images in the ```\photos``` directory.
