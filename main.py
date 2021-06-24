import time

from PIL import ImageGrab, ImageOps
import numpy
import keyboard
import win32api

initial_state = 0
initial_state_down = 0
ticks = 0
difficulty_modifier = 1
x1Coordinate, y1Coordinate, x1Offset, y1Offset = 530, 290, 10, 1
x3Coordinate, y3Coordinate, x3Offset, y3Offset = 510, 290, 10, 1
birdXCoordinate, birdYCoordinate, xOffset, yOffset = 460, 261, 10, 1
farX, farY, farXOffset, farYOffset = 555, 290, 10, 1
isdownX, isdownY = 394, 294


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


def reset_values():
    return 0, 0, 1, 530, 510


while True:
    if keyboard.is_pressed('q'):
        print("Stopping game!")
        break
    if win32api.GetKeyState(0x01) < 0:
        print("Game restart!")
        initial_state, ticks, difficulty_modifier, x1Coordinate, x3Coordinate = reset_values()
    box1 = (x1Coordinate, y1Coordinate, x1Coordinate + x1Offset, y1Coordinate + y1Offset)
    box3 = (x3Coordinate, y3Coordinate, x3Coordinate + x3Offset, y3Coordinate + y3Offset)
    boxBird = (birdXCoordinate, birdYCoordinate, birdXCoordinate + xOffset, birdYCoordinate + yOffset)
    boxFar = (farX, farY, farX + farXOffset, farY + farYOffset)
    value = turn_box_into_array_sum(box1)
    value_ = turn_box_into_array_sum(box3)
    valueBird = turn_box_into_array_sum(boxBird)
    valueFar = turn_box_into_array_sum(boxFar)
    boxDown = (isdownX, isdownY, xOffset, yOffset)
    valueDown = turn_box_into_array_sum(boxDown)
    # if initial_state != 0:
    #     if valueFar != initial_state:
    #         if value != initial_state:
    #             time.sleep(0.01)
    #             keyboard.press('space')
    #         elif value_ != initial_state:
    #             time.sleep(0.01)
    #             keyboard.press('space')
    #     else:
    #         if value_ != initial_state:
    #             time.sleep(0.01)
    #             keyboard.press('space')
    #         elif value != initial_state:
    #             time.sleep(0.01)
    #             keyboard.press('space')
    #     if valueBird != initial_state:
    #         keyboard.press('down')
    # else:
    #     initial_state = value
    if initial_state != 0 and valueDown == initial_state_down:
        if valueFar != initial_state:
            time.sleep(0.01)
            keyboard.press('space')
        elif value_ != initial_state or value != initial_state:
            time.sleep(0.01)
            keyboard.press('space')
        if valueBird != initial_state:
            keyboard.press('down')
    else:
        initial_state = value
        initial_state_down = valueDown
    if ticks == 100:
        difficulty_modifier *= 1.01
        x1Coordinate = multiply_coordinate(x1Coordinate, difficulty_modifier)
        x3Coordinate = multiply_coordinate(x3Coordinate, difficulty_modifier)
        ticks = 0
    else:
        ticks += 1
