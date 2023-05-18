# Tratamiento de los datos
# ========================
import pandas as pd
import numpy as np

# Librerías para realizar la codificación
# =======================================
from sklearn.preprocessing import OrdinalEncoder

#  Modelado y métricas
# ====================
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score , cohen_kappa_score, roc_curve,roc_auc_score, r2_score, mean_squared_error, mean_absolute_error


# EDA. EXPLORACIÓN NUMÉRICA
def explorar_df(dataframe, nombre = ''):
    """Esta función realiza la exploración inicial de un dataframe dado:
            - Muestra las 5 primeras filas
            - Muestra las 5 últimas filas
            - Muestra 10 filas aleatorias
            - Indica el nº de filas y columnas
            - Muestra el resultado del método .info()
            - Indica el número de nulos por columna en valor absoluto y porcentaje
            - Indica el nº de filas duplicadas. En caso de que no pueda realizar la comprobación muestra un error
            - Muestra los principales estadísticos tanto de las columnas numéricas (si las hay) como de las categóricas (si las hay)
            - Muestra el nombre de las columnas
            - Indica el numero de valores distintos de cada columna y muestra los valores cuando sean 15 o menos          
        Parámetros:
            - dataframe (pandas.core.frame.DataFrame): dataframe que se requiere explorar
            - nombre (str): nombre del dataframe a explorar. Parámetro por defecto con valor '' para que si n o se le quiere poner un nombre al dataframe
              la exploración pueda continuar.
        Return: None.
    """
    print(f'EXPLORACIÓN DEL DATAFRAME {nombre.upper()}')
    print('---------------------------------------------------------------------------')
    print(f'Las primeras 5 filas del dataframe {nombre} son:')
    display(dataframe.head())
    print('---------------------------------------------------------------------------')
    print(f'Las últimas 5 filas del dataframe {nombre} son:')
    display(dataframe.tail())
    print('---------------------------------------------------------------------------')
    print(f'A comntinuación se muestran 10 filas aleatorias del dataframe {nombre}:')
    display(dataframe.sample(10))
    print('---------------------------------------------------------------------------')
    print(f'El dataframe {nombre} tiene {dataframe.shape[0]} filas y {dataframe.shape[1]} columnas')
    print('---------------------------------------------------------------------------')
    print('A continuación el resultado del método .info() incluyendo los tipos de dato de cada columna:')
    dataframe.info()
    print('---------------------------------------------------------------------------')
    print('El número de nulos por columna en valor absoluto y porcentaje es:')
    for i, col in enumerate(dataframe.isnull().sum()):
        print(f'{dataframe.isnull().sum().index[i]}: nº de nulos: {col}. % de nulos: {round(col/dataframe.shape[0]*100, 2)} %')
    print('---------------------------------------------------------------------------')
    try:
        print(f'El nº de filas duplicadas del dataframe {nombre} es: {dataframe.duplicated().sum()}')
    except:
        print(f'Ha ocurrido un error. No se ha podido comprobar si el dataframe {nombre} tiene filas duplicdas')
    print('---------------------------------------------------------------------------')
    if dataframe.select_dtypes(include=np.number).shape[1] != 0:
        print(f'Los principales estadísticos de las columnas numéricas son:')
        display(dataframe.describe().T)
    print('---------------------------------------------------------------------------')
    if dataframe.select_dtypes(exclude=np.number).shape[1] != 0:
        print(f'Los principales estadísticos de las columnas categóricas son:')
        display(dataframe.describe(include=object).T)
    print('---------------------------------------------------------------------------')
    print(f'El dataframe {nombre} tiene las siguientes columnas: \n{dataframe.columns}')
    print('---------------------------------------------------------------------------')
    print('El numero de valores distintos de cada columna es:')
    for col in dataframe.columns:
        if len(dataframe[col].value_counts()) > 15:
            print(f'{col}: {len(dataframe[col].value_counts())}')
        else:
            print(f'{col}: {len(dataframe[col].value_counts())}')
            print(f'Los valores únicos de la columna "{col}" son: {dataframe[col].unique()}')



