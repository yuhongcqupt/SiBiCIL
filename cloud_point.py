import sys
try:
    import pandas as pd
except ImportError as e:
    print("pandas is required for this example. Please install with conda or pip  and then try again.")
    sys.exit()
import numpy as np
import pandas as pd
pd.set_option('display.max_columns', None)
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
pd.set_option('display.max_columns', None)

##Generate point-cloud data
def data_clean(origin_data):

    data = pd.DataFrame(origin_data)
    pointclouds_num = np.zeros((len(data), data.shape[1], data.shape[1]))
    totalrows = data.shape[0]  
    totalpred = data.shape[1]  
    for i in range(0, totalrows):
        irow = data.iloc[[i]]
        irow = irow.iloc[:, :]
        pointcloud = irow.copy()
        for j in range(0, totalpred):
            newrow = irow.copy()
            newrow.iat[0, j] = 0 
            pointcloud = pointcloud.append(newrow, ignore_index=True)
        pointclouds_num[i, :, :] = pointcloud
    return pointclouds_num