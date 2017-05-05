import SimpleCV
from SimpleCV import Image, Display, Color
import def colorRange(c , variant):
    variant
    num = [c - variant, c + variant]
    if num[0] < 0:
        num[0] = 0
    if num[1] > 255:
        num[1] = 255
    return num

def change_color(currColor, newColor):
    global qrgen
    global colorVariant
    time.sleep(3)
    subprocess.call('raspistill -n -w %s -h %s -o testimage.png' % (640, 480), shell=True)
    
    img2 = Image('testimage.png')
    #cam2.getImage()
    img2.show()
    time.sleep(5)
    oldRGB = colordef(currColor)
    r = colorRange(oldRGB[0], colorVariant)
    g = colorRange(oldRGB[1], colorVariant)
    b = colorRange(oldRGB[2], colorVariant)
    
    for i in range (r[0], r[1]):
        for j in range (g[0], g[1]):
            for k in range (b[0], b[1]):
                colore = (i, j, k)
                white_distance = img2.colorDistance(colore).invert()
                blobs = white_distance.findBlobs()
                newRGB = colordef(newColor)
                blobs.draw(color= (newRGB[0], newRGB[1], newRGB[2]), width=-18)
    d = white_distance.show()
    time.sleep(8)
    white_distance.save('image.png')
    d.quit()


    

def colordef(i):

    i = i.lower()
    rgbArray = [3]
    if i == "white":
        rgbArray = [255, 255, 255]
    if i == "red":
        rgbArray = [255, 0, 0]
    if i == "yellow":
        rgbArray = [255, 255, 0]
    if i == "black":
        rgbArray = [0, 0, 0]
    if i == "green":
        rgbArray = [0, 255, 0]
    
    return rgbArray
