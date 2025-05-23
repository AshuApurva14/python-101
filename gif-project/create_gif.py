# Create a GIF from images

# Import necessary libraries
import imageio.v3 as iio


# Create an List of images
filenames =['/workspaces/python-101/gif-project/team-pic1.png', '/workspaces/python-101/gif-project/team-pic2.png']

# Create a empty to store images
images = []

# Read images and append to the list
for filename in filenames:
   images.append(iio.imread(filename))

# Create a GIF from the images

iio.imwrite('team.gif', images, duration=500, loop=0)

