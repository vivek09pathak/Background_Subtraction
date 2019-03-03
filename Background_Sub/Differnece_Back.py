import cv2
import numpy as np

cap = cv2.VideoCapture('check.mp4')

ret, first_frame = cap.read()

first_gray = cv2.cvtColor(first_frame,cv2.COLOR_BGR2GRAY)

first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)
count = 0

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    difference = cv2.absdiff(first_gray,gray)

    # cv2.imshow("First Frame",first_frame)
    # cv2.imshow("Frame",frame)

    if count == 0:
        # cv2.imshow("diffe",difference)
        count = 1
        prev_gray = first_gray
    elif count % 10 == 0:
        second_gray = gray
        diff2 = cv2.absdiff(second_gray,prev_gray)
        # TO check if two frames are still or same then it will print Not a car chase scene please uncomment below code and comment above
        #diff2 = cv2.absdiff(gray,gray)

        # print(first_gray)
        # print("---------------------------------------")
        # print(gray)
        # print("---------------------------------------")
        # print(diff2)


        # print(cv2.countNonZero(diff2))

        if cv2.countNonZero(diff2) != 0:
            print("Chase Scene")
            cv2.putText(diff2, "Chase Scene", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), lineType=cv2.LINE_AA )
        else:
            print("Not A Chase Scene")
        cv2.imshow("diff2", diff2)
        prev_gray = gray
    count += 1

    key = cv2.waitKey(33)

    if key == 27:
        break

cap.release()
cap.destroyAllWindows()
