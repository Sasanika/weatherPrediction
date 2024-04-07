from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# load the model
model = pickle.load(open('savemodel.sav', 'rb'))

# Mapping of class numbers to class names
class_mapping = {
    2: 'Cloudy Skies',
    4: 'Foggy Day',
    0: 'Breezy Day',
    1: 'Clear Skies',
    5: 'Humid Day',
    7: 'Windy Day',
    3: 'Dry Day',
    6: 'Rainy Day'
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract input features from the form
        features = [float(request.form[feature]) for feature in request.form]
        # Make prediction
        result = model.predict([features])[0]
        # Map the predicted class to its name
        result_name = class_mapping[result]
        # Return the predicted class name as a string
        return result_name

if __name__ == '__main__':
    app.run(debug=True)
