import imageio.v3 as iio #v3= version 3 of the imageio library + "as" means renamed imageio.v3 to iio 
filenames= ['team-pic1.png', 'team-pic2.png']
images= []
for filename in filenames: #for loop goes through the file paths + read the images using imageio library’s .imread() method:
  images.append(iio.imread(filename)) #append built-in function(lists) The .imread() method loads an image based on the file path. So now, our images variable has all the images!
iio.imwrite('team.gif', images, duration = 500, loop = 0)
#'team.gif': This is the name you want to give to your new GIF file.
#images: The list containing the image data.
#duration = 500: How long each picture should show in the GIF, in milliseconds.
#loop = 0: How many times the GIF should repeat (0 means it keeps looping forever).