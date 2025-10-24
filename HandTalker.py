import cv2
import mediapipe as mp
import numpy as np
import pickle
import string
from difflib import get_close_matches

# Load trained gesture recognition model
model_dict = pickle.load(open('gesture_model.pkl', 'rb'))
model = model_dict['model']
labels_dict = model_dict['labels']

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.6)

# Basic correction dictionary (can be expanded)
CORRECTION_DICT = {
    'helo': 'hello',
    'thnak': 'thank',
    'plase': 'please',
    'goobye': 'goodbye',
    'pleas': 'please'
}

def autocorrect(word, known_words):
    word = word.lower()
    if word in CORRECTION_DICT:
        return CORRECTION_DICT[word]
    matches = get_close_matches(word, known_words, n=1, cutoff=0.8)
    return matches[0] if matches else word

def process_frame(image):
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    if not results.multi_hand_landmarks:
        return image, None

    for hand_landmarks in results.multi_hand_landmarks:
        data_aux = []
        for lm in hand_landmarks.landmark:
            data_aux.extend([lm.x, lm.y, lm.z])
        mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        prediction = model.predict([np.asarray(data_aux)])
        pred_text = labels_dict[int(prediction[0])]
        return image, pred_text

    return image, None


def main():
    cap = cv2.VideoCapture(0)
    sentence = ''

    known_words = list(labels_dict.values())

    print("Press 'c' to clear text, 'q' to quit.\n")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame, label = process_frame(frame)

        if label:
            corrected = autocorrect(label, known_words)
            if sentence.endswith(' ') or not sentence:
                sentence += corrected + ' '
            elif corrected != sentence.split()[-1]:
                sentence += corrected + ' '

        cv2.putText(frame, f"Text: {sentence}", (10, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow("Sign Language Translator", frame)

        key = cv2.waitKey(10) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('c'):
            sentence = ''

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
