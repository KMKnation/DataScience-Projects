# Python program to play a video in reverse mode using opencv

import cv2

cap = cv2.VideoCapture("D:\\chrome_download\\videoplayback.mp4")

# Grab the current frame.
check, vid = cap.read()

# counter variable for counting frames
counter = 0

# of check variable
check = True

frame_list = []

# If reached the end of the video
# then we got False value of check.

while (check == True):
    # imwrite method of cv2 saves the
    cv2.imwrite("frame%d.jpg" % counter, vid)
    check, vid = cap.read()

    # Add each frame in the list by using append method of the List

    frame_list.append(vid)

    # increment the counter by 1
    counter += 1

# removing the last value from the
# frame_list by using pop method of List
frame_list.pop()

# looping in the List of frames.
for frame in frame_list:

    # show the frame.
    cv2.imshow("Frame", frame)

    # waitkey method to stoping the frame
    # for some time. q key is presses,
    # stop the loop
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break

# release method of video
# object clean the input video
cap.release()

# close any open windows
cv2.destroyAllWindows()

# reverse method of the List.
frame_list.reverse()

for frame in frame_list:
    cv2.imshow("Frame", frame)
    if cv2.waitKey(25) and 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
