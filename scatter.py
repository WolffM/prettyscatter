from PIL import Image, ImageDraw
import plotly.express as px
import pandas as pd
import numpy as np

# Update the boundaries to the max and min x and y coordinates in the list

indexLookup = [
    "Loquat",
    "sips",
    "DuffleMonsta",
    "Teddee",
    "irilyvia",
    "[TOPO]",
    "Astroturf",
    "Hadoku",
    "oshi",
    "KooKly The Quiet",
    "Harry",
    "littlemiss",
    "thyeggman",
    "Cozmiverse",
    "B33N",
    'Kawakimi'
]

imageFiles = []
for i in indexLookup:
    imageFiles.append(f"./assets/{i}.png")

coordinates = [
    (0, 4.6, -3.3),
    (1, 6.8, -8.1),
    (2, 8.55, -6.9),
    (3, 5.9, -3.2),
    (4, 7.7, -8.4),
    (5, 4.65, -4.15),
    (6, 5.85, -6.4),
    (7, 16.4, -5.45),
    (8, 4.15, -3.75),
    (9, 12.9, -13.65),
    (10, 9, -13.6),
    (11, 3.6, -5),
    (12, 6.3, -6.3),
    (13, 8.1, -3.85),
    (14, 5.1, -5.1)
    (15, 6.9, -4.6)

]

indexes = [index for index, x, y in coordinates]
x_coords = [x for index, x, y in coordinates]
y_coords = [y for index, x, y in coordinates]

min_x = min(x_coords)
max_x = max(x_coords)
min_y = min(y_coords)
max_y = max(y_coords)

# Normalize the coordinates with the new ranges
normalized_x_coords = [((x - min_x) / (max_x - min_x)) for x in x_coords]
normalized_y_coords = [((y - min_y) / (max_y - min_y)) for y in y_coords]

df = pd.DataFrame({'x': normalized_x_coords, 'y': normalized_y_coords})

fig = px.scatter(x=normalized_x_coords,
                 y=normalized_y_coords)


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

    fig.add_layout_image(
        dict(
            source=output,
            xref="x",
            yref="y",
            xanchor="center",
            yanchor="middle",
            x=row["x"],
            y=row["y"],
            sizex=.08,
            sizey=.08,
            sizing="contain",
            opacity=0.9,
            layer="above",

        )
    )
    iterator += 1

# Set the x and y axis ranges to [0, 1]
fig.update_layout(xaxis=dict(range=[-.04, 1.04]),
                  yaxis=dict(range=[-.04, 1.04]))

# Show the plot
fig.show()
