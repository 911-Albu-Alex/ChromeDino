import time

from PIL import ImageGrab, ImageOps
import numpy
import keyboard
import win32api

initial_state = 0
ticks = 0
difficulty_modifier = 1
x1Coordinate, y1Coordinate, x1Offset, y1Offset = 500, 292, 20, 1
x3Coordinate, y3Coordinate, x3Offset, y3Offset = 480, 292, 20, 1
birdXCoordinate, birdYCoordinate, xOffset, yOffset = 460, 261, 20, 1
farX, farY, farXOffset, farYOffset = 520, 292, 20, 1


def turn_box_into_array_sum(box):
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    array = numpy.array(grayImage.getcolors())
    value = array.sum()
    return value


def multiply_coordinate(coordinate, modifier):
    coordinate *= modifier
    coordinate = numpy.ceil(coordinate)
    return coordinate


def press_space():
    keyboard.press('space')
    keyboard.press('space')


def reset_values():
    return 0, 0, 1, 500, 480, 520


while True:
    if keyboard.is_pressed('q'):
        print("Stopping game!")
        break
    if win32api.GetKeyState(0x01) < 0:
        print("Game restart!")
        initial_state, ticks, difficulty_modifier, x1Coordinate, x3Coordinate, farX = reset_values()
    box1 = (x1Coordinate, y1Coordinate, x1Coordinate + x1Offset, y1Coordinate + y1Offset)
    box3 = (x3Coordinate, y3Coordinate, x3Coordinate + x3Offset, y3Coordinate + y3Offset)
    boxFar = (farX, farY, farX + xOffset, farY + yOffset)
    boxBird = (birdXCoordinate, birdYCoordinate, birdXCoordinate + xOffset, birdYCoordinate + yOffset)
    value = turn_box_into_array_sum(box1)
    value_ = turn_box_into_array_sum(box3)
    valueBird = turn_box_into_array_sum(boxBird)
    valueFar = turn_box_into_array_sum(boxFar)
    if initial_state != 0:
        if valueFar != initial_state:
            press_space()
        if value != initial_state:
            press_space()
        if value_ != initial_state:
            press_space()
        if valueBird != initial_state:
            keyboard.press('down')
    else:
        initial_state = value
    if ticks == 100:
        difficulty_modifier *= 1.03
        x1Coordinate = multiply_coordinate(x1Coordinate, difficulty_modifier)
        x3Coordinate = multiply_coordinate(x3Coordinate, difficulty_modifier)
        farX = multiply_coordinate(farX, difficulty_modifier)
        ticks = 0
    else:
        ticks += 1
