from PIL import Image, ImageDraw
import plotly.express as px
import pandas as pd
import numpy as np
from background import *
from imageProcessing import *
from statics import *

imageFiles = []
newImage = []
for i in indexLookup:
    imageFiles.append(f"./assets/{i}.png")
    newImage.append(f"{i}2.png")

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

df = pd.DataFrame({'x': x_coords, 'y': y_coords})

fig = px.scatter(x=x_coords,
                 y=y_coords)

iterator = 0
for i, row in df.iterrows():
    rad = 40
    image = getRoundedImage(imageFiles[iterator], newImage[iterator])


    fig.add_layout_image(
        dict(
            source=image,
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
#fig.update_layout(xaxis=dict(range=[-.04, 1.04]),
#                  yaxis=dict(range=[-.04, 1.04]))

fig.update_layout(width=1200, height=1200)

#fig = addBackgroundGradient2(fig)
fig.update_layout(
    xaxis=dict(
        showgrid=False, 
        zeroline=False, 
        title=None, 
        ticktext=None, 
        tickvals=None,
        showticklabels=False), 
    yaxis=dict(
        showgrid=False, 
        zeroline=False, 
        title=None, 
        ticktext=None, 
        tickvals=None,
        showticklabels=False))

# Show the plot
fig.show()
