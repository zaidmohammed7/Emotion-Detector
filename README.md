# Emotion Detection Web Application

## Project Overview

In this project, I developed an **Emotion Detection** web application that analyzes customer feedback in text format. The application processes the feedback, identifies the emotions (like joy, sadness, anger, disgust, and fear), and provides a response indicating the dominant emotion. This type of AI-based system is valuable for understanding user sentiments in applications such as chatbots, recommendation systems, and customer support systems.

---

### Key Features:
- Emotion analysis based on customer feedback using **Watson NLP** library.
- Return output in a structured format (emotion scores and dominant emotion).
- Web deployment using **Flask** to make the application accessible through a user-friendly interface.
- Error handling to manage invalid inputs.
- Static code analysis for PEP 8 compliance.

## Important Notice:
The external URL used for emotion detection in this project is currently disabled, as it was part of the course. Therefore, the service that was previously available at the following URL: https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict
is no longer accessible.

### What You Can Do:
- Feel free to explore and adapt the code to fit other emotion detection tools or APIs.
- Change the URL located in the EmotionDetection/emotion_detection.py file to an alternate service

---

## Skills Demonstrated

- **Emotion Detection:** Implemented an emotion detection system using the Watson NLP API to process and analyze text input.
- **Flask Web Application Development:** Built a simple Flask web application to serve the emotion detection functionality.
- **Error Handling:** Incorporated error handling in the Python function to manage edge cases (like blank or invalid inputs).
- **Unit Testing:** Wrote unit tests to validate the functionality of the emotion detection application.
- **Static Code Analysis:** Ran static code analysis using **PyLint** to ensure compliance with best coding practices.
- **GitHub & Version Control:** Managed project development and version control using Git and GitHub, ensuring smooth collaboration and easy code management.

---

## Project Setup and Installation

### Clone the Repository
To set up this project locally, follow these steps:

1. **Clone this repository:**

    ```bash
    git clone https://github.com/zaidmohammed7/Emotion-Detector.git
    cd Emotion-Detector
    ```

2. **Install required dependencies:**

    This project requires Python 3.11 and the following packages:

    ```bash
    pip install flask
    pip install requests
    ```

3. **Run the Application:**

    To start the Flask web application locally, run:

    ```bash
    python server.py
    ```

    The application will be accessible at `http://localhost:5000`.

### API Endpoints
The primary endpoint for the application is:

- `POST /emotion`: Accepts a `text` parameter in the request body and returns a JSON response containing the emotion analysis results.

### Example Request

- **Endpoint:** `/emotion`
- **Method:** `POST`
- **Request Body:**
    ```json
    {
        "text": "I love my new phone!"
    }
    ```

- **Response:**
    ```json
    {
        "anger": 0.002,
        "disgust": 0.003,
        "fear": 0.004,
        "joy": 0.989,
        "sadness": 0.002,
        "dominant_emotion": "joy"
    }
    ```

## Acknowledgements
- The course *"Developing AI Applications with Python and Flask"*, offered by **IBM** through **Coursera**.
  You can find more details about the course [here](https://www.coursera.org/learn/python-project-for-ai-application-development).
- Initial project template was forked from "https://github.com/ibm-developer-skills-network/oaqjp-final-project-emb-ai.git"
- Special thanks to the **IBM Developer Skills Network** for providing the foundational project structure and guidance.

---
