from model_to_load import ModelFromFiles

def test_load():
    list_models = ModelFromFiles.load_all_models_to_list()
    assert len(list_models) == 4
