import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands

hands = mp_hands.Hands()
# method for drawing points
mp_draw = mp.solutions.drawing_utils

userChoice = None

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
        for hand_landmarks in results.multi_hand_landmarks:
            RING_FINGER_TIP_Y = hand_landmarks.landmark[16].y
            RING_FINGER_MCP_Y = hand_landmarks.landmark[13].y

            PINKY_TIP_Y = hand_landmarks.landmark[20].y
            PINKY_MCP_Y = hand_landmarks.landmark[17].y

            MIDDLE_FINGER_TIP_Y = hand_landmarks.landmark[12].y
            MIDDLE_FINGER_MCP_Y = hand_landmarks.landmark[9].y

            INDEX_FINGER_TIP_Y = hand_landmarks.landmark[8].y
            INDEX_FINGER_MCP_Y = hand_landmarks.landmark[5].y

            if PINKY_TIP_Y < PINKY_MCP_Y and \
               RING_FINGER_TIP_Y < RING_FINGER_MCP_Y and \
               MIDDLE_FINGER_TIP_Y < MIDDLE_FINGER_MCP_Y and \
               INDEX_FINGER_TIP_Y < INDEX_FINGER_MCP_Y:
                userChoice = "ROCK"
            elif PINKY_TIP_Y > PINKY_MCP_Y and \
                 RING_FINGER_TIP_Y > RING_FINGER_MCP_Y and \
                 MIDDLE_FINGER_TIP_Y > MIDDLE_FINGER_MCP_Y and \
                 INDEX_FINGER_TIP_Y > INDEX_FINGER_MCP_Y:
                userChoice = "PAPER"
            elif PINKY_TIP_Y < PINKY_MCP_Y and \
                 RING_FINGER_TIP_Y < RING_FINGER_MCP_Y and \
                 MIDDLE_FINGER_TIP_Y > MIDDLE_FINGER_MCP_Y and \
                 INDEX_FINGER_TIP_Y > INDEX_FINGER_MCP_Y:
                userChoice = "SCISSORS"

            mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    print(userChoice)
    cv2.imshow("TrackMyHands", image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()