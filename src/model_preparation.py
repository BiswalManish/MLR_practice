from clean_data import *
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

corr = house.corr()

plt.figure(figsize = (12,12))
sns.heatmap(corr, annot = True, cmap = 'inferno')
plt.show()
# plt.savefig('Heatmap.png' , dpi = 500)

# TRAIN TEST SPLIT
df_train, df_test = train_test_split(house, test_size = 0.3,
                                    random_state = 42)

#Rescalling
num_cols = num_cols + num_dis_col
scaler = MinMaxScaler()
df_train[num_cols] = scaler.fit_transform(df_train[num_cols])

### Creating X and y
X_train, y_train = df_train.drop(['price'], axis = 1), df_train.price


