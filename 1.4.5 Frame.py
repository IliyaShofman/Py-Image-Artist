import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        #test if file is image by checking extension
        #if entry.lower().endswith(('.png', '.jpg', '.jpeg')) == True 
        #if os.splitext(absolute_filename) in ('.png', '.jpg', '.jpeg')
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list


def frame_one_image(original, color, frame): #
    ''' Returns PIL.Image object with the original picture framed.
        original: PIL.Image object of picture; 
        color:3-tuple (r,g,b) color; 
        frame: integer thickness of frame'''
    width, height = original.size
    h = height+ 2*frame #new width and height
    w = width + 2*frame
    new_image = PIL.Image.new('RGBA', (w, h), (0,0,0,0))
    new_image_canvas = PIL.ImageDraw.Draw(new_image)
    
    new_image_canvas.polygon([(0,0), (w,0), (w,h), (0,h), (0,frame), 
                              (frame, frame), (frame, h-frame),
                              (w-frame, h-frame), (w-frame, frame),
                              (0,frame), (0,0)], fill=color)
    
    new_image.paste(original, (frame, frame), mask=None)
    return new_image

def alter_all_images(directory=None): #
    '''calls frame_all_images(), saves modified files to new folder'''
    if directory == None:
        directory = os.getcwd()
    
    new_directory = os.path.join(directory, 'framed')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass 
     
    image_list, path_list = get_images(directory)
    
    for n in range(len(image_list)):
        original = image_list[n]
        new = frame_one_image(original, (127,127,127,1), 10)
        new_image_path = os.path.join(new_directory, path_list[n])
        new.save(new_image_path)
        

































