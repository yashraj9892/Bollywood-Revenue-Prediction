import pickle
import numpy as np
import sklearn

def predict(values):
    x_test= np.zeros((6,))
    for i in zip(values,range(0,len(values))):
        x_test[i[1]]=i[0]
    x_test = np.reshape(x_test,(-1,6))
    loaded_model = pickle.load(open('F:/django/box_office - Copy/predict/year_lm2.pkl', 'rb'))
    y_pred = loaded_model.predict(x_test)
    return y_pred
