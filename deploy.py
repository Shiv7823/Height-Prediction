import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel  # For request validation
import pickle

# Define input data schema using Pydantic
class HeightData(BaseModel):
    father : float
    mother: float
    children: int
    childNum: int
    gender : int
    
# Initialize FastAPI app
app = FastAPI()

# Load the pre-trained model
pickle_in = open("model.pkl", "rb")  # Ensure the correct .pkl file path
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'Deployment': 'Welcome to the Height Prediction API'}

@app.post('/predict')
def predict(data: HeightData):
    # Parse input data
    data = data.dict()
    father = data['father']
    mother = data['mother']
    children = data['children']
    childNum = data['childNum']
    gender = data['gender']

    # Make prediction
    prediction = classifier.predict([[father, mother, children, childNum, gender]])

    return {
        'predicted_height': f"{prediction[0]:.2f} centimeters"
    }

# Run the app
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)