# DETECCIÓN OUTLIERS
def detectar_outliers(lista_columnas, dataframe): 
    """Esta función realiza detección de aoutliers de las columnas indicadas de un dataframe dado.      
        Parámetros:
            - lista_columnas (list): lista de las columnas en las que queremos detectar los outliers
            - dataframe (pandas.core.frame.DataFrame): dataframe que se requiere explorar
        Return: 
            - df (pandas.core.frame.DataFrame): dataframe con los outliers detectados
            - dicc_indices (dict): diccionario con los índices de los mismos.
    """
    dicc_indices = {}
    df = pd.DataFrame()
    for col in lista_columnas:
        Q1 = np.percentile(dataframe[col], 25)
        Q3 = np.percentile(dataframe[col], 75)
        IQR = Q3 - Q1
        outlier_step = 1.5 * IQR
        outliers_data = dataframe[(dataframe[col] < (Q1 - outlier_step)) | (dataframe[col] > (Q3 + outlier_step))]
        df = pd.concat([df, outliers_data], axis=0)
        if outliers_data.shape[0] > 0:
            dicc_indices[col] = (list(outliers_data.index))   
    return df, dicc_indices # estraemos tanto el dataframe con los outliers como el diccionario con sus índices


# ENCODING
def ordinal_encoder(df, columna, orden_valores, lista_índice):
    """Esta función utiliza el ordinal encoder para ralizar el encoding de una columna dada. 
    Parámetros:
        - df (pandas.core.frame.DataFrame): dataframe sobre el que queremos realizar el encoding
        - columna (pandas.core.series.Series): columna a la que queremos aplicar el encoding
        - orden_valores (list): lista con las categorías ordenadas de menor a mayor valor de la mediana de la variable respuesta
        - lista_índice (list): lista con los valores del índice que le queremos poner al dataframe con los datos codificados al crearlo
    Return:
        - df (pandas.core.frame.DataFrame): dataframe con el cncoding realizado
    """ 
    ordinal = OrdinalEncoder(categories = [orden_valores], dtype = int) # iniciamos el método
    transformados_oe = ordinal.fit_transform(df[[columna]]) # aplicamos la transformación a los datos
    oe_df = pd.DataFrame(transformados_oe, index=lista_índice) # lo convertimos a dataframe
    oe_df.columns = ordinal.feature_names_in_ # cambiamos el nombre de la columna
    columna += "_oe" # nombre columna generada
    df[columna] = oe_df # sobreescribimos la columna con los valores de la tranformación 
    return df


# REGRESIÓN LINEAL. MÉTRICAS
def metricas_rlin(real_test, predict_test, real_train, predict_train, modelo):
    resultados = {'MAE': [mean_absolute_error(real_test, predict_test), mean_absolute_error(real_train, predict_train)],
                'MSE': [mean_squared_error(real_test, predict_test), mean_squared_error(real_train, predict_train)],
                'RMSE': [np.sqrt(mean_squared_error(real_test, predict_test)), np.sqrt(mean_squared_error(real_train, predict_train))],
                'R2':  [r2_score(real_test, predict_test), r2_score(real_train, predict_train)],
                 "set": ["test", "train"], 
                 "modelo": [modelo, modelo]}
    df = pd.DataFrame(resultados)
    return df

# REGRESIÓN LOGÍSTICA. MÉTRICAS
def metricas_rlog(clases_reales_test, clases_predichas_test, clases_reales_train, clases_predichas_train, modelo):  
    # para el test
    accuracy_test = accuracy_score(clases_reales_test, clases_predichas_test)
    precision_test = precision_score(clases_reales_test, clases_predichas_test) # pos_label='satisfied'
    recall_test = recall_score(clases_reales_test, clases_predichas_test)
    f1_test = f1_score(clases_reales_test, clases_predichas_test)
    kappa_test = cohen_kappa_score(clases_reales_test, clases_predichas_test)
    # para el train
    accuracy_train = accuracy_score(clases_reales_train, clases_predichas_train)
    precision_train = precision_score(clases_reales_train, clases_predichas_train)
    recall_train = recall_score(clases_reales_train, clases_predichas_train)
    f1_train = f1_score(clases_reales_train, clases_predichas_train)
    kappa_train = cohen_kappa_score(clases_reales_train, clases_predichas_train)
    #creamos el df
    df = pd.DataFrame({"accuracy": [accuracy_test, accuracy_train], 
                       "precision": [precision_test, precision_train],
                       "recall": [recall_test, recall_train], 
                       "f1": [f1_test, f1_train],
                       "kappa": [kappa_test, kappa_train],
                       "set": ["test", "train"]})
    df["modelo"] = modelo
    return df