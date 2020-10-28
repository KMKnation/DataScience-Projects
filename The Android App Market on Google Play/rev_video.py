# Python program to save a video using OpenCV


import cv2

rev_video = cv2.VideoCapture("D:\\chrome_download\\videoplayback.mp4")

frame_width = int(rev_video.get(3))
frame_height = int(rev_video.get(4))

size = (frame_width, frame_height)

result = cv2.VideoWriter('reverse_video.avi', cv2.VideoWriter_fourcc(*'MJPG'), 10, size)
while (True):

    ret, frame = rev_video.read()
    if ret == True:

        result.write(frame)
        cv2.imshow('Frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

    else:
        break

rev_video.release()
result.release()

cv2.destroyAllWindows()

print("The video was successfully saved")