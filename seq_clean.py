import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.preprocessing import LabelEncoder,OneHotEncoder,StandardScaler,OrdinalEncoder,LabelBinarizer

# Importing the first dataset
df = pd.read_csv("protein-data-set/pdb_data_no_dups.csv")

# Importing the second dataset
df1 = pd.read_csv("protein-data-set/pdb_data_seq.csv")

# Merging the two datasets
df2 = df.set_index('structureId').merge(df1.set_index('structureId'),on='structureId',how='left')

# select proteins
df3 = df2[df2.macromoleculeType_x == 'Protein']
df3.reset_index()

# Drop unwanted columns(not relevant for our model)
df3 = df3.drop(['publicationYear', 'experimentalTechnique', 'chainId', 'macromoleculeType_x', 'macromoleculeType_y',
                'residueCount_x', 'residueCount_y', 'resolution', 'structureMolecularWeight', 'pdbxDetails',
                'densityPercentSol', 'phValue', 'densityMatthews', 'crystallizationTempK', 'crystallizationMethod'], axis = 1)
df4 = df3.drop_duplicates(subset=['sequence', 'classification'])

# Selecting families with 1000<count <2000
counts = df4.classification.value_counts()
class_data = np.asarray(counts[(counts > 1000)&(counts < 2000)].index)
class_data = df4[df4.classification.isin(class_data)]

# Drop nan observations
class_data = class_data.dropna(how='any')

cat_transformer = OrdinalEncoder()
cat_features1 = ['classification']
transformed_cat = cat_transformer.fit_transform(class_data[cat_features1])
class_data[cat_features1] = transformed_cat

#######################
idex = []
idex2 = []
class_data = np.array(class_data)
for i in range(len(class_data)):
    seq = class_data[i, 1]
    a = len(str(seq))
    if a < 50:
        idex.append(i)
class_data1 = np.delete(class_data, idex, axis=0)

#delete B，J，O，U，X and Z
for i in range(len(class_data1)):
    #seq = np.array(class_data[i, 1])
    seq = class_data[i, 1]
    temp = [seq[index:] for index in range(0, len(seq))]
    my_result = [list(element) for element in temp]
    my_result = np.array(my_result)
    for j in range(len(my_result[0])):
        if my_result[0][j] == 'X':
            idex2.append(i)
        elif my_result[0][j] == 'J':
            idex2.append(i)
        elif my_result[0][j] == 'O':
            idex2.append(i)
        elif my_result[0][j] == 'U':
            idex2.append(i)
        elif my_result[0][j] == 'B':
            idex2.append(i)
        elif my_result[0][j] == 'Z':
            idex2.append(i)

class_data2 = np.delete(class_data1, idex2, axis=0)
class_data2 = pd.DataFrame(class_data2)
class_data2.to_csv('protein_family.csv', index=False)

