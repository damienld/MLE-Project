from model_to_load import ModelFromFiles

def test_load():
    lst_models = ModelFromFiles.load_all_models_to_list()
    assert len(lst_models) == 4
