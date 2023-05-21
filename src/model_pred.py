from model import *

# Rescalling test data
df_test[num_cols] = scaler.transform(df_test[num_cols])

#Creating X_test and y_test
X_test = df_test[X_train.columns]
y_test = df_test.price

# Prediction and evaluation
def model_eval(X_test, y_test, model):
    
    y_test_pred = model.predict(sm.add_constant(X_test))
        
    r2 = r2_score(y_true = y_test,
                  y_pred = y_test_pred)
    
    mse = mean_squared_error(y_true = y_test,
                             y_pred = y_test_pred )
    
    plt.scatter(x = y_test, y = y_test_pred, color = 'C1')
    plt.xlabel('y_test')
    plt.ylabel('y_test_pred')
    plt.title('y_test vs y_pred')
#   plt.savefig('y_test vs y_pred.png', dpi = 500)
    
    
    print('\nCoeff of determination, r2: {}'.format(r2))
    print('\nMean squared error, mse: {}'.format(mse))
    
    return r2, mse

model_eval(X_test, y_test, m4)