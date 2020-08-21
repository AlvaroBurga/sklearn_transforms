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
        from sklearn import preprocessing as pre
        from sklearn.preprocessing  import MinMaxScaler
        scaler = pre.MinMaxScaler()
        #Si cambio
        data = X.copy()
        xfeatures = data.iloc[:,:-1]
        ar_Norm = pre.MinMaxScaler(xfeatures)
        scaler.fit(xfeatures)
        ar_Norm=scaler.transform(xfeatures)
        df_Norm= pd.DataFrame(ar_Norm, columns=df_data_3.columns[:-1])
        df_data_4 = pd.concat([df_Norm, df_data_3.iloc[:,-1:]], axis=1)
        # Devolvemos el data frame con los datos normalizados
        return df_data_4
