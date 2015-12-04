# RasPi-Rattle
RASpberry PI - RemoTe Time LapsE: find wifi, plug in power, take pictures, make video, upload to the web

Copyright (c) 2015 Pyre Flos, Provided to the public under The MIT License

Recommended Hardware:

    Raspberry Pi (A+)
    Raspberry Pi Camera
    PaPirus (ePaper, Buttons, RTC)
    EdiMax (Wifi)
    Apple iPad charger (5V @ 2.1A)

Dependencies:

    Dropbox-Uploader by andreafabrizi  (https://github.com/andreafabrizi/Dropbox-Uploader)

---------------------------------------------------------------------------------------------
| 1 | Scaled 2k | 2592x1944 -> crop to 2592x1367 (top/bottom lost) -> scale to 2048x1080 |
| 2 | Cropped 2k | 2592x1944 -> crop to 2048x1080 (centered - outside lost) |
| 3 | Scaled 1080p | 2592x1944 -> crop to 2592x---- (top/bottom lost) -> scale to 1920x1080 |
| 4 | Cropped 1080p | 2592x1944 -> crop to 1920x1080 (centered - outside lost) |
| 5 | Scaled 720p | 2592x1944 -> crop to 2592x----(top/bottom lost) -> scale to 1280x720 |
| 6 | Cropped 720p | 2592x1944 -> crop to 1280x720 (centered - outside lost) |
---------------------------------------------------------------------------------

if custom_width <= 0, set custom_width = 10
else if custom_width >= 2593, set custom_width = 2592
else custom_width = 648


avconv -y -r 30 -i *.jpg -r 30 -vcodec libx264 -q:v 15 -vf crop=ow=2592:oh=1367,scale=ow=2048:oh=1080 timelapse-2015-12-03.mp4

avconv -y -r 30 -i img_%4d-%2d-%2d_%2d-%2d-%2d.jpg -r 30 -vcodec libx264 -q:v 15 -vf crop=ow=2592:oh=1367,scale=ow=2048:oh=1080 timelapse-2015-12-03.mp4

