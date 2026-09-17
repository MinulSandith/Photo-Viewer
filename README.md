# Photo Viewer

A simple desktop photo viewer built with Python's Tkinter and Pillow. Pick an
image and browse through every picture in the same folder with Forward/Backward
buttons, plus Zoom In/Zoom Out controls — all in a borderless, full-screen window.

## Features

- **Open a picture** via a native file picker.
- **Browse the folder** the chosen picture lives in — Forward/Backward cycle
  through every `.jpg`, `.jpeg`, and `.png` file in that directory (wrapping
  around at the ends).
- **Zoom in / zoom out** on the currently displayed image.
- Automatically scales large images down to fit the screen on load.

## Requirements

- Python 3
- [Pillow](https://pypi.org/project/Pillow/) (`PIL`)
- Tkinter (bundled with most Python installs; on Debian/Ubuntu install it
  separately with `sudo apt install python3-tk`)

## Setup

```bash
pip install Pillow
```

## Usage

Run the viewer from the repository root (it opens with the bundled
`photo.jpg` as the initial image):

```bash
python3 viewer.py
```

Then use the on-screen button to open a picture from any folder, and the
Forward / Backward / Zoom in / Zoom out buttons to navigate and resize it.

## Project structure

| File         | Purpose                                                  |
|--------------|-----------------------------------------------------------|
| `viewer.py`  | Application entry point and all viewer logic              |
| `photo.jpg`  | Default image shown when the app starts                   |
| `images.png` | Icon used for the "choose file" button                    |

## Known limitations

- The UI is laid out with fixed relative coordinates, so it's tuned for a
  single full-screen window rather than arbitrary resizing.
- Only `.jpg`, `.jpeg`, and `.png` files are picked up when browsing a folder.
