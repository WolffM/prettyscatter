iterator = 0
for i, row in df.iterrows():
    image = Image.open(imageFiles[iterator], mode="r")
    image = image.convert("RGBA")

    # Create a circular mask image with the same size as the rectangular image
    mask = Image.new('L', image.size, 0)

    # Convert the circular mask image to the "RGBA" pixel format
    mask = mask.convert("RGBA")

    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + image.size, fill=255)

    output = Image.blend(image, mask, 255)
