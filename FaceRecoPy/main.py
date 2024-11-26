from flask import Flask, request, jsonify
from comparing_faces import compare_faces
from encoding_faces import load_encodings
from flask_cors import CORS
import os
import tempfile

app = Flask(__name__)
CORS(app)  # 允许所有来源访问

# 加载预编码的明星人脸
encoding_path = 'celebrity_encodings.joblib'
celebrity_encodings, celebrity_names = load_encodings(encoding_path)
print(f"Loaded {len(celebrity_encodings)} celebrity encodings from file.")

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'photo' not in request.files:
        return jsonify({'error': '未上传照片'}), 400

    # 获取上传的图像
    image_file = request.files['photo']

    # 保存文件到临时文件夹
    with tempfile.TemporaryDirectory() as tmpdirname:
        file_path = os.path.join(tmpdirname, image_file.filename)
        image_file.save(file_path)

        # 对比上传的图像与明星人脸的相似度
        result = compare_faces(file_path, celebrity_encodings, celebrity_names)
        if 'error' in result:
            return jsonify(result), 400

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)