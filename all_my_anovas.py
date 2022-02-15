import pandas as pd
from scipy import stats

def my_oneway_anova(x):
    my_data = pd.read_csv(x)

    normal = my_data[my_data['condition']=='condition_a']['response_time']
    degraded = my_data[my_data['condition']=='condition_b']['response_time']

    return stats.f_oneway(normal, degraded)
