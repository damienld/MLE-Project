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
"""
DOCKER set up in VScode
https://towardsdatascience.com/the-nice-way-to-use-docker-with-vscode-f475c49aab1b
"""
"""
AZURE FIRST deployment
https://docs.microsoft.com/en-us/azure/developer/python/tutorial-deploy-containers-01
0 - Launch Docker Desktop
1 - Publish your docker image to Azure Registry: https://code.visualstudio.com/docs/containers/tutorial-django-push-to-registry
- CTR SHIFT P >> Docker: Push
2 - You should see your container under Docker left tab > Registries > Azure > MyAzuresubscription > MyRegistry > myimagename
Right click on the deeper level > Deploy Image to Azure App Service ...
3 - définir WEBSITES_PORT, basculez vers l’explorateur Azure : App Service
, développez le nœud de votre nouveau service d’application (actualisez si nécessaire)
, puis cliquez avec le bouton droit sur Paramètres de l’application et sélectionnez Ajouter un nouveau paramètre. 
Quand vous y êtes invité, entrez WEBSITES_PORT comme clé et le numéro de port(expl: 8000) comme valeur.

AZURE update deployment

https://disneyreviews.azurewebsites.net/docs#/default/text_to_sentiment_text_to_sentiment__text___model_index__get
"""
from pydantic.types import Json
import uvicorn
from fastapi import Depends, FastAPI, params, HTTPException, status, Query
from pydantic import BaseModel
from model_to_load import ModelFromFiles, EnumModel
import nltk
import pickle
from nltk.tokenize import NLTKWordTokenizer
import secrets
from fastapi.security import HTTPBasic, HTTPBasicCredentials

path='model_pickles'
app = FastAPI()

#LOAD pickles files pre recorded under Jupyter notebook for nltk english stopwords and nltkwordtokenizer
with open(f'{path}/stopwords.pkl', 'rb') as handle:
    pkl_stopwords = pickle.load(handle)
with open(f'{path}/NLTKWordTokenizer.pkl', 'rb') as handle:
    pkl_tokenizer = pickle.load(handle)

#LOAD all 4 models (1=All Branch, 2=HK, 3=California, 4=Paris)
lst_models = ModelFromFiles.load_all_models_to_list()

dict_usernames_passwords= {
    'alice': 'wonderland',
    'bob': 'builder',
    'clementine': 'mandarine'
}

#AUTHENTICATION following https://testdriven.io/blog/moving-from-flask-to-fastapi/
"""
FastAPI natively supports a number of security and authentication tools via the fastapi.security package. 
With a few lines of code, you can add basic HTTP authentication to your application
"""
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
async def get_username(username: str = Depends(get_current_username)):
    """
    Used to check the authentication is correct
    Returns the **username** of the currently authenticated user
    """
    return {"username": username}

#INDEX()
@app.get("/")
async def index():
    return {'score':'1'}

#MODELS PERFS
@app.get("/get_performance")
async def get_performance(modelindex: EnumModel):
    """
    Returns the ***name*** and the **score** of the selected model
    """
    model_index = modelindex.value
    model = lst_models[model_index-1]
    return {"model": model.model_name, "score": model.model_score}

#TEXT_TO_SENTIMENT()
class SentimentRequest(BaseModel):
    text: str
    model: EnumModel

@app.post("/text_to_sentiment/")
async def text_to_sentiment(request: SentimentRequest 
#text: str, model: int = Query(..., gt=1, le=4)
, username: str = Depends(get_current_username)):
    """
    Test
    ----
    http://localhost:8000/text_to_sentiment/hello world/1

    Parameters
    ----------
    - **text**: str
        The text to analyse
    - **model_index**: int between 1 and 4
        Index of the model to use 
        1=All Branch, 2=HK, 3=California, 4=Paris

    Returns
    -------
    Returns the prediction score matching the given "text" and using the specific model (as per "model_index")
    401 if the user is not authenticated
    TypeError if model_index is incorrect
    """
    #value directly checked by Query() in the definition of the parameters(above line)
    #but still need to manage the exception
    model_index = request.model.value
    text = request.text
    #not needed anymore with Enum as the value can't be out of range
    #if (model_index not in [1,2,3,4]):
    #    raise HTTPException(status_code=404, detail="model_index must be an integer between 1 and 4")
    model = lst_models[model_index-1]
    ypred=(model.predict(text, pkl_stopwords, pkl_tokenizer))
    return {"score":str(ypred)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

"""
VSCODE DEBUGGING
in Visual Studio Code, you can:

Go to the "Debug" panel.
"Add configuration...".
Select "Python"
Run the debugger with the option "Python: Current File (Integrated Terminal)".
"""