import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

import warnings 
warnings.filterwarnings('ignore')

path = '/Users/manish/Documents/Projects/data_science/MLR_practice/data/raw data/Housing.csv'

house = pd.read_csv(path)

cat_col = ['mainroad', 'guestroom', 'basement', 
           'hotwaterheating', 'airconditioning',
           'prefarea', 'furnishingstatus']

num_cols = ['area', 'price']

num_dis_col = ['bedrooms', 'bathrooms', 'stories', 'parking']