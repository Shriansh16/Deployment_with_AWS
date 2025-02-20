from typing import Union   # Union is used to specify that a parameter can be of multiple types

from fastapi import FastAPI

app = FastAPI()

# define a route that returns a dictionary with a key "Hello" and a value "World"
@app.get("/")
def read_root():
    return {"Hello": "World"}

# define a route that returns a dictionary with a key "item_id" and a value of the item_id passed in the URL
@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

# define a route that returns a dictionary with a key "text" and a value of the text passed in the URL
# and a key "sentiment" with a value "positive"
@app.get("/get_sentiment/{text}")
def get_sentiment(text: str, user_id: Union[str, None] = None):
    return {"text": text, 
            "sentiment": "positive", 
            "user_id": user_id}

@app.get("/get_sentiment_v2/{text}/{ip}")  # all the written here are compulsory to pass with url
def get_sentiment_v2(text: str, ip: str, user_id: Union[str, None] = None):  #here user id is not compulsory
    return {"ip": ip,
            "text": text, 
            "sentiment": "positive", 
            "user_id": user_id}

# lets explore post request
# here you do not need to pass the data in the url, you can pass the data in data payload
@app.post("/get_twitter_sentiment")
def get_twitter_sentiment(text: str, ip: str, user_id: Union[str, None] = None):
    return {"ip": ip,
            "text": text, 
            "sentiment": "normal", 
            "user_id": user_id}

    # http://127.0.0.1:8000/docs

@app.post("/get_twitter_sentiment_v2")
async def get_twitter_sentiment_v2(request: Request):
    data = await request.json()

    text:str = data.get('text')
    ip = data.get('ip')
    user_id = data.get('user_id')

    return {"ip": ip,
            "text": text, 
            "sentiment": "normal", 
            "user_id": user_id}

    """🔹 How It Works
async def → Makes the function asynchronous.
await request.json() → This tells Python "pause here, but continue handling other requests."
Other API calls can still be processed while waiting for JSON data.

 Without async and await
If you remove async and await, the server pauses until it reads the JSON data, blocking other users."""