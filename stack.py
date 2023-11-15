from PIL import Image

def combine_images_vertically(image_paths, output_path):
    images = [Image.open(image_path) for image_path in image_paths]

    # Get the width and height of the first image
    first_image = images[0]
    width, height = first_image.size

    # Calculate the total height for the combined image
    total_height = height * len(images)

    # Create a new image with the width of the first image and the calculated total height
    combined_image = Image.new('RGB', (width, total_height))

    # Paste each image into the combined image
    y_offset = 0
    for image in images:
        combined_image.paste(image, (0, y_offset))
        y_offset += height

    # Save the combined image
    combined_image.save(output_path)
    print(f"Combined image saved to {output_path}")

if __name__ == "__main__":
    # List of image file paths ("combined_image311238.jpg", "combined_image311239.jpg", etc.)
    base_path = "C:\downloads\2021\20\368521"
    image_paths = list()
    for i in range(311238, 311269):
        image_paths.append(fr"C:\downloads\2021\20\368521\gesh_368521_{i}_20.jpg")
    print(image_paths)
    image_paths.reverse()
    # Output path for the combined image
    output_path = 'me/stacked_image.jpg'

    # Call the function to stack and save the images
    combine_images_vertically(image_paths, output_path)