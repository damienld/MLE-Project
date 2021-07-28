import pickle
from model_to_load import ModelFromFiles

path='model_pickles'
lst_models = [ModelFromFiles(i) for i in range(1, 5)]
#load pickles files pre recorded under Jupyter notebook for nltk english stopwords and nltkwordtokenizer
with open(f'{path}/stopwords.pkl', 'rb') as handle:
    pkl_stopwords = pickle.load(handle)
with open(f'{path}/NLTKWordTokenizer.pkl', 'rb') as handle:
    pkl_tokenizer = pickle.load(handle)

ypred=(lst_models[0].predict("I am sad and disappointed and unhappy and angry", pkl_stopwords, pkl_tokenizer))
print(ypred)