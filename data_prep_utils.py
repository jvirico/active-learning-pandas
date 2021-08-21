import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import statsmodels.api as sm
from scipy import stats

plt.style.use('seaborn-darkgrid')

def RunNormalityAnalysis(data,desc='Energy per hour',var='energy'):
    #### Normality analysis
    fig, axes = plt.subplots(2,2)
    ax = axes.ravel()
    # we fit mean and variance to the data
    mu, sigma = stats.norm.fit(data)
    print('Mean: %s and Std: %s' % (mu,sigma))
    # theorical values of normal distribution in the observed range
    print(min(data))
    print(max(data))
    x_hat = np.linspace(min(data),max(data), num=100)
    y_hat = stats.norm.pdf(x_hat, mu, sigma)

    ax[0].plot(x_hat, y_hat, linewidth=2, label='normal')
    ax[0].hist(x=data, density=True, bins=40, color="#3182bd", alpha=0.5)
    ax[0].plot(data, np.full_like(data, -0.01), '|k', markeredgewidth=1)
    ax[0].set_title(desc)
    ax[0].set_xlabel(var)
    ax[0].set_ylabel('Probaility Distribution')
    ax[0].legend()

    ## Q-Q plot
    sm.qqplot(data,fit=True,line='q',alpha=0.4,lw=2,ax=ax[1])
    ax[1].set_title('Q-Q plot of %s' % var)
    ax[1].tick_params(labelsize=7)
    # Boxplot
    ax[2].set_title(desc)
    ax[2].boxplot(data)

    # Analytical methods
    kurt = stats.kurtosis(data)
    skewness = stats.skew(data)
    # Hypothesis Contrast
    shapiro_test = stats.shapiro(data)
    k2, p_value = stats.normaltest(data)

    ax[3].text(0.1, 0.8, 'Kurtosis = %4.2f'% kurt, dict(size=9))
    ax[3].text(0.1, 0.7, 'Skewness = %4.2f'% skewness, dict(size=9))
    ax[3].text(0.1, 0.6, 'Shapiro test p-value = %4.5f'% shapiro_test[1], dict(size=9))
    ax[3].text(0.1, 0.5, "D'Agostino test p_value = %4.5f"% p_value, dict(size=9))
    ax[3].axis('off')
    ax[3].grid(False)

    plt.show()

# DataFrame columns normalization
def normalize(df,columns):
    result = df.copy()
    for feature_name in columns:
        max_value = df[feature_name].max()
        min_value = df[feature_name].min()
        result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    return result