"""
to install a package to a global interpreter (i.e. python 3.7..)
Palette: Create New Integrated Terminal 
"""

"""
to install a package for a specific virtual environment

1 - Create a virtual environment (use the Python Terminal at the bottom)
py -3 -m venv .mleproject_test_venv
2 - Activate it
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
.mleproject_test_venv\scripts\activate
3 - Select your new environment from the Palette:Python: Select Interpreter (might need to refresh)
4 - Install the packages
python -m pip install matplotlib
5 - pip freeze > requirements.txt 
===> requests==2.26.0
"""
import os
import requests
from requests.auth import HTTPBasicAuth
import sys
'''script paremeters:
The script will necessarily be called with 6 parameters, set them to "" if no value
1: "127.0.0.1" (ip address)
2: "8000" (port)
3: "permissions"(endpoint)
4: (sentence)
5: (model_index)
6: (username)
7: (password)
'''
if __name__ == "__main__":
#just for debugging
    api_address = '127.0.0.1'
    api_port = '8000'
    api_endpoint = "text_to_sentiment"
    test_sentence = "I am sad and disappointed and unhappy and angry"
    test_model_index = "1"
    test_username = "alice"
    test_password = "wonderland1"
else:
    api_address = sys.argv[1]
    api_port =sys.argv[2]
    api_endpoint = sys.argv[3]
    test_sentence = sys.argv[4]
    test_model_index = sys.argv[5]
    test_username = sys.argv[6]
    test_password = sys.argv[7]

#a dictionnary will contain the expected result for each set of parameters
#the key will be formatted from {endpoint}#{sentence}#{model_index}#{username}#{password}
#the value will be a tuple with (status_code, value)
dict_tests_expected_results ={
    '': (200, '1'), #test index
    'text_to_sentiment#hello#0': (403, ''),  #test bad model_index=0
    'text_to_sentiment#I am sad and disappointed and unhappy and angry#1': (200, '3')
}

r = requests.get(
    url='http://{address}:{port}/{endpoint}/{sentence}/{model}'.format(address=api_address, port=api_port, endpoint=api_endpoint
    , sentence=test_sentence, model=test_model_index)
    #,    params= dict_params_req
    , auth=HTTPBasicAuth(test_username, test_password)
)

# get request HTTP status (200, 401..)
status_code = r.status_code
response=r.json()
# get the expected tuple (status_code, score) matching the current parameters of the script from the dictionnary
expected_result = dict_tests_expected_results[api_endpoint+"#"+test_sentence+"#"+test_model_index]
    
try:
    score=response["score"]
except:
    score="error"

if status_code == expected_result[0]:
    test_status = 'SUCCESS'
else:
    test_status = 'FAILURE'

output = '''
============================
    API test
============================

request done at "/{endpoint}"
| sentence={sentence}
| model_index={model_index}
| username="{username}"
| password="{password}"

expected result = {expected_code}
actual restult = {status_code}

==>  {test_status}

'''

stroutput=(output.format(sentence=test_sentence,expected_code=expected_result[0],username=test_username,password=test_password,endpoint=api_endpoint,status_code=status_code, test_status=test_status, model_index=test_model_index))
print(stroutput)

'''
# impression dans un fichier
#if os.environ.get('LOG') == 1:
with open('/home/api_test.log', 'a') as file:
    file.write(stroutput)
    file.close() 
'''