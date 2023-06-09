import copy


def remove_red(pixel_data):
    """Sets all red channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[0] = 0
    return new_pixel_data


def remove_green(pixel_data):
    """Sets all green channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[1] = 0
    return new_pixel_data


def remove_blue(pixel_data):
    """Sets all blue channels to 0 in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[2] = 0
    return new_pixel_data


def invert_red(pixel_data):
    """ Inverts the red channel in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[0] = 255 - pixel[0] 
    return new_pixel_data


def invert_green(pixel_data):
    """ Inverts the green channel in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[1] = 255 - pixel[1] 
    return new_pixel_data


def invert_blue(pixel_data):
    """ Inverts the blue channel in a list of pixels."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            pixel[2] = 255 - pixel[2] 
    return new_pixel_data


def grayscale(pixel_data):
    """ Converts all the pixels in a pixel list to grayscale."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        for pixel in row:
            sum_pixel = pixel[0] + pixel[1] + pixel[2]
            pixel[0] = round(sum_pixel / 3)
            pixel[1] = round(sum_pixel / 3)
            pixel[2] = round(sum_pixel / 3)
    return new_pixel_data


def flip_horizontal(pixel_data):
    """ Flips the pixels in the list so that the left-most become the right-most."""
    new_pixel_data = copy.deepcopy(pixel_data)
    for row in new_pixel_data:
        row.reverse()
    return new_pixel_data


def flip_vertical(pixel_data):
    """ Flips the pixels in the list so that the top-most become the bottom-most."""
    new_pixel_data = copy.deepcopy(pixel_data)
    new_pixel_data.reverse()
    return new_pixel_data