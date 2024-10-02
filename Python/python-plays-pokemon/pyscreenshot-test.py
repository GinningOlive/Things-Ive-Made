import pyscreenshot
from PIL import Image
import time
import random
import subprocess
# import pyscreeze

image = pyscreenshot.grab(bbox=(549,494,550,495)) # First Pokemon
rgb_value = image.getpixel((0, 0))
if rgb_value[1] > 200:
    time.sleep(random.randint(1, 5))
    subprocess.call('xdotool key space', shell=True)
    time.sleep(random.randint(1, 5))
    subprocess.call('xdotool key space', shell=True)
    print("attacking")
else:
    image = pyscreenshot.grab(bbox=(1919,0,1920,1)) # Second Pokemon
    rgb_value = image.getpixel((0, 0))
    if rgb_value[1] > 200:
        print("switching to second pokemon")
    else:
        image = pyscreenshot.grab(bbox=(0,1079,1,1080)) # Third Pokemon
        rgb_value = image.getpixel((0, 0))
        if rgb_value[1] > 200:
            print("test3")
        else:
            image = pyscreenshot.grab(bbox=(1919,1079,1920,1080)) # Fourth Pokemon
            rgb_value = image.getpixel((0, 0))
            if rgb_value[1] > 200:
                print("test4")
            else:
                image = pyscreenshot.grab(bbox=(959,0,960,1)) # Fifth Pokemon
                rgb_value = image.getpixel((0, 0))
                if rgb_value[1] > 200:
                    print("test5")
                else:
                    image = pyscreenshot.grab(bbox=(959,1079,960,1080)) # Sixth Pokemon
                    rgb_value = image.getpixel((0, 0))
                    if rgb_value[1] > 200:
                        print("test6")
                    else:
                        print("out of usable pokemon")
                        image = pyscreenshot.grab(bbox=(0,0,550,495)) # Find health


# image.save("pyscreenshot.png") # Save screenshot to file
# image.show() #Display screenshot (in browser for some reason)
print(rgb_value)
