Here’s an example of a `README.md` file for your QR code generator project. You can customize it as needed:

```markdown
# QR Code Generator

A simple Python application for generating QR codes based on text or images using PyQt5 and the `qrcode` library. This application allows users to generate QR codes by entering text, website URLs, or selecting an image. It also allows saving the generated QR code as an image.

## Features

- Generate QR codes from text or image file paths.
- Choose the QR code type (text or image) via a dropdown.
- Browse for an image file to embed in the QR code.
- Save the generated QR code as a PNG file.
- Simple and easy-to-use interface built with PyQt5.
- Developer name displayed in the app footer.

## Requirements

Before running the application, make sure you have the required libraries installed:

- Python 3.x
- PyQt5
- qrcode
- Pillow (PIL)

You can install the necessary libraries by running:

```bash
pip install pyqt5 qrcode[pil] pillow
```

## Usage

1. Run the Python script `main.py`.
2. Select the type of QR code (Text or Image) from the dropdown.
3. Enter the text or select an image by clicking the "Select an image" button.
4. Click "Generate code QR" to create the QR code.
5. Choose a location to save the generated QR code image.

## Screenshot

![QR Code App Screenshot](screenshot.png)

## Developer

This app was developed by **Obaid Med Bouslahi**.

## License

This project is open-source and available under the MIT License.

```

If you have a screenshot of the app, you can include it as `screenshot.png` in the repository directory. Make sure to update the usage section if you add or modify features.
