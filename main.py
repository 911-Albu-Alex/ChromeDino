from PIL import ImageGrab, ImageOps
import numpy
import keyboard
import time

previous_value = 0
ticks = 0
difficulty_modifier = 1
x1Coordinate, y1Coordinate, x1Offset, y1Offset = 510, 292, 1, 1
x2Coordinate, y2Coordinate, x2Offset, y2Offset = 677, 266, 1, 1
x3Coordinate, y3Coordinate, x3Offset, y3Offset = 490, 292, 1, 1
while True:
    if keyboard.is_pressed('q'):
        print("Stopping game!")
        break
    box1 = (x1Coordinate, y1Coordinate, x1Coordinate + x1Offset, y1Coordinate + y1Offset)
    box3 = (x3Coordinate, y3Coordinate, x3Coordinate + x3Offset, y3Coordinate + y3Offset)
    image = ImageGrab.grab(box1)
    _image = ImageGrab.grab(box3)
    grayImage = ImageOps.grayscale(image)
    array = numpy.array(grayImage.getcolors())
    value = array.sum()
    grayImage = ImageOps.grayscale(_image)
    array = numpy.array(grayImage.getcolors())
    value_ = array.sum()
    if ((value != previous_value and value_ == previous_value) or (value == previous_value and value_ != previous_value)) and previous_value != 0:
        keyboard.press('space')
    previous_value = value
    box2 = (x2Coordinate, y2Coordinate, x2Coordinate+x2Offset, y2Coordinate+y2Offset)
    image = ImageGrab.grab(box2)
    grayImage = ImageOps.grayscale(image)
    array = numpy.array(grayImage.getcolors())
    value = array.sum()
    # if value == 84:
    #     time.sleep(2)
    #     keyboard.press('space')
    if ticks == 100:
        difficulty_modifier *= 1.01
        print(difficulty_modifier)
        x1Coordinate *= difficulty_modifier
        x1Coordinate = numpy.ceil(x1Coordinate)
        ticks = 0
    else:
        ticks += 1
