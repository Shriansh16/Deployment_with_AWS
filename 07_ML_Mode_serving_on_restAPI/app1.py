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
    output = sentiment_model(data.text)
    return output





if __name__=="__main__":
    uvicorn.run(app="app:app", port=8502, reload=True, host="0.0.0.0")