## Language & Emotion Detection Based On Text

  This project is a language and emotion detection model using Flask. It predicts the language and emotion of the given text.

- Getting started
 
  These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
- Python 3.6+
- Flask
- Scikit-learn
- Pandas
- Pickle


# Installation
1. Clone the repo:
   ```sh
   git clone https://github.com/SinestreaSwl/Language-Detection.git
   cd Language-Detection
   ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the Flask app:
   ```sh
   python app.py
   ```

2. Open your browser and go to `http://127.0.0.1:5000/`.

## Prediction API

You can use the `/predict` endpoint to get predictions. Send a POST request with a JSON body containing the text to be analyzed, for example:
```json
{
    "Text": "I am so happy today!"
}
