"""
Author: Łukasz Wróbel
Date: 01/01/2019
About: Function that allows to save your body dimensions progress
"""

#date module (used to save the file name as a date)
from datetime import date
#json
import json

#filename has name as a date
filename = str(date.today())

#load data function
def load_data_dimensions():
    print("Hello in Body Dimensions app!")
    print("This program allow you to save your'e body dimensions in file.")

    try:
        with open(filename) as f_object:
            dimensions = json.load(f_object)

    #if FileNotFoundError -> write_data_dimensions function load
    except FileNotFoundError:
        write_data_dimensions()

    #if the file with current date exists -> iteration of the file content
    else:
        print(f"\nYour body dimensions of {date.today()}:\n")
        for key, value in dimensions.items():
            print(f"{key} : {value}")


#write data function
def write_data_dimensions():
    print("We will now save the new dimensions to the file")
    #open file with write
    with open(filename, 'w') as f_obj:
        #new dictionary for saving object's
        body_dimensions = {}

        #names of objects with input() function
        weight = input("Weight: ")
        waist = input("Waist: ")
        chest = input("Chest: ")
        neck = input("Neck: ")
        huckle = input("Huckle: ")
        calf = input("Calf: ")
        thigh = input("Thigh: ")
        right_bicep = input("Right Bicep: ")
        left_bicep = input("Left Bicep: ")
        right_forearm = input("Right Forearm: ")
        left_forearm = input("Left Forearm: ")

        #saving object's to the dict
        body_dimensions['weight'] = weight
        body_dimensions['waist'] = waist
        body_dimensions['neck'] = neck
        body_dimensions['calf'] = calf
        body_dimensions['thigh'] = thigh
        body_dimensions['huckle'] = huckle
        body_dimensions['chest'] = chest
        body_dimensions['right_bicep'] = right_bicep
        body_dimensions['left_bicep'] = left_bicep
        body_dimensions['right_forearm'] = right_forearm
        body_dimensions['left_forearm'] = left_forearm

        #saving json file
        json.dump(body_dimensions, f_obj)



load_data_dimensions()


