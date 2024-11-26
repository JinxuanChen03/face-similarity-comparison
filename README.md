### 人脸相似度检测

#### 项目文件解释

`pages` - Web前端

- `index.html` - 主页面

FaceRecoPy - Flask后端

- `main.py` - 后端路由
- `cropping_faces.py` - 截取人脸
- `encoding_faces.py` - 获取人像特征
- `comparing_faces.py` - 人脸相似度对比
- `celebrity_encodings.joblib` - 预提取好的明星人脸特征

#### ~~如何构建人脸信息数据库~~

~~首先有一个`celebrities`文件夹，用于存储爬取好的人像照片，图片名称以明星姓名命名。~~

~~先运行`croping_faces.py`，自动生成`cropped_images`文件夹，存储了截取人脸的图片。~~

~~再运行`encoding_faces.py`，自动生成`celebrity_encodings.joblib`，其中存储了明星的人像特征。~~

**本项目已在`celebrity_encodings.joblib`中预提取了人脸特征，可跳过构建人像数据库这一步，直接进行部署。**

#### 如何部署

打开`FaceRecoPy`文件夹，在终端输入以下命令

```
python main.py
```

后端将运行在`http://127.0.0.1:5000`

在浏览器访问`http://127.0.0.1:5501/index.html`，即可使用
