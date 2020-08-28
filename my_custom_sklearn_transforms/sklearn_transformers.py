from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing as pre
from sklearn.preprocessing  import MinMaxScaler
from sklearn.utils import resample

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        data = X.copy()
        # Devolvemos un nuevo dataframe de datos sin las columnas no deseadas
        return data.drop(labels=self.columns, axis='columns')

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
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        b= X.copy()
        i=0
        aceptado=[]
        sospechoso=[]
        for mayor in range(len(b[:,1])):
            boolean=(b[mayor,-1]=='Aceptado')
            if(boolean): aceptado.append(b[i,:])
            else: sospechoso.append(b[i,:])
            i=i+1
        la=len(aceptado)
        sospechoso=resample(sospechoso,replace=True,n_samples=la,random_state=123)
        data=aceptado+sospechoso
        return data
