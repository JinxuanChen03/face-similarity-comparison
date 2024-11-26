import os
import face_recognition
from PIL import Image
from tqdm import tqdm

def process_image(image_path, output_dir):
    image = face_recognition.load_image_file(image_path)

    face_locations = face_recognition.face_locations(image)

    if not face_locations:
        print(f"No faces detected in {image_path}. Skipping...")
        return

    first_face_location = face_locations[0]

    # Convert the face_recognition image to a PIL image
    img = Image.fromarray(image, 'RGB')

    # Create the cropped image
    img_cropped = img.crop((
        first_face_location[3],
        first_face_location[0],
        first_face_location[1],
        first_face_location[2]
    ))

    # Save the cropped image using the original file name with a suffix
    cropped_image_path = os.path.join(output_dir, f"{os.path.basename(image_path)}")
    img_cropped.save(cropped_image_path)
    return cropped_image_path

def process_images(input_dir, cropped_dir):
    # Get a list of all .jpg files in the input directory
    jpg_files = [f for f in os.listdir(input_dir) if f.endswith('.jpg')]

    # Create the output directory if it doesn't exist
    if not os.path.exists(cropped_dir):
        os.makedirs(cropped_dir)

    # Process each .jpg file with a progress bar
    for filename in tqdm(jpg_files, desc="Processing images"):
        image_path = os.path.join(input_dir, filename)

        # Load the image and detect faces
        image = face_recognition.load_image_file(image_path)
        face_locations = face_recognition.face_locations(image)

        if not face_locations:
            print(f"No faces detected in {image_path}. Skipping...")
            continue

        first_face_location = face_locations[0]

        # Convert the face_recognition image to a PIL image
        img = Image.fromarray(image, 'RGB')

        # Create the cropped image
        img_cropped = img.crop((
            first_face_location[3],
            first_face_location[0],
            first_face_location[1],
            first_face_location[2]
        ))

        # Save the cropped image using the original file name with a suffix
        cropped_image_path = os.path.join(cropped_dir, f"{filename}")
        img_cropped.save(cropped_image_path)


# process_images("./celebrities", "./cropped_images")