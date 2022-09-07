from types import NoneType
import cv2
import mediapipe as mp
cap = cv2.VideoCapture(0)
hands_mp = mp.solutions.hands
connection_mp = mp.solutions.drawing_utils
tipIndex = [8 , 12 , 16 , 20]
hands = hands_mp.Hands(min_detection_confidence = 0.8 , min_tracking_confidence = 0.5)

def Reaction(image , hand_landmarks , handNo = 0):
    if(hand_landmarks):
        fingers = []
        landmarks = hand_landmarks[handNo].landmark
        for i in tipIndex:
            
            fingerX = landmarks[i].x
            fingerBx = landmarks[i-2].x
            Ty = landmarks[4].y
            BTy = landmarks[2].y
            Wy = landmarks[0].y
            if(i != 4):
                if(fingerX>fingerBx):
                    fingers.append(0)
                elif(fingerX<fingerBx):
                    fingers.append(1)
                if(Ty>BTy):
                    fingers.append(0)
                elif(Ty<BTy):
                    fingers.append(1)
            if(fingers.count(0) == 4):
                
                if(Ty<Wy):
                    cv2.putText(image,"LIKE",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
                elif(Ty>Wy):
                    cv2.putText(image,"DISLIKE",(75,90),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
def drawHandLanmarks(image, hand_landmarks):

    # Darw connections between landmark points
    if hand_landmarks:

      for landmarks in hand_landmarks:
               
        connection_mp.draw_landmarks(image, landmarks, hands_mp.HAND_CONNECTIONS)


while True:
    ret , image = cap.read()
    image = cv2.flip(image , 1)
    results = hands.process(image)
    hand_landmarks = results.multi_hand_landmarks
    Reaction(image , hand_landmarks)
    drawHandLanmarks(image , hand_landmarks)
    cv2.imshow("frame" , image)
    if (cv2.waitKey(25) == 32):
        break
cv2.destroyAllWindows()
cap.release()