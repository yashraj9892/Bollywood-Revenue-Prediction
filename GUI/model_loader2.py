import pickle
import numpy as np
import sklearn

def predict(values):
    x_test=np.asarray(values,dtype=int)
    x_test=x_test.reshape(1,6)
    loaded_model = pickle.load(open('F:/project2/Newfolder/year_lm2.pkl', 'rb'))
    y_pred = loaded_model.predict(x_test)
    return y_pred
