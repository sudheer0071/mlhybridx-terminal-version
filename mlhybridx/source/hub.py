from sklearn.model_selection import train_test_split 
from source.check_extention import check_file
from source.algorithm import ols, multiple, GDR
from source.scores import SE
from source.split import split_data
from source.predict import predict_olr, perdict_multiple, predict_gdr
# from default import multiple_data
from source.train import train_data
# from main_class import Hybrid
from source.default import By_default 
from source.Visualization import count_plot,box_plot