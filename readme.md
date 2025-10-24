# HandTalker

>  **Real-Time Sign Language to Text Converter with Auto-Correction**

## Project Description
HandTalker is an intelligent, real-time sign language translation app written in Python. By leveraging computer vision and machine learning, it captures hand and finger movements from a standard webcam, recognizes American Sign Language (ASL) gestures, and instantly translates them into readable text. The system features advanced auto-correction to correct small recognition errors, improving communication efficiency and usability for the speech-impaired and the wider community. HandTalker is built for accessibility, scalability, and ease of use.​

## Features
- Real-time detection of hand and finger gestures using MediaPipe and OpenCV.

- Recognizes and translates signs into English text output.

- Intelligent auto-correction for common misclassifications.

- User-friendly interface suitable for all experience levels.

## Installation
- 1 Clone this repository:

      git clone https://github.com/your-username/handtalker.git
  
      cd handtalker
    
- 2 Install requirements:

      pip install -r requirements.txt
  
> (Requirements: opencv-python, mediapipe, numpy, scikit-learn, difflib )


- 3 Download or train the hand gestures model:

   - Place your trained gesture_model.pkl in the project root, or follow the Model Training Guide.

## Usage Guide
- 1 Run the main program:

      python handtalker.py

- 2 Allow webcam access when prompted.

- 3 Make ASL hand signs in front of your camera. Detected text will display live.

- 4 Controls:

  - Press `q` to quit the program.

  - Press `c` to clear the text area and start a new sentence.

- 5 Auto-correction is applied to each detected sign for the most accurate results ( *uncompleted* ).

## License
- This project is licensed under the MIT License.


## Visitor Counter

<p align="center">
  <img src="https://github.com/el-guemra-br.png" alt="Visitor Count" width="130" />
  <br>
  <img src="https://visitor-badge.laobi.icu/badge?page_id=el-guemra-br.HandTalker&" />
  <br>
  <sub>
    Thank you for stopping by! Your visit is appreciated. 
  </sub>
</p>
 
  
