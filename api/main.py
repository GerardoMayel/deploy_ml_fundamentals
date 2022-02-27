from fastapi import FastAPI
import app.models as models
import app.views as views

app = FastAPI(docs_url='/')


@app.post('/v1/prediction')
def make_model_prediction(request: models.PredictionRequest):
    return models.PredictionResponse(worldwide_gross=views.get_prediction(request))
