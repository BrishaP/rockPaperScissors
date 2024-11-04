import cv2

# import library importcv2 to create videocapture object and read the input file
# cv2.VideoCapture(0): Means first camera or webcam
# So initialises video capture object to use first camera (in this case my laptop webcam)
cap = cv2.VideoCapture(0)

# Check if camera is opened

if (cap.isOpened()==False):
    print("Error opening video file")

# Read until video is completed
# Reads frames in a loop, which continues as long as the camera is open 
while(cap.isOpened()):

# Capture frame-by-frame
# cap.read() captures a frame from the camera 
# ret is a boolean checking if the frame was read correctly 
# frame is the captured frame 
# if ret is true, the frame is displayed in a separate window called 'Frame'
    ret, frame = cap.read()
    if ret == True:
    # Display the resulting frame
        cv2.imshow('Frame', frame)
        
    # Press Q on keyboard to exit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

# Break the loop
    else:
        break

# When everything done, release the video capture object and close all OpenCV windows (in this case 'Frame')
cap.release()

# Closes all the frames
cv2.destroyAllWindows()