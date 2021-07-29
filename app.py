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
5 - pip freeze > requirements.txt
"""
import uvicorn
from fastapi import Depends, FastAPI, params, HTTPException, status
from pydantic import BaseModel
from model_to_load import ModelFromFiles
import nltk
import pickle
from nltk.tokenize import NLTKWordTokenizer
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials

path='model_pickles'
app = FastAPI()

#load pickles files pre recorded under Jupyter notebook for nltk english stopwords and nltkwordtokenizer
with open(f'{path}/stopwords.pkl', 'rb') as handle:
    pkl_stopwords = pickle.load(handle)
with open(f'{path}/NLTKWordTokenizer.pkl', 'rb') as handle:
    pkl_tokenizer = pickle.load(handle)

#load all 4 models (1=All Branch, 2=HK, 3=California, 4=Paris)
lst_models = [ModelFromFiles(i) for i in range(1, 5)]
ypred=(lst_models[0].predict("I am sad and disappointed and unhappy and angry", pkl_stopwords, pkl_tokenizer))
print(ypred)

#authentication following https://testdriven.io/blog/moving-from-flask-to-fastapi/
dict_usernames_passwords= {
    'alice': 'wonderland',
    'bob': 'builder',
    'clementine': 'mandarine'
}
security = HTTPBasic()
def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):   
    """
    Retrieve the current HTTPBasicCredentials (username/password)
    And compare with the existing list of key/values in dict_usernames_passwords
    """
    try:
        #compare_digest permits to prevent timing attacks
        correct_password = secrets.compare_digest(credentials.password, dict_usernames_passwords[credentials.username])
    except:
        correct_password = False
    if not (correct_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return credentials.username

@app.get("/get_username")
def get_username(username: str = Depends(get_current_username)):
    return {"username": username}

@app.get("/")
async def index():
    return {'score':'1'}

@app.get("/text_to_sentiment/{text}/{model_index}")
async def text_to_sentiment(text: str, model_index: int, username: str = Depends(get_current_username)):
    """
    Returns the sentiment score
    TEST
    http://localhost:8000/text_to_sentiment/hello world/1

    Parameters
    ----------
    text: str
        The text to analyse
    model_index: int between 1 and 4
        Index of the model to use 
        1=All Branch, 2=HK, 3=California, 4=Paris
    Returns
    -------
    The prediction score matching the given "text" and using the specific model (as per "model_index")
    401 if the user is not authenticated
    TypeError if model_index is incorrect
    """
    if (model_index<1 or model_index>4):
            raise TypeError("model_index must be between 1 and 4")
    model = lst_models[model_index-1]
    ypred=(model.predict("I am sad and disappointed and unhappy and angry", pkl_stopwords, pkl_tokenizer))
    return {"score":str(ypred)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
in Visual Studio Code, you can:

Go to the "Debug" panel.
"Add configuration...".
Select "Python"
Run the debugger with the option "Python: Current File (Integrated Terminal)".
"""