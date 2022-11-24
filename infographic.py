### Name: Jordan Orvik
### Class: CSC 110
### Description: This program analyzes various properties of a text file
### such as the most used words, how many different words there are,
### how much of the words are punctuated or capitalized, and the percent
### of small, medium, and large words.
### The program then displays these properties in the form of text and
### bar graphs, all shown in a neat graphical window.

### IMPORTANT: The graphics module below is required! Download it here:
### https://bddicken.github.io/cs110fall2022website/files/graphics.py

from graphics import graphics

def get_words(file) :
    '''
    This function opens a text file selected
    by the user, and puts the lines of it into a list,
    removing new line characters.
    Words are then split apart in each line,
    and put into a new list. The list of words is then returned.

    file = a string with the name of a text file
    (including .txt)
    '''
    # Opens a file and reads the lines.
    plain_text = open(file, 'r')
    lines = plain_text.readlines()
    # Removes new line characters.
    for i in range(0, len(lines)):
        lines[i] = lines[i].strip("\n")
    word_list = []
    # Finds all the words in the file and adds them to a list.
    for line in lines :
        line_words = line.split()
        for line_word in line_words :
            word_list.append(line_word)
    return word_list

def count_words(word_list) :
    '''
    This function uses a dictionary to count how many 
    times each word appears in the text file.
    The first time a word appears, the word entry is added,
    and for every subsequent word appearance, 1 is added to the
    word count.
    This dictonary of the words and their counts is then returned.

    word_list = the list of all the words in the text file.
    '''
    word_counts = {}
    for word in word_list :
        # Adds new words to the dictionary.
        if word not in word_counts :
            word_counts[word] = 0
        word_counts[word] += 1
    return word_counts

def word_lengths(word_count) :
    '''
    This function sorts the words into small, medium, and
    large lengths. If-statements check each word across the lengths
    and add them to the appropriate separated dictionaries.
    Small words are 4 characters or less, mediums are 5 to 7 characters,
    and large words are 8 characters or more.
    The 3 dictionaries with words sorted into lengths are then
    returned.
    
    word_count = the dictionary with all unique words and their
    counts.
    '''
    small = {}
    medium = {}
    large = {}
    for word, count in word_count.items() :
        # Checks each word against the set s/m/l lengths.
        if len(word) <= 4 :
            small[word] = count
        elif 5 <= len(word) <= 7 :
            medium[word] = count
        else :
            large[word] = count
    return small, medium, large

def most_common_words(small, medium, large) :
    '''
    This function checks to see what the most common 
    small, medium, and large words actually are.
    These three words, once they are determined, are appended
    into a dictionary in that order (s, m, l), and that is then returned.
    
    small = the dictionary with all small words and their counts.
    medium = the dictionary with all medium words and their counts.
    large = the dictionary with all large words and their counts.
    '''
    most_used = {}
    # Finds the most common small word.
    small_common = "a"
    small_count = 0
    for key, value in small.items() :
        # Replaces the current "most common" if a word is more common.
        if value > small_count :
            small_common = key
            small_count = value
    # Appends the most common small words to a new dictionary.
    most_used[small_common] = small_count

    # The preceding comments apply, but for medium words.
    med_common = "a"
    med_count = 0
    for med_key, med_value in medium.items() :
        if med_value > med_count :
            med_common = med_key
            med_count = med_value
    most_used[med_common] = med_count

    # Same deal here, but with large words.
    large_common = "a"
    large_count = 0
    for large_key, large_value in large.items() :
        if large_value > large_count :
            large_common = large_key
            large_count = large_value
    most_used[large_common] = large_count
    return most_used

def unique_words(word_list) :
    '''
    This function finds the unique words from all the words 
    in the file, and adds them to a list that is returned.
    This might seem redundant because of count_words, 
    but the list format makes it easier to work with
    than a dictionary in the following functions.

    word_list = the list of all the words in the text file.
    '''
    unique = []
    for word in word_list :
        # Adds only not yet existing words to the list.
        if word not in unique :
            unique.append(word)
    return unique

def capital_words(unique) :
    '''
    This function determines the number of unique words in the text
    that have a beginning capital letter, using .isupper().
    This number is then returned.
    
    unique = the list of all unique words in the text.
    '''
    capitals = 0
    for word in unique :
        # If a word begins with a capital letter, 1 is added 
        # to the count of capital words.
        if word[0].isupper() :
            capitals += 1
    return capitals

def punctuation(unique) :
    '''
    This function determines the number of unique words in the text
    that have a period, exclamation mark, question mark, or comma at the end.
    This number is then returned.
    
    unique = the list of all unique words in the text.
    '''
    # Identifies the list to avoid hard-coding.
    punctuation_marks = [".", "!", "?", ","]
    mark_count = 0
    for word in unique :
        # Checks to see if the current word has any of the punctuation marks on the end of it.
        # If it does, 1 is added to the count of punctuated words.
        for mark in punctuation_marks :
            if word[len(word)-1] == mark :
                mark_count += 1
    return mark_count

