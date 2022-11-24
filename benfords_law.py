### Name: Jordan Orvik
### Class: CSC 110
### Description: Determines whether the numbers in a CSV
### data sheet follow the math phenomenon known as Benford's Law.
### A data table showing the percent that certain numbers appear first
### is printed to show proof of the law.
### A graphical representation can also be shown instead by user request.

### IMPORTANT: Graphics module required for the gui mode, download here:
### https://bddicken.github.io/cs110fall2022website/files/graphics.py
### If you are planning to use text mode only, you do not have to download.

# Imports the required modules.
from graphics import graphics
import random


def get_numbers(file) :
    '''
    This function opens a CSV data sheet, reads the lines,
    separates the columns (by commas), then checks for valid numbers.
    This check is done by making sure the first and last characters of
    each data entry are numeric, and that no number begins with zero.
    If these conditions pass, that particular number is added to a new list
    called numbers. This new list is then returned.

    file = the name of a CSV data file (with .csv).
    '''
    # Opens and reads the lines of the file.
    lists = open(file, "r")
    lines = lists.readlines()
    numbers = []
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip("\n")

    # Filters out anything that is not a non-0 number.
    # Loop for each row.
    for line in lines :
        separated = line.split(",")

        # Nested loop to check every column in a row.
        for j in range(0, len(separated)) :
            second = separated[j]
            end_char = len(separated[j]) - 1
            if second[0].isnumeric() and second[end_char].isnumeric() :
                if float(second[0]) != 0 :
                    numbers.append(second)
    return numbers

def counting(numbers, digits) :
    '''
    This function counts the leading digits of each of the numbers,
    and adds them to a dictionary. A loop is checked to go through 
    each leading digit, and a nested loop is used to determine
    what digit that first number is (using a list of all digits).
    Then 1 is added to the dictionary entry for that digit.
    The dictionary is returned.

    numbers = the list of all non-zero numbers in the data sheet.
    digits = a list with all digits as elements (1-9).
    '''
    count = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for number in numbers :
        for digit in digits :
            if int(number[0]) == digit :
                count[digit] += 1
    return count
 
def calc_percent(numbers, count, digits) :
    '''
    This function calculates the percentage that each digit
    was the leading digit of the numbers in the data set.
    These percentages are saved to a new dictionary entry for that digit,
    which is then returned after all digit percents have been calculated.

    numbers = the list of non-zero numbers in the data sheet.
    count = the dictionary with the number of times each number
    was a leading digit.
    digits = a list with all digits as elements (1-9).
    '''
    total_nums = len(numbers)
    # New dictionary that the percents will be saved to.
    percents = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
    for digit in digits :
        percents[digit] = int((count[digit] / total_nums) * 100)
    return percents

def is_legal(percents, digits) :
    '''
    This function checks to see (from the percentages), whether the
    data in the sheet follows Benford's Law.
    The percent is checked against a valid percentage of that digit 
    for the law (stored in a dictionary), and if any of the percentages
    fail to be in the proper valid range (-5% and +10%), then the data
    does not follow Benford's Law!
    A boolean of whether the data follows the law is returned.

    percents = the dictionary with the calculated leading digit 
    percentages for each digit.
    digits = a list with all digits as elements (1-9).
    '''
    law = True
    # All of the valid percentages for Benford's Law.
    valid = {1: 30, 2: 17, 3: 12, 4: 9, 5: 7, 6: 6, 7: 5, 8: 5, 9: 4}

    for digit in digits :
        if not (valid[digit] - 5) <= percents[digit] <= (valid[digit] + 10) :
            law = False
    return law

def text_display(percents, law, digits) :
    '''
    This function prints out the breakdown of percentages
    of each leading digit in the data set (each # is 1 percent).
    It will also print whether the data follows 
    Benford's Law.

    percents = the dictionary with the calculated leading digit 
    percentages for each digit.
    law = the Boolean for whether the law is followed.
    digits = a list with all digits as elements (1-9).
    '''
    print(" ")
    for digit in digits :
        print(digit, "|", "#" * percents[digit])
    if law :
        print(" ")
        print("Follows Benford's Law")
    else :
        print(" ")
        print("Does not follow Benford's Law") 

def bar_colors(gui) :
    '''
    This function creates a random color for the graphical bars, 
    then returns it.
    
    gui = the current graphics canvas.
    '''
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    bar_color = gui.get_color_string(red, green, blue)
    return bar_color

def gui_display(gui, percents, law, digits) :
    '''
    This function creates a graphical representation
    of the percentages of leading digits with a bar graph. 
    The bar graph uses random colors, and at the bottom, 
    the result on if the data follows the law will be displayed.

    gui = the current graphical canvas. 
    percents = the dictionary with the calculated leading digit 
    percentages for each digit.
    law = the Boolean for whether the law is followed.
    digits = a list with all digits as elements (1-9).
    '''
    # Background
    gui.rectangle(0, 0, 650, 680, "aqua")
    gui.rectangle(50, 50, 540, 540, "black")
    gui.rectangle(60, 60, 520, 520, "aqua")
    gui.text(50, 10, "Benford's Law Analysis Results:", "blue", 20)
    list_y = 65

    # Drawing the bar graph.
    for digit in digits :
        gui.text(20, list_y+5, str(digit), "red", 20)
        bar_color = bar_colors(gui)
        bar_x = 60
        for i in range(0, percents[digit]) :
            gui.rectangle(bar_x, list_y-3, 18, 51, "black")
            gui.rectangle(bar_x, list_y, 15, 45, bar_color)
            bar_x += 15
        list_y += 55
    # Puts the text on the screen whether the data follows the law,
    # with a little graphic as well.
    if law :
        gui.ellipse(35, 630, 30, 30, "dark green")
        gui.text(25, 621, "OK", "white", 12)
        gui.text(70, 615, "Follows Benford's Law", "dark green", 20)
    else :
        gui.ellipse(35, 630, 30, 30, "red")
        gui.text(28, 618, "X", "white", 18)
        gui.text(70, 615, "Does not follow Benford's Law", "red", 20)
    gui.draw()


def main() :
    # Asks for file name and mode.
    # DO NOT type mode as gui if graphics module not installed!
    file = input("Data file name: \n")
    mode = input("Mode: \n")

    # Retrieves the file, gets numbers, and calls calculation functions.
    numbers = get_numbers(file)
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    count = counting(numbers, digits)
    percents = calc_percent(numbers, count, digits)

    # Does the data follow the law?
    law = is_legal(percents, digits)

    # Displays the result.
    if mode == "text" :
        text_display(percents, law, digits)
    elif mode == "gui" :
        # Canvas is created only when gui mode is selected,
        # to avoid breaking compatibility with a non-graphics
        # interpreter.
        gui = graphics(650, 680, "Benford's Law")
        gui_display(gui, percents, law, digits)

main()
    
    

