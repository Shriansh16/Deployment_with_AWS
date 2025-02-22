# accept the input params/data payload
# output the score, class, latency

from pydantic import BaseModel
from pydantic import EmailStr, HttpUrl

class NLPDataInput(BaseModel):
    """
    NLPDataInput is a child class.
    BaseModel is the parent class from the Pydantic library.
     Why Are We Using BaseModel?
BaseModel provides powerful features for:

✅ Data validation (Checks if the data type matches what you specified).
✅ Data parsing (Converts input data into the right format).
✅ Automatic error handling (Throws clear errors for invalid inputs).
✅ Serialization (Converts objects to JSON or dictionaries easily).

When you inherit from BaseModel, your class automatically gets all these features without writing extra code.
    """
    text: list[str]      # A list of text strings for NLP tasks
    user_id: EmailStr    # User ID validated as an email address

class ImageDataInput(BaseModel):
    url: list[HttpUrl]   # A list of URLs pointing to images
    user_id: EmailStr

class NLPDataOutput(BaseModel):
    model_name: str     # Name of the model used for predictions
    text: list[str]     # Original input texts
    labels: list[str]   # Predicted classes/labels for each input text
    scores: list[float]  # Confidence scores for each prediction
    prediction_time: int  # Time taken for prediction in milliseconds

class ImageDataOutput(BaseModel):
    model_name: str
    url: list[HttpUrl]
    labels: list[str]
    scores: list[float]
    prediction_time: int


"""
Pydantic is used for data validation and data parsing. It ensures that the data passed into your models has the right type and structure.

For example:

If you expect an email (EmailStr), Pydantic will validate whether the provided input is a valid email.
If you expect a URL (HttpUrl), Pydantic ensures the input is a properly formatted URL.
If the input doesn't match the required type, it will automatically raise an error.

This Python code defines data models using Pydantic, a library used for data validation and parsing in Python. 
These models ensure that input and output data conform to specific types and structures.
"""

"""
User Input (JSON) 
   |
   V
Pydantic Input Model (Validation & Parsing)
   |
   V
Processing (ML Model Prediction)
   |
   V
Pydantic Output Model (Validation & Structuring)
   |
   V
Response (JSON)

"""