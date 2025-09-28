import cv2
import mediapipe as mp
import serial
import time
from collections import deque

class HandTracker:
    def __init__(self, com_port='COM4', baud_rate=9600):
        # Serial connection setup
        try:
            self.arduino = serial.Serial(com_port, baud_rate)
            time.sleep(2)
            print(f"Successfully connected to Arduino on {com_port}")
        except serial.SerialException as e:
            print(f"Error connecting to Arduino: {e}")
            self.arduino = None

        # Mediapipe setup
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        self.mp_draw = mp.solutions.drawing_utils

        # Camera setup
        self.cap = cv2.VideoCapture(0)
        if not self.cap.isOpened():
            print("Error: Could not open video stream.")
            return
        self.cap.set(3, 640)
        self.cap.set(4, 480)

        # History buffer for stability
        self.history = deque(maxlen=10)
        self.tips = [4, 8, 12, 16, 20]  # finger tip landmarks

    def count_fingers(self, landmarks):
        count = 0
        # Thumb
        if landmarks[self.tips[0]].x < landmarks[self.tips[0]-1].x:
            count += 1

        # Other 4 fingers
        for id in range(1, 5):
            knuckle_y = landmarks[self.tips[id]-2].y
            tip_y = landmarks[self.tips[id]].y
            if tip_y < knuckle_y:
                count += 1
        return count

    def run(self):
        while self.cap.isOpened():
            ret, img = self.cap.read()
            if not ret:
                break

            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            results = self.hands.process(img_rgb)
            stable_count = 0

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    finger_count = self.count_fingers(hand_landmarks.landmark)
                    self.history.append(finger_count)

                    # Draw landmarks
                    self.mp_draw.draw_landmarks(img, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)

            # Smooth result
            if self.history:
                stable_count = max(set(self.history), key=self.history.count)
            else:
                stable_count = 0

            # Send to Arduino
            if self.arduino:
                try:
                    self.arduino.write(str(stable_count).encode())
                    print(f"Fingers: {stable_count}")
                except serial.SerialException:
                    print("⚠️ Disconnected from Arduino.")
                    self.arduino.close()
                    self.arduino = None

            # Display result
            cv2.putText(img, f"Fingers: {stable_count}", (30, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            cv2.imshow("Hand Tracking", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
        if self.arduino:
            self.arduino.close()

if __name__ == '__main__':
    tracker = HandTracker(com_port='COM4')  # Change COM4 if needed
    tracker.run()
