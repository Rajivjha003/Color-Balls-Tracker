# Importing libraries
import cv2 
import numpy as np

# defining the color ranges for the balls in HSV color space
color_ranges = {
    'white': ([50, 10, 70], [70, 30, 90]),
    'yellow': ([20, 100, 100], [30, 255, 255]),
    'green': ([40, 50, 50], [90, 255, 100]),
    'pink': ([0, 50, 50], [10, 255, 200])
}

# defining the coordinates of the quadrants
quadrants = {
    1: ((320, 240), (640, 480)),
    2: ((0, 240), (320, 480)),
    3: ((0, 0), (320, 240)),
    4: ((320, 0), (640, 240))
}

# Creating function to track balls
def track_balls(video_path, output_path):
    cap = cv2.VideoCapture(video_path)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_path, fourcc, 10.0, (640, 480))

    # Opening the text file for writing the event data
    with open('output.txt', 'w') as f:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Converting the frame to HSV color space
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            for color, (lower, upper) in color_ranges.items():
                # Created a mask for the current color
                mask_color = cv2.inRange(hsv, np.array(lower), np.array(upper))
                # Perform morphological operations to remove noise
                mask_color = cv2.morphologyEx(mask_color, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
                mask_color = cv2.morphologyEx(mask_color, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)

                # Find the contours in the mask
                contours_ball, _ = cv2.findContours(mask_color, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

                # Loop over the contours
                for contour_ball in contours_ball:
                    
                    if cv2.contourArea(contour_ball) > 1000: # ignored small contours
                        # minimum enclosing circle of the contour
                        (x, y), radius = cv2.minEnclosingCircle(contour_ball)
                        center = (int(x), int(y))

                        # make circle around the ball and label it with the color
                        frame = cv2.circle(frame, center, int(radius), (255, 0, 0), 2)
                        cv2.putText(frame, color, (center[0] - 20, center[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

                        # Checking which quadrant the ball is in
                        for quadrant, (top_left, bottom_right) in quadrants.items():
                            if top_left[0] <= center[0] <= bottom_right[0] and top_left[1] <= center[1] <= bottom_right[1]:
                                # the event data to the text file
                                f.write(f'{cap.get(cv2.CAP_PROP_POS_MSEC)/1000}, {quadrant}, {color}, Entry\n')

            out.write(frame)
            cv2.imshow('frame', cv2.resize(frame, (640, 480)))

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

# Call the function with the input and output video paths
track_balls("E:\Ball Tracking\Videos\AI Assignment video.mp4", 'output_video1.avi')
