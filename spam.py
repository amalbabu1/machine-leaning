mport sys
import numpy
import pandas
import matplotlib
import seaborn
import scipy
print('Python: {}'.format(sys.version))
print
('Numpy: {}'.format(numpy.__version__))
print('Pandas: {}'.format(pandas.__version__))
print('Matplotlib: {}'.format(matplotlib.__version__))
print('Seaborn: {}'.format(seaborn.__version__))
print('Scipy: {}'.format(scipy.__version__))
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv(r'E:\development\New folder\creditcard.csv')#load data set
print(data.columns)
