from model import *

def residual_analysis(X_train, y_train, model):
    
    if input('Which model?\n(stats/sklearn) ').lower() == 'stats':
        
        y_train_pred = model.predict(sm.add_constant(X_train))
    
    else:
        
        y_train_pred = model.predict(X_train.values.reshape(-1, 1))

    
    res = y_train - y_train_pred
    
    for i in X_train.columns:
    
        plt.figure(figsize = (10, 5))    
        plt.subplot(1, 2, 1)
        sns.distplot(x = res, color = 'C3')
    
        plt.subplot(1, 2, 2)
        sns.scatterplot(x = X_train[i], y = res)
    
#         if input('Save residual analysis?\n(y/n) ').lower() == 'y':
#             plt.savefig(f'Residual analysis for {i}', dpi = 500)
    
#         else:
        plt.show() 


# training data
residual_analysis(X_train, y_train, m4)