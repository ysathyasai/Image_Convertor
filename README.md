# Image Compressor and Converter

This project is a Streamlit application designed for compressing, resizing, cropping, and converting images between various formats. It provides an intuitive interface for users to upload an image and apply different modifications. This tool is ideal for users who need to quickly and easily manipulate image files without using complex software.

## Features

1. **Compress Image**: Compresses the given image to the specified quality. Converts the image to RGB and saves it as JPEG.
2. **Convert Image Format**: Converts the given image to a different format (JPEG, PNG, BMP, GIF).
3. **Resize Image**: Resizes the given image to the specified width and height.
4. **Crop Image**: Crops the given image using specified coordinates (left, top, right, bottom).
5. **Convert to Grayscale**: Converts the given image to grayscale.

## Detailed Explanation of Functionalities

### Compress Image
- **Description**: Reduces the file size of the uploaded image by adjusting its quality.
- **Usage**: Upload an image and select the desired compression quality using the slider. Click the "Compress Image" button to apply the compression.

### Convert Image Format
- **Description**: Changes the file format of the uploaded image to one of the supported formats (JPEG, PNG, BMP, GIF).
- **Usage**: Upload an image, select the desired format from the dropdown menu, and click the "Convert Format" button.

### Resize Image
- **Description**: Adjusts the dimensions of the uploaded image to specified width and height.
- **Usage**: Upload an image, enter the desired width and height, and click the "Resize Image" button.

### Crop Image
- **Description**: Cuts out a rectangular portion of the uploaded image using specified coordinates.
- **Usage**: Upload an image, enter the coordinates for the left, top, right, and bottom edges, and click the "Crop Image" button.

### Convert to Grayscale
- **Description**: Converts the uploaded image to grayscale, removing all color.
- **Usage**: Upload an image and click the "Convert to Grayscale" button.

## Getting Started

### Prerequisites
- Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

- Install required dependencies using the command below. Ensure `requirements.txt` is present in the project directory.

   ```sh
   pip install -r requirements.txt
   ```
## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/ysathyasai/Image_Convertor.git
   ```
2. Navigate to the project directory in your terminal:
   ```sh
   cd Image_Convertor
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:
   ```sh
   streamlit run Image_Convertor.py
   ```

5. Open your web browser and go to http://localhost:8501 to access the application (Or any ther localhost server provided in your terminal).

## Usage
1. **Upload an Image**: Use the file uploader in the sidebar to upload an image (supported formats: JPG, JPEG, PNG).
2. **Select and Apply Modifications**: Choose the desired functionality from the sidebar, adjust the parameters, and click the corresponding button to apply the changes.
3. **Download Processed Image**: After processing, you can view the modified image and download it using the provided link.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](https://github.com/ysathyasai/Image_Convertor/blob/main/LICENSE) file for details.

## Contributions

Any improvements, corrections, contributions, or ideas are always welcome! Feel free to open an issue or submit a pull request. For any questions or inquiries, please contact [ysathyasai.dev@gmail.com](mailto:ysathyasai.dev@gmail.com).