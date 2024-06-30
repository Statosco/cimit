import glob
from PIL import Image

print(glob.glob("*.png"))

for file in glob.glob("*.png"):
    im = Image.open(file)
    rgbIm = im.convert('RGB')
    rgbIm.save(file.replace("png", "jpg"), quality=950)
