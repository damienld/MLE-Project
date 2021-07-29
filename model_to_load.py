import pickle
from sklearn.ensemble import RandomForestClassifier

path='model_pickles'

class ModelFromFiles:
    """
    Each of the 4 models is loaded by using 2 prerecorded pickles files generated under Jupyter notebook
    model{i}.pkl
    count_vectorizer{i}.pkl
    """
    def __init__(self, model_index):#, count_vectorizer, model):
        if (model_index<1 or model_index>4):
            raise TypeError("model_index must be between 1 and 4")
        self.name= ""
        self.model_index=model_index
        self.pkl_count_vectorizer=None
        self.pkl_model=None
        self._load_from_pickles_files()

    #protected method
    def _load_from_pickles_files(self):
        with open(f'{path}/model{self.model_index}.pkl', 'rb') as handle:
            self.pkl_model = pickle.load(handle)
        with open(f'{path}/count_vectorizer{self.model_index}.pkl', 'rb') as handle:
            self.pkl_count_vectorizer = pickle.load(handle)

    def preprocess(self, text, pkl_stopwords, pkl_tokenizer):
        text = text.lower()
        tokens = pkl_tokenizer.tokenize(text)
        tokens = [t for t in tokens if t not in pkl_stopwords]
        return ' '.join(tokens)

    def predict(self, text, pkl_stopwords, pkl_tokenizer):
        X_text=[self.preprocess(text, pkl_stopwords, pkl_tokenizer)]
        X_test_cv = self.pkl_count_vectorizer.transform(X_text)
        return self.pkl_model.predict(X_test_cv)

    