def text_info(gui, file, unique, most_used) :
    '''
    This function draws the text header on the graphical screen. 
    The header contains the file name, the number of unique words,
    and the most used small, medium, and large words.
    
    gui = the current graphical canvas.
    file = the name of the text file that was opened.
    unique = the number of total unique words.
    most_used = the dictionary with the most used s/m/l words.
    '''
    # Prints the header.
    gui.text(50, 10, file, "red", 15)
    gui.text(50, 40, "Total Unique Words:" + " " + str(unique), "white", 12)
    gui.text(50, 70, "Most used words (s/m/l):", "white", 10)
    most_used_string = ""
    # Adds the most used words to a string, one at a time
    # from small to large.
    for key, value in most_used.items() :
        most_used_string += (str(key) + " (" + str(value) + "x) ")
    # Displays the string with the most used words of each size.
    gui.text(200, 70, most_used_string, "yellow", 10) 

def word_length_chart(gui, small_list, med_list, large_list, count) :
    '''
    This function creates the left-most bar in the graphic,
    showing the percentage of small, medium, and large words
    in the text file.

    gui = the current graphics canvas.
    small_list = the dictionary with all small words and their counts.
    med_list = the dictionary with all medium words and their counts.
    large_list = the dictionary with all large words and their counts.
    count = the number of unique words in the text file.
    '''
    # Sets the pixel heights for all of the graphs
    small_height = (400 / count) * len(small_list)
    med_height = (400 / count) * len(med_list)
    large_height = (400 / count) * len(large_list)

    # Displays the header text for this bar, plus the border "line" around the bar.
    gui.text(50, 110, "Word Lengths", "white", 15)
    gui.rectangle(45, 145, 160, 410, "black")
    starting_point = 150

    # Draws the "small word" bar segment.
    gui.rectangle(50, starting_point, 150, small_height, "green")
    gui.text(50, starting_point, "small words", "white", 10)
    # Increments the starting point so that the next segment starts where
    # the previous segment ends.
    starting_point += small_height

    # Draws the "medium word" bar segment.
    gui.line(50, starting_point, 200, starting_point, "black", 6)
    gui.rectangle(50, starting_point, 150, med_height, "red")
    gui.text(50, starting_point, "medium words", "white", 10)
    starting_point += med_height

    # Draws the "large word" bar segment.
    gui.line(50, starting_point, 200, starting_point, "black", 6)
    gui.rectangle(50, starting_point, 150, large_height, "purple")
    gui.text(50, starting_point, "large words", "white", 10)

def capitals_chart(gui, count, capitals) :
    '''
    This function creates the middle bar in the graphic,
    showing the percentage of words that are capitalized
    in the text file.

    gui = the current graphics canvas.
    count = the number of unique words in the text file.
    capitals = the number of capitalized words.
    '''
    # Calculates the percentages and pixel heights of the segments.
    cap_percent = (capitals / count)
    non_cap_percent = 1 - cap_percent
    cap_height = cap_percent * 400
    non_cap_height = non_cap_percent * 400

    # Displays the header and then the border rectangle.
    gui.text(250, 110, "Cap/Non-Cap", "white", 15)
    gui.rectangle(245, 145, 160, 410, "black")

    # Draws the "capitalized" bar segment.
    starting_point = 150
    gui.rectangle(250, starting_point, 150, cap_height, "green")
    gui.text(250, starting_point, "Capitalized", "white", 10)
    # Increments the starting point so that the next segment starts where
    # the previous segment ends.
    starting_point += cap_height

    # Draws the "non capitalized" bar segment.
    gui.line(250, starting_point, 400, starting_point, "black", 6)
    gui.rectangle(250, starting_point, 150, non_cap_height, "red")
    gui.text(250, starting_point, "Non Capitalized", "white", 10)

def punctuation_chart(gui, count, marks) :
    '''
    This function creates the right-most bar in the graphic
    showing the percentage of words that end with
    punctuation marks in the text file.

    gui = the current graphics canvas.
    count = the number of unique words in the text file.
    marks = the number of words with punctuation.
    '''
    # Calculates the percentages and pixel heights of the segments.
    punct_percent = (marks / count)
    non_punct_percent = 1 - punct_percent
    punct_height = punct_percent * 400
    non_punct_height = non_punct_percent * 400

    # Displays the header and then the border rectangle.
    gui.text(450, 110, "Punct/Non-Punct", "white", 15)
    gui.rectangle(445, 145, 160, 410, "black")

    # Draws the "punctuated" bar segment.
    starting_point = 150
    gui.rectangle(450, starting_point, 150, punct_height, "green")
    gui.text(450, starting_point, "Punctuated", "white", 10)
    # Increments the starting point so that the next segment starts where
    # the previous segment ends.
    starting_point += punct_height

    # Draws the "non punctuated" bar segment.
    gui.line(450, starting_point, 600, starting_point, "black", 6)
    gui.rectangle(450, starting_point, 150, non_punct_height, "red")
    gui.text(450, starting_point, "Non Punctuated", "white", 10)

def main() :
    # Asks the user what file to open, and gathers the words.
    file = input("Create an infographic for which file? \n")
    word_list = get_words(file)

    # Calls all the functions to analyze the text files,
    # passing parameters through them all.
    word_count = count_words(word_list)
    small, medium, large = word_lengths(word_count)
    most_common = most_common_words(small, medium, large)
    unique = unique_words(word_list)
    capitals = capital_words(unique)
    marks = punctuation(unique)

    # Draws the infographic.
    gui = graphics(650, 700, "Infographic")
    gui.rectangle(0, 0, 750, 750, "dark blue")
    text_info(gui, file, len(unique), most_common)
    word_length_chart(gui, small, medium, large, len(unique))
    capitals_chart(gui, len(unique), capitals)
    punctuation_chart(gui, len(unique), marks)
    gui.draw()
    
main()