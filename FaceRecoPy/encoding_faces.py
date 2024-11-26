import os
import face_recognition
from tqdm import tqdm
from joblib import dump, load


def encode_image(image_path):
    image = face_recognition.load_image_file(image_path)
    # 检测面部特征
    face_encodings = face_recognition.face_encodings(image)
    if len(face_encodings) > 0:
        return face_encodings[0]
    else:
        print(f"No faces detected in {image_path}. Skipping...")


def encode_images(face_images_dir, save_path):
    face_encodings = []
    face_names = []

    # 获取所有图像文件名
    image_filenames = os.listdir(face_images_dir)

    for filename in tqdm(image_filenames, desc="Processing images", unit="image"):
        if filename.endswith('.jpg'):
            image_path = os.path.join(face_images_dir, filename)

            image = face_recognition.load_image_file(image_path)
            # 检测面部特征
            encoding = face_recognition.face_encodings(image)
            if len(encoding) > 0:
                face_encodings.append(encoding[0])
                face_names.append(filename.split('.')[0])  # 将文件名作为人名
            else:
                print(f"No faces detected in {image_path}. Skipping...")

    # 保存人脸编码到文件
    code_path = os.path.join(save_path, 'celebrity_encodings.joblib')
    data = {
        'encodings': face_encodings,
        'names': face_names
    }
    dump(data, code_path)


def load_encodings(file_path):
    # 加载编码和对应的人名
    data = load(file_path)
    return data['encodings'], data['names']

# encode_images("./cropped_images", "./")
# celebrity_encodings, celebrity_names = load_encodings("celebrity_encodings.joblib")
# print(type(celebrity_encodings))
# print("qqqqqqqqqqqqqq")
# print(type(celebrity_names))