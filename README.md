# image_serial_transfer
To serially transmit and receive the image using Python 

Requirements:

Python 2.7
Pyserial

The code for Protocol Wrapper was taken from [http://eli.thegreenplace.net], but is adapted for image data.
Since image have high amount of data, it can't be sent in one go, instead sent in several frames.
Changed format from Header/Data/Footer to Header/FrameID/Data/Footer.

It will read for FrameID after detecting Header and place the corresponding data into that index of list.

