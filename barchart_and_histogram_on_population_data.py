# -*- coding: utf-8 -*-
"""Barchart and Histogram on population data.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IvcIjXSpknJ3ivaSwo-lpKmi-vC9Hhjv

Importing the libraries
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

"""Obtaining the datasets"""

data = pd.read_csv('/content/drive/MyDrive/adult.data.csv')
data.head()

# @title race

from matplotlib import pyplot as plt
import seaborn as sns
data.groupby('race').size().plot(kind='bar', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

# @title age

from matplotlib import pyplot as plt
data['age'].plot(kind='hist', bins=20, title='age')
plt.gca().spines[['top', 'right',]].set_visible(False)

"""Gender"""

sfrom matplotlib import pyplot as plt
import seaborn as sns
data.groupby('sex').size().plot(kind='bar', color=sns.palettes.mpl_palette('Dark2'))
plt.gca().spines[['top', 'right',]].set_visible(False)

