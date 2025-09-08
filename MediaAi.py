import json
import cv2
import mediapipe as mp

mhands = mp.solutions.hands
hands = mhands.Hands(
    static_image_mode=False
    ,max_num_hands = 2
    ,min_detection_confidence=0.5
    ,min_tracking_confidence=0.5
)
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('Not open')
else:
    print('is open')


def getStateHands(hand_landmarks):
    fts = [8,12,16,20]
    fss = []

    if hand_landmarks.landmark[mhands.HandLandmark.THUMB_TIP].x < hand_landmarks.landmark[mhands.HandLandmark.THUMB_IP].x:
        fss.append(1)
    else:
        fss.append(0)

    for ft in fts:
        if hand_landmarks.landmark[ft].y < hand_landmarks.landmark[ft - 2].y:
            fss.append(1)
        else:
            fss.append(0)
    return fss

def reconGes(fss):
    if fss == [0,1,1,0,0]:
        return 'Peace'
    elif fss == [0,1,0,0,0]:
        return 'Point'
    elif fss == [1,1,1,1,1]:
        return 'Open Hands'
    elif fss == [0,0,0,0,0]:
        return 'Closed'
    elif fss == [1,0,0,0,0]:
        return 'Like'
    else:
        return 'Unknown'

sas = []
while True:
    ret , frame = cap.read()
    fts = range(0,21)
    if not ret:
        break

    irgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    res = hands.process(irgb)

    if res.multi_hand_landmarks:
        for hand_landmarks in res.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame, hand_landmarks, mhands.HAND_CONNECTIONS)

        sst = getStateHands(hand_landmarks)
        gst = reconGes(sst)

        cv2.putText(frame, gst, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2, cv2.LINE_AA)

        if cv2.waitKey(1) & 0xFF == ord('f'):#this is for saving a state of fingertips to get some data
            for ft in fts:
                sas.append({'ft': f'{ft}','x': hand_landmarks.landmark[ft].x , 'y': hand_landmarks.landmark[ft].y,'z': hand_landmarks.landmark[ft].z})
                print('state appended')


    cv2.imshow('Cam', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


if sas:
    with open('GesData/Codata.json', 'x') as jsf:# you should replace Codata name with the gesture you want to save the coordinates for.
        jsf.write(json.dumps(sas,indent=4))
        print('saved states')
cap.release()
cv2.destroyAllWindows()