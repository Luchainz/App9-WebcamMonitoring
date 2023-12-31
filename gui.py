import streamlit as st
import cv2
from datetime import datetime


st.title("Motion Detector")
start = st.button("Start Camera")

if start:
    streamlit_image = st.image([])
    camera = cv2.VideoCapture(0)

    while True:
        check, frame = camera.read()
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Get current time as a datetime obj.
        now = datetime.now()

        # Get day and time, add them to the frame.
        cv2.putText(img=frame, text=now.strftime("%A"), org=(30, 80),
        fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(225, 255, 255),
                    thickness=2, lineType=cv2.LINE_AA)

        cv2.putText(img=frame, text=now.strftime("%H:%M:%S"), org=(30, 140),
                    fontFace=cv2.FONT_HERSHEY_PLAIN, fontScale=2, color=(255, 0, 0),
                    thickness=2, lineType=cv2.LINE_AA)




        streamlit_image.image(frame)