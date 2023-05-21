from data import *

#EDA

def get_bars(data, cols):
    
    for i in cols:
        sns.catplot(kind = 'count',
                   palette = 'Spectral',
                   x = i,
                   data = data)
        plt.show()
#         plt.savefig(f'Count plot for {i}', dpi = 500)

def get_dist(data, cols):
        
    for i in cols:
        plt.figure(figsize = (10, 5))
        plt.subplot(1, 2, 2)
        sns.boxenplot(color = 'C0',
                   x = i,
                   data = data)
        
        plt.subplot(1, 2, 1)
        sns.kdeplot(data = data,
                   x = i, color = 'C3')
        
#         plt.savefig(f'Dist plot for {i}', dpi = 500)
        plt.show()


