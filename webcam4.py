import cv2
import time
from flask import Flask, Response
app = Flask(__name__)

@app.route('/')
def index():
    return "Default Message!!"

def gen():

   cap = cv2.VideoCapture('example.mp4')
   while(cap.isOpened()):
       ret, img = cap.read()
       if ret == True:
           img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)
           frame = cv2.imencode('.jpg', img)[1].tobytes()

           yield (b'--frame\r\n'b'Content-Type: image/jpef\r\n\r\n' + frame + b'\r\n')
           time.sleep(0.1)
       else:
           break

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')