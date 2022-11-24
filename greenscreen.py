### Author: Jordan Orvik
### Class: CSC 110
### Description: This program takes a PPM image file and replaces a red, green or
### blue screen in the background with another user-chosen PPM image.
### The images are combined in this way and saved to a new image.
### The background color and masking differences are set by the user.

def get_image_dimensions_string(file_name):
    '''
    Given the file name for a valid PPM file, this function will return the
    image dimensions as a string. For example, if the image stored in the
    file is 150 pixels wide and 100 pixels tall, this function should return
    the string '150 100'.
    file_name: A string. A PPM file name.
    '''
    image_file = open(file_name, 'r')
    image_file.readline()
    return image_file.readline().strip('\n')

def load_image_pixels(file_name):
    ''' 
    Load the pixels from the image saved in the file named file_name.
    The pixels will be stored in a 3d list, and the 3d list will be returned.
    Each list in the outer-most list are the rows of pixels.
    Each list within each row represents and individual pixel.
    Each pixel is representd by a list of three ints, which are the RGB values of that pixel.
    '''
    pixels = []
    image_file = open(file_name, 'r')

    image_file.readline()
    image_file.readline()
    image_file.readline()

    width_height = get_image_dimensions_string(file_name)
    width_height = width_height.split(' ')
    width = int(width_height[0])
    height = int(width_height[1])

    for line in image_file:
        line = line.strip('\n ')
        rgb_row = line.split(' ')
        row = []
        for i in range(0, len(rgb_row), 3):
            pixel = [int(rgb_row[i]), int(rgb_row[i+1]), int(rgb_row[i+2])]
            row.append(pixel)
        pixels.append(row)

    return pixels





def pixel_swap(color, diff, gs_pixels, fi_pixels) :
    '''
    This function creates a new image, replacing the background of the
    greenscreen with the fill-in image.
    The function takes the color channel and difference values
    and compares them against the greenscreen image.
    The new image starts off as the greenscreen image, however:
    if the current pixel in the greenscreen image has a higher color value
    in the selected color channel than the other color values 
    multiplied by the color channel difference, that pixel is swapped to the
    corresponding pixel in the fill-in image. If not, the pixel will remain how it was in the 
    greenscreen image. 
    The new image list with the proper pixels swapped is then returned.

    channel = the color (r, g or b) that will be masked out.
    diff = the channel difference value (should be a float from 1-10).
    gs_pixels = the 3D list of pixels of the greenscreen image.
    fi_pixels = the 3D list of pixels of the fill-in image.
    '''
    new_image = gs_pixels
    # Iterates through each row of pixels.
    # Note: in range loops are used because multiple lists need to be indexed
    # at the same time.
    for i in range(0, len(gs_pixels)) :

        # Iterates through each pixel in a row.
        for j in range(0, len(gs_pixels[i])) :
            # Red-screen
            if color == "r" :
                if gs_pixels[i][j][0] > (diff*gs_pixels[i][j][1]) :
                    if gs_pixels[i][j][0] > (diff * gs_pixels[i][j][2]) :
                        new_image[i][j] = fi_pixels[i][j]
            # Green-screen
            elif color == "g" :
                if gs_pixels[i][j][1] > (diff*gs_pixels[i][j][0]) :
                    if gs_pixels[i][j][1] > (diff * gs_pixels[i][j][2]) :
                        new_image[i][j] = fi_pixels[i][j]
            # Blue-screen
            elif color == "b" :
                if gs_pixels[i][j][2] > (diff*gs_pixels[i][j][0]) :
                    if gs_pixels[i][j][2] > (diff * gs_pixels[i][j][1]) :
                        new_image[i][j] = fi_pixels[i][j]
    return new_image

def save(filename, size, output) :
    '''
    This function saves the new, edited image to a file specified
    by the user. 

    filename = the name of the output PPM file (with .ppm).
    size = the size of the image (identical to GS image)
    output = the 3D list of pixels of the new image.
    '''
    file = open(filename, "w")
    
    # Writes the header.
    file.write("P3 \n")
    file.write(size + "\n")
    file.write("255 \n")

    # Writes the pixel contents.
    for row in output :
        for pixel in row :
            for colors in pixel :
                file.write(str(colors) + " ")
        file.write("\n")
    file.close()

def main():
    # Asks the user for the 5 inputs and validates them.
    # If any validity condition fails, the program ends.
    channel = input('Enter color channel\n')
    if not (channel == "r" or channel == "g" or channel == "b") :
        print("Channel must be r, g, or b. Will exit.")
        exit()
    channel_difference = input('Enter color channel difference\n')
    if 1.0 < float(channel_difference) < 10.0 :
        diff = float(channel_difference)
    else :
        print("Invalid channel difference. Will exit.")
        exit()
    gs_file = input('Enter greenscreen image file name\n')
    fi_file = input('Enter fill image file name\n')
    gs_size = get_image_dimensions_string(gs_file)
    fi_size = get_image_dimensions_string(fi_file)
    if not gs_size == fi_size :
        print("Images not the same size. Will exit.")
        exit()
    out_file = input('Enter output file name\n')
    # Loads the pixels from each image.
    gs_pixels = load_image_pixels(gs_file)
    fi_pixels = load_image_pixels(fi_file)
    # Creates the new image with the swapped background.
    output = pixel_swap(channel, diff, gs_pixels, fi_pixels)
    # Saves the new image to a new file.
    save(out_file, gs_size, output)
    print("Output file written. Exiting.")
main()

