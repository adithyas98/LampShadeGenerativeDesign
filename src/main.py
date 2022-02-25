#!/usr/bin/env python3

import sys
from LampGen import LampGen as Lamp

def main():
    '''
    Main method that will run all of our code
    '''
    #Parse arguments
    filename = None
    if len(sys.argv) == 1:
        print("Box class will be run normally")
        lamp = Lamp()
    elif sys.argv[1] == '-h':
        print("You have three options for flags:\n")
        print("-o {FileName.csv} will create an editable csv file with ")
        print("the inputs needed to make your box. You can add your specifications in the ")
        print("Input column of the csv\n")
        print("-i {FileName.csv} will import your specifications from the file specified\n")
        print("Run the file with no arguments to have the script manually ask you for each input")
        quit()
    elif sys.argv[1] == '-o':
        lamp  = Lamp(fileInput=sys.argv[2],questionOut=True)
    elif sys.argv[1] == '-i':
        print("Data will be imported from the file")
        lamp = Lamp(fileInput=sys.argv[2],questionOut=False)
        filename = sys.argv[2].split('/')[1].split('.')[0]
    else:
        print("Unrecognized input")
        print("Try -h for help")
        quit()
    #Generate the box now
    #we want to just use the name of the file if the user inputted one
    if filename is None:
        filename = input("What you like to name the file? Just give us the name, we will handle the rest!")
    lamp.exportLampShade("output/{}.stl".format(filename))
    








if __name__ == '__main__':
    main()
