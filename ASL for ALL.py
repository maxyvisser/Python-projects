import turtle
from PIL import Image

img1 = Image.open(r"C:\Users\MAXYv\Desktop\Files\ASL for ALL\HomepageBG.png")
img2 = Image.open(r"C:\Users\MAXYv\Desktop\Files\external-content.duckduckgo.com-removebg-preview.png")
max = (1024, 1024)
img1.paste(img2, (0, 0), mask = img2)
img1.thumbnail(max, Image.ANTIALIAS)
img1.save(r"C:\Users\MAXYv\Desktop\Files\img1.png")

img = r"C:\Users\MAXYv\Desktop\Files\img1.png"
wn = turtle.Screen()
wn.title = "ASL for ALL"
wn.bgpic(img)

turtle.done()