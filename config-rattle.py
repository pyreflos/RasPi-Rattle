##
##  User configuration file - edit these settings to suit your own project
##

file_path_i = '/home/pi/RasPi-Rattle/images/'  ##  path to save images
file_path_v = '/home/pi/RasPi-Rattle/video/'  ##  path to save video
file_prefix = 'img_'  ##  prefix before filename.jpg, if needed - e.g. a project number
use_timestamp = True  ##  True = timestamp in filename, False = incremental numbering
image_time = 5  ## time delay between images (in minutes), recommended range: 2 to 99

##  Image Set: This takes a still image at full size, crops it, scales it, and saves it. See readme.md for more info.
##  0 = Custom Size - see below
##  1 = Full --> 2592x1944 px (~2.4mb / image)
##  2 = 2k --> 2048x1080 px (~0.0mb / image)
##  3 = 1080p --> 1920x1080 px (~0.0mb / image)
##  4 = 720p --> 1280x720 (~0.0mb / image)
image_set = 1
custom_width = 648  ##  Custom sizes crop the image only
custom_height = 486


video_framerate = 30  ##  Framerates restricted between 1 & 60; Recommended values: 24 or 30


