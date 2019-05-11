import dlib
import cv2
import time
from math import sqrt
start_time = time.time()
img = cv2.imread('./sad1.jpg')
detector = dlib.get_frontal_face_detector() #Load face detector
dets = detector(img, 1)  #Xác định vị trí khuôn mặt trong bức ảnh
predictor = dlib.shape_predictor('./shape_predictor_68_face_landmarks.dat')
landmark = predictor(img, dets[0])
lines = []
# Xác định facial landmark trên khuôn mặt
for k, d in enumerate(landmark.parts()):
    #xác định khung miệng
     if(k>=60 and k<=68):
         cv2.circle(img, (d.x, d.y), 1, (255, 255, 255), 2)
         lines.append((d.x,d.y))

#tìm điểm trung bình line
x_line = round((lines[4][0]+lines[0][0])/2)
y_line = round((lines[4][1]+lines[0][1])/2)

#tính toán khoảng cách
u_x = (lines[2][0]-x_line)*(lines[2][0]-x_line)
u_y = (lines[2][1]-y_line)*(lines[2][1]-y_line)
print('Khoảng cách điểm trung bình line đến đỉnh trên môi', sqrt(u_x+u_y))
d_x = (lines[6][0]-x_line)*(lines[6][0]-x_line)
d_y = (lines[6][1]-y_line)*(lines[6][1]-y_line)
print('Khoảng cách điểm trung bình line đến đỉnh dưới môi',sqrt(d_x+d_y))

#kết luận
if sqrt(u_x+u_y) < sqrt(d_x+d_y):
    print('Vui')
elif sqrt(u_x+u_y) > sqrt(d_x+d_y):
    if sqrt(u_x+u_y) - sqrt(d_x+d_y) >= 1: #tính độ chênh lệch ( độ chênh lệch tương đương khoảng cách đỉnh môi trên và dưới. Lưu ý : Điểu chỉnh điều kiện để tạo độ nhạy !
        print('buồn')
    else:
        print('Bình thường')

end_time = time.time()
print('time:', end_time-start_time)

#cv2.imshow('complete',img)
#cv2.waitKey()
cv2.imwrite('Image_landmarks_text_new.jpg',img)

#Đây là thuật toán xác định cảm xúc với phương pháp trung điểm