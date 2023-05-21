from model_preparation import *
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import r2_score, mean_squared_error

# Features with highest correlation with price
var = list(corr.price.sort_values(ascending = False).index)
var.remove('price')

var_list = []
for i in range(1,len(var) + 1):
    k = var[ : i]
    var_list.append(k)

# Getting a linear model
def get_linear_model(X_train, y_train):
    
    model = sm.OLS(y_train, sm.add_constant(X_train))
    model = model.fit()
    print(model.summary2())
    print('\n' * 4)
    
    return model

#getting the model after adding one variable at a time
adjusted_r2 = []
for i in var_list:
    m = get_linear_model(X_train = X_train[i],
                    y_train = y_train)
    adjusted_r2.append(round(m.rsquared_adj * 100, 3))


# Adjusted R2 vs features
plt.plot(adjusted_r2, 'C3')
plt.ylabel('Adjusted_r2')
plt.xlabel('No. of features')
plt.title('Adjusted R2 vs No. of features')
# plt.savefig('Adjusted R2 vs no. of features.png', dpi = 500)


# Checking Variable inflation factor
def get_VIF(X_train):
    vif = pd.DataFrame()
    vif['Features'] = X_train.columns
    vif['VIF'] = [variance_inflation_factor(X_train.values, i) for i in range(X_train.shape[1])]
    vif['VIF'] = round(vif['VIF'], 2)
    vif = vif.sort_values(by = "VIF", ascending = False)
    return vif


#FEATURE ELIMINATON
def get_features(X_train, y_train, feat_):
    X_train = X_train.drop(feat_, axis = 1)
    model = get_linear_model(X_train, y_train)
    print(get_VIF(X_train))
    return model, X_train

# highest p-value and VIF is of semi-furnished
# remove semi-furnished
m1, X_train = get_features(X_train, y_train,
                           feat_ = ['semi-furnished'])

#removing bedrooms and semi furnished
m2, X_train = get_features(X_train, y_train,
                           feat_ = ['bedrooms'])

# removing gurnished, mainroad and guestroom as them have high values
m3, X_train = get_features(X_train, y_train,
                           feat_ = ['furnished', 'guestroom', 'mainroad'])

# removing unfurnished
m4, X_train = get_features(X_train, y_train,
                           feat_ = ['hotwaterheating'] )


# SAVING THE MODELS
# models = [m1, m2, m3, m4]
# for m in range(len(models)):
#     fname = f'Model {m + 1}'
#     pickle.dump(models[m], open(fname, 'wb'))

