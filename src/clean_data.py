from data import *


def binary_map(x):
    
    return x.map({'yes': 1, 'no': 0})
    
status = cat_col.pop(-1)

house[cat_col] = house[cat_col].apply(lambda x: binary_map(x))

status = pd.get_dummies(house[status])

house = pd.concat([house, status], axis = 1).drop(['furnishingstatus'], axis = 1)

# house.to_csv('Housing_clean.csv', sep = ',', index = False)