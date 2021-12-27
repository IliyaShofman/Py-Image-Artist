import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw  
import random
import numpy as np       

w = 750
h = 500
color = (0,0,125,125)
new_image = PIL.Image.new('RGBA', (w, h), color)
new_image_canvas = PIL.ImageDraw.Draw(new_image)

def triangle():
    for each in range(0, 25):
        x = random.randint(10,w-10)
        y = random.randint(10,h-10)
        s = random.randint(1, w/4)
        o = random.uniform(0, 2* np.pi)
        a = random.randint(0,255)
        new_image_canvas.polygon([(x,y), (x+s*np.cos(o), y+s*np.sin(o)), 
                          (x+s*(np.cos(o)+np.cos(o+2*np.pi/3)), 
                           y+s*(np.sin(o)+np.sin(o+2*np.pi/3)))], 
                           fill = (0,100,0,a) )
    

def white_to_transparent(img):
    """When pasting PIL Image with transparency onto another, 
       the transaprent colorless pixels turn white by default"""
    img = img.convert("RGBA")
    datas = img.getdata()

    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255 or item[3] == 0:
            newData.append(color) 
        else:
            newData.append(item)

    img.putdata(newData)
    return img

def generator(image_directory, n):
    i = 0
    while i < n:
        o = random.randint(-90, 90)
        s = random.uniform(0.1*min(w, h), 0.5*min(w, h)) 
        factor = s/max(w,h)
        #print factor
        x = random.randint(0.1*w,0.9*w)
        y = random.randint(0.1*h, 0.9*h)
        
        shape = PIL.Image.open(image_directory)
        shape.convert('RGBA')
        shape = shape.resize((int(factor*shape.width), int(factor*shape.height)))          
        #shape = shape.resize((int(0.1*shape.width), int(.1*shape.height)))
        shape = shape.rotate(o, expand=True)
        
        shadow = new_image.crop((x,y, x+ shape.width, y+shape.height))
        #print shadow.getextrema()
        data = list(shadow.getdata())
        
        paste = True
        for item in data:
            if item != color: #paste if and only if all pixels = color
                paste = False
        if paste:
            shape = white_to_transparent(shape)
            new_image.paste(shape, (x,y), mask=None)
            i +=1  
    return new_image

Photos = ("C:\\Users\\shofm\\Downloads\\pineapple2.png", 
          "C:\\Users\\shofm\\Downloads\\sunglass3.png", 
          "C:\\Users\\shofm\\Downloads\\martini.png"     )

def mono_gen(image1, n):
    generator(image1, n)
    return new_image

def multi_gen(image_tuple, n):
    for each in range (0, n):
        for image in image_tuple:
            generator(image, 1)
    return new_image
    

#COLOR SMART ALGORITHM DEVELOPMENT
#find average pixel value of all non-white, non-black, and non-transparent pixels
def differentiator(image_source_tuple):
    #convert input tuple of directories to array of PIL Images in RGBA called "photos"
    photos = []
    for directory in image_source_tuple:
        photo = PIL.Image.open(directory)
        photo = photo.convert("RGBA")
        photos += [photo]
    
    #generates a nested array with all colored pixels for each image
    black = (0, 0, 0)
    white = (255, 255, 255)
    photo_data = []
    photo_data_extract = []
    
    for image in photos:
        i = photos.index(image)
        photo_data += [[]]
        photo_data[i] = list(image.getdata())
        useful_pixels = []
        for pixel in photo_data[i]:
            if pixel[0:3] != white and pixel[0:3] != black and pixel[3] != 0:
                useful_pixels+= pixel
        photo_data_extract += [[useful_pixels]]
    
    #generates nested array of calculated averages of useful pixel for all images
    photo_calc = [] 
    for image_data in photo_data_extract:
        r, g, b, = 0, 0, 0
        for data_pixel in image_data:
            r = (r + data_pixel[0])/2
            g = (g + data_pixel[1])/2
            b = (b + data_pixel[2])/2
        photo_calc += [[r, g, b]]
    
    return photo_calc
        

#compare average pixel values with other pictures and calculate complementary color
    
def save(name):
    name += ".png" 
    directory = os.getcwd()
    new_image_path = os.path.join(directory, name)
    new_image.save(new_image_path)



























