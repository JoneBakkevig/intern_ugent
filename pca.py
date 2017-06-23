import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA as sklearnPCA
import sklearn.preprocessing as skp
from excelparse import fileToDframe

df = fileToDframe('Data_nieuwveer.xlsx', 92, [4,6,42,79], 1)
n = df.values
min_max_scaler = skp.MinMaxScaler()
n_scaled = min_max_scaler.fit_transform(n)

imp = skp.Imputer(missing_values='NaN', strategy='mean', axis=1)
clean_df = pd.DataFrame(imp.fit_transform(n_scaled),columns=df.columns, index=df.index)

def doPca(data, n_comp=2):
    pca = sklearnPCA(n_components=n_comp)
    pca.fit(data)
    # Create graph to determine best component number
    if n_comp == None:
        plt.figure(figsize=(8, 4))
        plt.plot(pca.explained_variance_)
        plt.xticks(np.arange(0, 4, 1.0))
        plt.xlabel('n_components')
        plt.ylabel('explained_variance_')
        plt.show()

    return pca

pca = doPca(clean_df)




# print pca.explained_variance_
# print pca.explained_variance_ratio_











