image = Image.open(imageFiles[iterator], mode="r")
image = image.convert("RGBA")

# Create a circular mask image
mask = Image.new('L', image.size, 0)
mask = mask.convert("RGBA")

draw = ImageDraw.Draw(mask)
draw.ellipse((0, 0) + image.size, fill=0)

output = Image.alpha_composite(image, mask)
