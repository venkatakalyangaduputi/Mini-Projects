import cv2
import mediapipe as mp
import numpy as np
import subprocess

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
cap = cv2.VideoCapture(0)

prev_brightness = 0.5  # Initial brightness
smoothing_factor = 0.1  # Smooth transition

def set_mac_brightness(value):
    subprocess.run(["brightness", str(value)])

def draw_filled_circle(frame, center, radius, color, alpha=0.6):
    overlay = frame.copy()
    cv2.circle(overlay, center, radius, color, -1)
    return cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    h, w, _ = frame.shape  # Get frame dimensions

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            x1, y1 = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)  # Thumb
            x2, y2 = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)  # Index finger

            distance = np.linalg.norm([x2 - x1, y2 - y1])
            target_brightness = np.interp(distance, [30, 200], [0.1, 1.0])  # 10% to 100% brightness

            # Smooth brightness transition
            prev_brightness = prev_brightness * (1 - smoothing_factor) + target_brightness * smoothing_factor
            set_mac_brightness(prev_brightness)

            # Draw hand tracking markers
            cv2.circle(frame, (x1, y1), 10, (0, 255, 0), -1)
            cv2.circle(frame, (x2, y2), 10, (0, 255, 0), -1)
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

            # Draw brightness circular indicator
            center_x, center_y = 100, 100
            cv2.circle(frame, (center_x, center_y), 50, (255, 255, 255), 2)
            angle = int(prev_brightness * 360)
            for i in range(angle):
                angle_rad = np.deg2rad(i)
                x = int(center_x + 45 * np.cos(angle_rad))
                y = int(center_y + 45 * np.sin(angle_rad))
                cv2.circle(frame, (x, y), 2, (0, 255, 0), -1)

            # Draw brightness bar
            bar_x, bar_y = 50, 80
            bar_height = 200
            fill_height = int(bar_height * prev_brightness)
            cv2.rectangle(frame, (bar_x, bar_y), (bar_x + 30, bar_y + bar_height), (255, 255, 255), 2)
            cv2.rectangle(frame, (bar_x, bar_y + bar_height - fill_height), (bar_x + 30, bar_y + bar_height), (0, 255, 0), -1)

            # Draw a stylish filled circle with transparency
            frame = draw_filled_circle(frame, (center_x, center_y), 50, (0, 255, 0), 0.3)

            # Display brightness level
            cv2.putText(frame, f'Brightness: {int(prev_brightness * 100)}%', (center_x - 40, center_y + 5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    cv2.imshow('Brightness Control', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
