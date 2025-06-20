# L-Flask: Machine Learning Image Classifier

L-Flask is a simple web application that demonstrates how to deploy a machine learning model using the Flask web framework. Users can upload an image, and the application will return a prediction of what the image contains using a pre-trained image classification model.

### About This Project

This project was created by following the video tutorial **"Deploy Machine Learning Model with Flask"**. The goal was to understand the fundamentals of integrating a Keras/TensorFlow model into a web backend to serve predictions to a user.

You can watch the full tutorial here: **https://youtu.be/0nr6TPKlrN0**

## Features

-   **Web Interface**: A clean and simple UI for uploading images.
-   **Image Prediction**: Uses the pre-trained `VGG16` model to classify uploaded images.
-   **Dynamic Results**: Displays the top predicted class and its confidence score on the web page.

## Technologies Used

-   **Backend**: Python, Flask
-   **Machine Learning**: TensorFlow, Keras
-   **Frontend**: HTML, Bootstrap (for styling)

## Setup and Usage

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/al-Jurjani/L-Flask.git
    cd L-Flask
    ```

2.  **Create and activate a virtual environment (recommended):**
    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the required dependencies:**
    This project requires Flask and TensorFlow.
    ```bash
    pip install Flask tensorflow
    ```
    *(Note: Keras is included with modern TensorFlow installations.)*

4.  **Run the Flask application:**
    ```bash
    python app.py
    ```

5.  **Open your browser:**
    Navigate to `http://127.0.0.1:2100`. You should now be able to upload an image and get a prediction!
