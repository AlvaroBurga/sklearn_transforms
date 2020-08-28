from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing as pre
from sklearn.preprocessing  import MinMaxScaler
from sklearn.utils import resample
import numpy as np

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')
    
# All sklearn Transforms must have the `transform` and `fit` methods
class Normalizate():
    def __init__(self):
        self.columns = "a"

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        from sklearn import preprocessing
        from sklearn.preprocessing  import MinMaxScaler
        import numpy as np
        scaler = MinMaxScaler()
        data = X.copy()
        xfeatures = data[:,:-1]
        ar_Norm = preprocessing.MinMaxScaler(xfeatures)
        scaler.fit(xfeatures)
        ar_Norm=scaler.transform(xfeatures)
        ar_Norm2=np.concatenate((ar_Norm,data[:,-1:]),axis=1)
        return ar_Norm2

class LlenarMedia():
    def __init__(self):
        self = self

    def fit(self, X, y=None):
        return self
    
    def transform(self, d):
        # Primero copiamos el dataframe de datos de entrada 'd'
        data = d.copy()
        x=data[:,:-1]
        y=data[:,[-1]]
        si.fit(X=x)
        x=si.transform(X=x)
        data=np.concatenate((x,y),axis=1)
        return data

class NivelarDatos():
    def __init__(self):
        self = self

    def fit(self, X, y=None):
        return self
    
class NivelarDatos():
    def __init__(self):
        self = self

    def fit(self, X, y=None):
        return self
    
    def transform(self, data):
        # Primero copiamos el dataframe de datos de entrada 'X'
        b=data.reshape(1, -1)
        i=0
        aceptado=[]
        sospechoso=[]
        for mayor in range(len(data[:,1])):
            boolean=(data[mayor,-1]=='Aceptado')
            if(boolean): aceptado.append(b[i,:])
            else: sospechoso.append(b[i,:])
            i=i+1
        la=len(aceptado)
        sospechoso=resample(sospechoso,replace=True,n_samples=la,random_state=123)
        aceptado=np.asarray(aceptado)
        sospechoso=np.asarray(sospechoso)
        fin=np.concatenate((aceptado,sospechoso))
        fin.reshape(1, -1)
        return fin

