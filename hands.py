import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mp_hands= mp.solutions.hands

hands = mp_hands.Hands()
# method for drawing points
mp_draw= mp.solutions.drawing_utils

while True:
    success, image = cap.read()
    # converting BGR image to RGB
    img_RGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # getting the image
    results = hands.process(img_RGB)
    #  showing image
    # print(results.multi_hand_landmarks)

    # if landmarks are detected than this works
    if results.multi_hand_landmarks:
        for hand_landmarks in  results.multi_hand_landmarks:
            mp_draw.draw_landmarks(image,hand_landmarks, mp_hands.HAND_CONNECTIONS)

    cv2.imshow("TrackMyHands", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()