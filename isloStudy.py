from PIL import Image

def combine_images_horizontally(image_paths, output_path):
    images = [Image.open(image_path) for image_path in image_paths]

    # Get the width and height of the first image
    first_image = images[0]
    width, height = first_image.size

    # Calculate the total width for the combined image
    total_width = width * len(images)

    # Create a new image with the calculated total width and the height of the first image
    combined_image = Image.new('RGB', (total_width, height))

    # Paste each image into the combined image
    x_offset = 0
    for image in images:
        combined_image.paste(image, (x_offset, 0))
        x_offset += width

    # Save the combined image
    combined_image.save(output_path)
    print(f"Combined image saved to {output_path}")

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
    image_paths_horizontal = list()
    image_paths_vertical = list()
    bas_path = fr"C:\downloads\2021\20" #JUST CHANGE THIS
    for j in range(311238, 311269):
        image_paths_horizontal = []
        for i in range(368521, 368561):
            print("You okay")
            image_paths_horizontal.append(fr'{bas_path}\{i}\gesh_{i}_{j}_20.jpg')

        # Output path for the combined image
        output_path = fr'me_horizontal/combined_image{j}.jpg'

        # Call the function to combine and save the images
        combine_images_horizontally(image_paths_horizontal, output_path)
        image_paths_vertical.append(output_path)
    image_paths_vertical.reverse()
output_path = fr'me_vertical/combined_image_2021.jpg'
combine_images_vertically(image_paths_vertical, output_path)
