from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing as pre
from sklearn.preprocessing  import MinMaxScaler

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
