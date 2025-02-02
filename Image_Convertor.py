import streamlit as st  # Import Streamlit for creating the web application
from PIL import Image, ImageOps  # Import PIL for image processing
import os  # Import os for file system operations

# Title of the Streamlit app
st.title("Image Compressor and Converter")

# Hide the Streamlit style header and footer
hide_st_style = """
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1v0mbdj {visibility: hidden;}  /* Hide the 'Deploy' button */
            .reportview-container {
                background-color: black;  /* Set background color to black */
            }
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)  # Apply the custom CSS

# Sidebar for user input
st.sidebar.header("Upload an image")  # Add header to the sidebar
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])  # File uploader for images

# Select compression quality
quality = st.sidebar.slider("Select compression quality", 10, 100, 85)  # Slider for selecting compression quality

# Create a directory to save processed images if it doesn't exist
output_dir = "processed_images"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to compress an image
def compress_image(image, quality):
    """
    Compresses the given image to the specified quality.
    Converts the image to RGB and saves it as JPEG.
    """
    image = image.convert("RGB")  # Convert image to RGB
    output_path = os.path.join(output_dir, f"{uploaded_file.name}")  # Generate output path
    image.save(output_path, "JPEG", quality=quality)  # Save the compressed image
    return output_path

# Function to convert image format
def convert_image_format(image, format):
    """
    Converts the given image to the specified format.
    """
    output_path = os.path.join(output_dir, f"{os.path.splitext(uploaded_file.name)[0]}.{format.lower()}")  # Generate output path
    image.save(output_path, format)  # Save the image in the new format
    return output_path

# Function to resize an image
def resize_image(image, width, height):
    """
    Resizes the given image to the specified width and height.
    """
    resized_image = image.resize((width, height))  # Resize the image
    output_path = os.path.join(output_dir, f"resized_{uploaded_file.name}")  # Generate output path
    resized_image.save(output_path)  # Save the resized image
    return resized_image, output_path

# Function to crop an image
def crop_image(image, left, top, right, bottom):
    """
    Crops the given image using the specified coordinates.
    """
    cropped_image = image.crop((left, top, right, bottom))  # Crop the image
    output_path = os.path.join(output_dir, f"cropped_{uploaded_file.name}")  # Generate output path
    cropped_image.save(output_path)  # Save the cropped image
    return cropped_image, output_path

# Function to convert an image to grayscale
def convert_to_grayscale(image):
    """
    Converts the given image to grayscale.
    """
    grayscale_image = ImageOps.grayscale(image)  # Convert image to grayscale
    output_path = os.path.join(output_dir, f"grayscale_{uploaded_file.name}")  # Generate output path
    grayscale_image.save(output_path)  # Save the grayscale image
    return grayscale_image, output_path

# Check if a file is uploaded
if uploaded_file is not None:
    # Open the uploaded image
    original_image = Image.open(uploaded_file)  # Open the uploaded image
    modified_image = original_image  # Initialize modified image as the original image

    # Display the original image
    st.image(original_image, caption="Original Image", use_container_width=True)  # Display the original image

    # Function to handle the user's choice of image to modify
    def get_image_to_modify():
        """
        Returns the image chosen by the user to modify (original or modified).
        """
        if st.sidebar.radio("Choose the image to modify", ("Original Image", "Modified Image")) == "Original Image":
            return original_image
        else:
            return modified_image

    # Compress the image
    if st.sidebar.button("Compress Image"):
        compressed_image_path = compress_image(modified_image, quality)  # Compress the image

        st.success("Image compressed successfully!")  # Display success message

        # Display the compressed image
        compressed_image = Image.open(compressed_image_path)  # Open the compressed image
        st.image(compressed_image, caption="Compressed Image", use_container_width=True)  # Display the compressed image
        modified_image = compressed_image  # Update modified image

        # Provide a download link for the compressed image
        with open(compressed_image_path, "rb") as file:
            st.download_button(
                label="Download Compressed Image",
                data=file,
                file_name=uploaded_file.name,
                mime="image/jpeg"
            )

    # Additional options
    st.sidebar.header("Additional Options")

    # Rotate the image
    rotate_angle = st.sidebar.slider("Rotate the image (in degrees)", 0, 360, 0)  # Slider for rotation angle
    if st.sidebar.button("Rotate Image"):
        rotated_image = modified_image.rotate(rotate_angle)  # Rotate the image
        st.image(rotated_image, caption=f"Rotated Image by {rotate_angle}°", use_container_width=True)  # Display the rotated image
        modified_image = rotated_image  # Update modified image

    # Resize the image
    resize_width = int(st.sidebar.number_input("Resize width", min_value=50, max_value=2000, value=640))  # Input for resize width
    resize_height = int(st.sidebar.number_input("Resize height", min_value=50, max_value=2000, value=360))  # Input for resize height
    if st.sidebar.button("Resize Image"):
        resized_image, resized_image_path = resize_image(modified_image, resize_width, resize_height)  # Resize the image
        st.image(resized_image, caption="Resized Image", use_container_width=True)  # Display the resized image
        modified_image = resized_image  # Update modified image
        # Provide a download link for the resized image
        with open(resized_image_path, "rb") as file:
            st.download_button(
                label="Download Resized Image",
                data=file,
                file_name=f"resized_{uploaded_file.name}",
                mime="image/jpeg"
            )

    # Crop the image
    st.sidebar.header("Crop Image")
    left = int(st.sidebar.number_input("Left", min_value=0, max_value=original_image.width, value=0))  # Input for left coordinate
    top = int(st.sidebar.number_input("Top", min_value=0, max_value=original_image.height, value=0))  # Input for top coordinate
    right = int(st.sidebar.number_input("Right", min_value=0, max_value=original_image.width, value=original_image.width))  # Input for right coordinate
    bottom = int(st.sidebar.number_input("Bottom", min_value=0, max_value=original_image.height, value=original_image.height))  # Input for bottom coordinate
    if st.sidebar.button("Crop Image"):
        cropped_image, cropped_image_path = crop_image(modified_image, left, top, right, bottom)  # Crop the image
        st.image(cropped_image, caption="Cropped Image", use_container_width=True)  # Display the cropped image
        modified_image = cropped_image  # Update modified image
        # Provide a download link for the cropped image
        with open(cropped_image_path, "rb") as file:
            st.download_button(
                label="Download Cropped Image",
                data=file,
                file_name=f"cropped_{uploaded_file.name}",
                mime="image/jpeg"
            )

    # Convert the image to grayscale
    if st.sidebar.button("Convert to Grayscale"):
        grayscale_image, grayscale_image_path = convert_to_grayscale(modified_image)  # Convert the image to grayscale
        st.image(grayscale_image, caption="Grayscale Image", use_container_width=True)  # Display the grayscale image
        modified_image = grayscale_image  # Update modified image
        # Provide a download link for the grayscale image
        with open(grayscale_image_path, "rb") as file:
            st.download_button(
                label="Download Grayscale Image",
                data=file,
                file_name=f"grayscale_{uploaded_file.name}",
                mime="image/jpeg"
            )

    # Format conversion options
    st.sidebar.header("Format Conversion")
    format_options = ["JPEG", "PNG", "BMP", "GIF"]  # List of format options
    selected_format = st.sidebar.selectbox("Select format to convert to", format_options)  # Dropdown for format selection
    if st.sidebar.button("Convert Format"):
        converted_image_path = convert_image_format(modified_image, selected_format)  # Convert the image format
        st.success(f"Image converted to {selected_format} format successfully!")  # Display success message
        converted_image = Image.open(converted_image_path)  # Open the converted image
        st.image(converted_image, caption=f"Image in {selected_format} format", use_container_width=True)  # Display the converted image
        modified_image = converted_image  # Update modified image
        # Provide a download link for the converted image
        with open(converted_image_path, "rb") as file:
            st.download_button(
                label=f"Download {selected_format} Image",
                data=file,
                file_name=f"{os.path.splitext(uploaded_file.name)[0]}.{selected_format.lower()}",
                mime=f"image/{selected_format.lower()}"
            )

    # Custom About section
    st.sidebar.header("About")
    st.sidebar.markdown("""
    **This project is made by me [Y.Sathya Sai](mailto:ysathyasai.dev@gmail.com). For any queries, you can contact me at [ysathyasai.dev@gmail.com](mailto:ysathyasai.dev@gmail.com).**
    """)

else:
    st.warning("Please upload an image to get started.")  # Display warning if no image is uploaded