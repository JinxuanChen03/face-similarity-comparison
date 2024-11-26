import os.path

from cropping_faces import process_image
from encoding_faces import encode_image
import face_recognition

def compare_faces(image_path, face_encodings_to_compare, face_names_to_compare):
    # 截取人脸
    cropped_path = process_image(image_path,os.path.dirname(image_path))
    # 检测面部特征
    uploaded_face_encoding = encode_image(cropped_path)
    if uploaded_face_encoding is None:
        return {"error": "未检测到人脸"}

    # 对比上传图像与明星人脸的相似度
    face_distances = face_recognition.face_distance(face_encodings_to_compare, uploaded_face_encoding)

    # 构建相似度矩阵
    similarity_matrix = {}
    for i, name in enumerate(face_names_to_compare):
        similarity_matrix[name] = 1 - face_distances[i]

    # 找出相似度最高的三组数据
    top3 = sorted(similarity_matrix.items(), key=lambda item: item[1], reverse=True)[:3]

    # 构建返回结果
    result = []
    for name, similarity in top3:
        result.append({
            "name": name,
            "similarity": round(similarity * 100, 2),  # 转换为百分比形式
        })

    return result