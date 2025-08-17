
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from Schema.UserInput import UserInput
from model.predict import predict_output,model,MODEL_VERSION
from Schema.predicion_response import PredictionResponse
app=FastAPI()

#human redable
@app.get('/')
def home():
    return {'messsage':'Insurance Premium Prediction API'}

#machine readable
@app.get('/health')
def health_check():
    return{
        'status':'OK',
        'version': MODEL_VERSION,
        "model_loaded": model is not None
    }

@app.post('/predict',response_model=PredictionResponse)
def predic_premium(data: UserInput):
    
    user_input = {
        'bmi': data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tire': data.city_tire,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    
    try:
        
        prediction= predict_output(user_input)
        # return prediction
        return JSONResponse(status_code=200, content={'response':prediction})

    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))