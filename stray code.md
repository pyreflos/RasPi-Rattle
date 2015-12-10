####Stray code that needs to be moved...


if custom_width <= 0, set custom_width = 10

else if custom_width >= 2593, set custom_width = 2592

else custom_width = 648




avconv -y -r 30 -i *.jpg -r 30 -vcodec libx264 -q:v 15 -vf crop=ow=2592:oh=1367,scale=ow=2048:oh=1080 timelapse-2015-12-03.mp4

 (DOES NOT WORK)
