"""
to install a package to a global interpreter (i.e. python 3.7..)
Palette: Create New Integrated Terminal 
"""

"""
to install a package for a specific virtual environment

1 - Create a virtual environment (use the Python Terminal at the bottom)
py -3 -m venv .mleproject_venv
2 - Activate it
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.mleproject_venv\scripts\activate
3 - Select your new environment from the Palette:Python: Select Interpreter (might need to refresh)
4 - Install the packages
python -m pip install matplotlib
"""
import uvicorn
from fastapi import FastAPI, params
from pydantic import BaseModel
from model_to_load import ModelFromFiles
import nltk
#from nltk.corpus import stopwords
import pickle
from nltk.tokenize import NLTKWordTokenizer
path='model_pickles'

#load pickles files pre recorded under Jupyter notebook for nltk english stopwords and nltkwordtokenizer
with open(f'{path}/stopwords.pkl', 'rb') as handle:
    pkl_stopwords = pickle.load(handle)
with open(f'{path}/NLTKWordTokenizer.pkl', 'rb') as handle:
    pkl_tokenizer = pickle.load(handle)

#load all 4 models (1=All Branch, 2=HK, 3=California, 4=Paris)
lst_models = [ModelFromFiles(i) for i in range(1, 5)]
ypred=(lst_models[0].predict("I am sad and disappointed and unhappy and angry", pkl_stopwords, pkl_tokenizer))
print(ypred)

app = FastAPI()

@app.get("/")
async def index():
    return {'1'}


@app.get("/text_to_sentiment/{text}/{model_index}")
async def text_to_sentiment(text: str="I am sad and disappointed and unhappy and angry", model_index: int=1):
    """
    Returns the sentiment score
    TEST
    http://localhost:8000/sentiment/Quinlan/5210/VADER%20is%20smart,%20handsome,%20and%20funny! => compound=0.8439

    Parameters
    ----------
    username : str
        The user name
    pwd : str
        The password for this username
    text: str
        The text to analyse
    model_index: int
        Index of the model to use (1 to 4)
        1=All Branch, 2=HK, 3=California, 4=Paris
    Returns
    -------
    a sentiment score
    """
    if (model_index<1 or model_index>4):
            raise TypeError("model_index must be between 1 and 4")
    model = lst_models[model_index-1]
    ypred=(model.predict("I am sad and disappointed and unhappy and angry", pkl_stopwords, pkl_tokenizer))
    return {str(ypred)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
in Visual Studio Code, you can:

Go to the "Debug" panel.
"Add configuration...".
Select "Python"
Run the debugger with the option "Python: Current File (Integrated Terminal)".
"""