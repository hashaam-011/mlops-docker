import joblib
from flask import Flask, request, jsonify

# Load trained model
model = joblib.load(r'C:\Users\dell\OneDrive\Desktop\Task\Copy_of_SentimentBert.ipynb')
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the request
    data = request.json

    # Perform preprocessing if necessary

    # Make predictions using the loaded model
    predictions = model.predict(data)

    # Return predictions as a JSON response
    return jsonify({'predictions': predictions})

if __name__ == '__main__':
    app.run(debug=True)
