from PIL import Image


class ImageToAscii:
    """
    A class used to turn images into ASCII art. Converted images will have a max
    width of 100 characters.

    Variables:

    image : Image
        an empty Image object from the library Pillow

    aspect_ratio : float
        the aspect ratio of the image being converted

    scale : array of char
        11 characters in order of heavy to light that the ASCII image will use

    Methods:

    import_image(name)
        imports the image from the argument and prepares it for conversion

        :param name: name of the file being converted

    gray_image()
        converts the imported image into grayscale

    resize_image()
        resizes the image to have a width of 100, aspect ratio preserved

    ascii_image()
        turns the grayscale resized image into a list of ascii characters

    print_ascii_image()
        formats the string of ascii characters, saves it in a txt file, and
        prints it in the console

    full_conversion(name)
        calls all of the previous functions to convert the image in a single
        call outside of the class.

        :param name: name of the file being converted
    """

    scale = ["@", "#", "S", "%", "?", "*", "+", ";", ":", ",", "."]

    def __init__(self):
        """
        Creates an empty Image object for use in the functions.
        """
        self.image = Image

    def import_image(self, name):
        """
        Uses the 'name' parameter to import an image using the Image class from
        the library Pillow.
        :param name: name of image being imported
        """
        self.image = Image.open(name)

    def gray_image(self):
        """
        Uses the convert function in the Image class from the library Pillow
        to make the image black and white. Assumes you already imported an
        image.
        """
        self.image = self.image.convert("L")

    def resize_image(self):
        """
        Gets the aspect ratio of the image, then resizes the image to have a
        width of 100 pixels with respect to the aspect ratio. Assumes you
        already imported an image.
        """
        # the width and length of the image is held in the tuple accessed with
        # Image.size, with width being the first and length being the second
        # integer.
        aspect_ratio = self.image.size[1] / self.image.size[0]
        self.image = self.image.resize((100, int(100 * aspect_ratio)))

    def ascii_image(self):
        """
        Using the getdata() function from Image to return the grayscale value
        of each pixel in the image, then uses a list comprehension to create a
        new string of ascii characters based on those values. Assumes you
        already imported an image.

        :return: ascii_art : the ascii_art variable
        """
        pixels = self.image.getdata()
        ascii_art = ""
        for pixel in pixels:
            # Since grayscale pixels are measured in color by the scale 0-255,
            # dividing by 25 allows for each pixel to be matched to one of 11
            # ASCII characters in the global variable scale. This loop assigns a
            # character to each pixel then appends it to the ascii_art string.
            ascii_art = ascii_art + "".join(self.scale[pixel // 25])
        return ascii_art

    def print_ascii_image(self):
        """
        Using the output from ascii_image(), this function separates the long
        string of ASCII with a newline character every 100 characters. It also
        saves the resulting ASCII string into a file named "ascii_image.txt" and
        then prints the ASCII art into the console.Assumes you already imported
        an image.
        """
        image_data = self.ascii_image(self)
        pixel_count = len(image_data)
        # This line adds a newline character after every 100th character in the
        # ASCII string to format it for viewing. It uses array notation since
        # strings are array of characters and join to append the newline char.
        ascii_image = "\n".join(image_data[i:(i + 100)] for i in
                                range(0, pixel_count, 100))
        txt_name = input("What do you want to save the ASCII art as?\n")
        # This creates or overrides a .txt file with the name the user input.
        with open(txt_name, "w") as f:
            f.write(ascii_image)
        print(ascii_image)

    def full_conversion(self, name):
        """
        Runs all of the functions with the name provided. One call of this
        function will call all of the functions needed to convert the image then
        print and save the image to a file.

        :param name: name of picture
        """
        self.import_image(self, name)
        self.gray_image(self)
        self.resize_image(self)
        self.print_ascii_image(self)


if __name__ == '__main__':
    image_name = input('Enter the name of the image you want to make an ASCII '
                       'image out of.\n')
    ascii_output = ImageToAscii
    ascii_output.full_conversion(ascii_output, image_name)
