import pickle
from sklearn.ensemble import RandomForestClassifier
from enum import IntEnum

path='model_pickles'
model_scores=[0.61,0.48,0.65,0.45]

#ENUM https://docs.python.org/3/library/enum.html
class EnumModel(IntEnum):
    AllBranch = 1
    HK = 2
    California = 3
    Paris = 4 

class ModelFromFiles:
    """
    Each of the 4 models is loaded by using 2 prerecorded pickles files generated under Jupyter notebook
    model{i}.pkl
    count_vectorizer{i}.pkl
    """
    @staticmethod
    def load_all_models_to_list():
        """
        Load all models
        Returns a list of ModelFromFiles
        """
        return [ModelFromFiles(enum_model) for enum_model in (EnumModel)]

    def __init__(self, enum_model: EnumModel):#, count_vectorizer, model):
        #if (model_index<1 or model_index>4):
        #    raise TypeError("model_index must be between 1 and 4")
        self.model_name= enum_model.name
        self.model_index=enum_model.value
        self.model_score=model_scores[enum_model.value-1]
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

    

