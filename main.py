from PIL import ImageGrab, ImageOps
import numpy
import keyboard
import time

previous_value = 0
start_time = time.time()
difficulty_modifier = 1
xCoordinate, yCoordinate, xOffset, yOffset = 510, 292, 1, 1
while True:
    if keyboard.is_pressed('q'):
        print("Stopping game!")
        break
    box1 = (xCoordinate, yCoordinate, xCoordinate+xOffset, yCoordinate+yOffset)
    image = ImageGrab.grab(box1)
    grayImage = ImageOps.grayscale(image)
    array = numpy.array(grayImage.getcolors())
    value = array.sum()
    print(value)
    if value != previous_value and previous_value != 0:
        keyboard.press('space')
        pass
    previous_value = value
    if numpy.floor(time.time() - start_time+1) % 3 == 0:
        difficulty_modifier *= 1.05
        xCoordinate *= difficulty_modifier
        xCoordinate = numpy.ceil(xCoordinate)
