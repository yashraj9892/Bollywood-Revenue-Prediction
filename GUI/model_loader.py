import pickle
import numpy as np
import sklearn

def predict(values):
    x_test=np.asarray(values,dtype=int)
    x_test=x_test.reshape(1,1796)
    y_pred=[]
    loaded_model = pickle.load(open('F:/project2/New folder/year_svm.pkl', 'rb'))
    y_pred.append(loaded_model.predict(x_test))
    loaded_model = pickle.load(open('F:/project2/New folder/year_naivebayes.pkl', 'rb'))
    y_pred.append(loaded_model.predict(x_test))
    loaded_model = pickle.load(open('F:/project2/New folder/year_knn.pkl', 'rb'))
    y_pred.append(loaded_model.predict(x_test))
    loaded_model = pickle.load(open('F:/project2/New folder/year_logreg.pkl', 'rb'))
    y_pred.append(loaded_model.predict(x_test))
    loaded_model = pickle.load(open('F:/project2/New folder/year_dt.pkl', 'rb'))
    y_pred.append(loaded_model.predict(x_test))
    print(y_pred)
    return y_pred
