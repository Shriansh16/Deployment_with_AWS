import warnings
warnings.filterwarnings('ignore')

from scripts.data_model import NLPDataInput, NLPDataOutput
from scripts import s3

from fastapi import FastAPI
from fastapi import Request
import uvicorn
import os
import time

import torch
from transformers import pipeline

app = FastAPI()

device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

####### Download ML Models ##########

model_name = 'tinybert-sentiment-analysis/'
local_path = 'ml-models/'+model_name
if not os.path.isdir(local_path):
    s3.download_dir(local_path, model_name)
sentiment_model = pipeline('text-classification', model=local_path, device=device)

######## Download ENDS  #############


@app.get("/")
def read_root():
    return "Hello! I am up!!!"

@app.post("/api/v1/sentiment_analysis")
def sentiment_analysis(data: NLPDataInput):
    start = time.time()
    output = sentiment_model(data.text)
    end = time.time()
    prediction_time = int((end-start)*1000)

    labels = [x['label'] for x in output]
    scores = [x['score'] for x in output]

    output = NLPDataOutput(model_name="tinybert-sentiment-analysis",
                           text = data.text,
                           labels=labels,
                           scores = scores,
                           prediction_time=prediction_time)

    return output





if __name__=="__main__":
    uvicorn.run(app="app:app", port=8502, reload=True, host="127.0.0.1")


#command to run the app: uvicorn app:app --host 127.0.0.1 --port 8502 --reload