from project import train_data, lr_model, prediction
from source.hybrid_class import EasyRegresspr
import pytest

new = EasyRegresspr('wine.csv')


def main():
    test_training_data()
    test_models()
    test_invalid_params()
    test_prediction()


def test_training_data(): 
    assert train_data('0.4') ==  True
    


def test_models(): 
    assert lr_model('s') == True

def test_invalid_params():
    assert lr_model('zx') == "You Entered wrong model name"

def test_prediction():
    assert prediction('s') == True
    assert prediction('zx') == 'You Entered wrong model_name' 
if __name__ == "__main__":
    main()
 
