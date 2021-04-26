from flask import Flask,render_template,jsonify
app = Flask(__name__)
import numpy as np
import cv2
from flask import make_response
from flask import request
from flask import url_for
import base64



@app.route('/')
def index():
    # 顯示表單
    return render_template('form.html')

# @app.route('/', methods=['POST'])
# def process():
#     # 處理圖片
#     return 'Process'

@app.route('/', methods=['POST'])
def process():
    # 取得上傳的圖片
    file1 = request.files['image1']
    # 讀取檔案內容
    file1_content = file1.read()
    # 將檔案內容轉為 Numpy Array
    npimg1 = np.fromstring(file1_content, np.uint8)
    # 將 Numpy Array 進行圖像解碼
    bgr1 = cv2.imdecode(npimg1, cv2.IMREAD_COLOR)
    # return jsonify(bgr1.shape)

    _, buffer = cv2.imencode('.jpg', bgr1)
    response = make_response(buffer.tobytes())
    response.mimetype = 'image/jpg'

    rgb1 = cv2.cvtColor(bgr1, cv2.COLOR_BGR2RGB)
    height, width = rgb1.shape[:2]
    radius = int(min(height, width) * 0.48)
    thickness = int(min(height, width) * 0.02)
    cv2.circle(rgb1, (int(width / 2), int(height / 2)), radius, (255, 0, 0), thickness)
    bgr1 = cv2.cvtColor(rgb1, cv2.COLOR_BGR2RGB)

    #以 JSON 回傳圖片的 Base64
    # response = {
    #     'output_image': base64.b64encode(cv2.imencode('.jpg', bgr1)[1]).decode()
    # }

    # folderPath = 'static/output_image'
    # if not os.path.exists(folderPath):
    #     os.makedirs(folderPath)

    # filename = '{}.jpg'.format(
    #     datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    # )

    # cv2.imwrite(os.path.join(folderPath, filename), bgr1)

    # response = {
    #     'url': url_for('static', filename='output_image/{}'.format(filename), _external=True)
    # }


    return response



