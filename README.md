# prettyscatter

This Python project enhances scatter plot visualizations by normalizing data points and incorporating custom images as markers using Plotly. It's designed to create visually appealing and informative scatter plots with personalized touches.

![alt text](https://github.com/WolffM/prettyscatter/blob/main/assets/newplot.png)

## Features

- **Data Normalization:** Scales scatter plot data to fit within a specified range (e.g., [0, 1]).
- **Image Markers:** Replaces standard plot markers with custom images.
- **Rounded Image Processing:** Rounds the corners of images for a smoother look.
- **Background Customization:** Apply gradient backgrounds to enhance visual aesthetics.
- **Plotly Integration:** Leverages Plotly's powerful graphing capabilities for interactive and customizable plots.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/WolffM/prettyscatter.git
   cd prettyscatter
   ```

2. **Install Dependencies:**
   ```bash
   pip install plotly pandas Pillow
   ```

## Usage

1. **Prepare Your Data:**
   - Create a CSV file with your x and y coordinates.
   - Place your custom marker images (PNG format) in the `assets` folder.

2. **Run the Script:**
   ```bash
   python scatter.py
   ```

3. **View Your Plot:**
   - The script will generate an interactive scatter plot in your browser.
   - Hover over data points to see the corresponding image markers.

## Files

- `scatter.py`: Main script to create the scatter plot.
- `imageprocessing.py`: Functions for image manipulation (rounding corners).
- `background.py`: Functions to add background gradients (not shown in provided code).
- `statics.py`: Contains coordinate data and image file names (not shown in provided code).

## Customization

- **Data:** Modify the CSV file with your own data points.
- **Images:** Replace the images in the `assets` folder with your own.
- **Image Size:** Adjust the `sizex` and `sizey` parameters in `scatter.py` to change the marker size.
- **Background:** Experiment with different background colors and gradients in `background.py`.

## Additional Notes

- The project assumes you have a Discord bot token (`DISCORD_TOKEN`) and guild ID (`DISCORD_GUILD`) in a `.env` file. This functionality is not directly related to the scatter plot creation and might be part of a larger project.

## Example

The project includes an example (`newplot.png`) demonstrating the output with custom rounded image markers on a scatter plot.

## Contributing

Contributions are welcome! Feel free to open issues, submit pull requests, or suggest improvements.
