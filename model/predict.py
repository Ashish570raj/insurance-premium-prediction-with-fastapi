
import pandas as pd
import pickle

with open ('model/model.pkl','rb') as f:
    model= pickle.load(f)
    
# generally from mlflow
MODEL_VERSION = "1.0.0"     #just manually taken

# get class labels from model(importan for maching probabiliies to class names)
class_labels= model.classes_.tolist()

def predict_output(user_input:dict):
    
    df= pd.DataFrame([user_input])
    
    #predicting the class
    predicted_class= model.predict(df)[0]
    
    # ge the probability for all classes
    probbabilities= model.predict_proba(df)[0]
    confidence=max(probbabilities)
    
    # create maping:{class_name:probability}
    class_probs = dict(zip(class_labels,map(lambda p:round(p,4),probbabilities)))
    
    return{
        'Predicted_category': predicted_class,
        'confidence':round(confidence,4),
        'class_probabilities': class_probs
    }   