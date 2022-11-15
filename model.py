import pandas as pd
from scipy.stats import bernoulli
from sklearn.linear_model import LogisticRegression


dates = pd.period_range(start='01/01/2021', end='30/03/2022', freq='D')
agent = bernoulli.rvs(0.1, size = dates.shape[0])
data_agent = pd.DataFrame(index = dates, data=dict(agent = agent))
n_lag = 1
data_agent_lag = data_agent.shift(n_lag)
data_agent_lag.columns = ['agent_lag']
data_total = pd.concat([data_agent, data_agent_lag], axis=1)
data_total.dropna(inplace=True)
data_total = data_total.astype(int)

lr = LogisticRegression()
condition = data_total == 0
((condition).all(axis=1)).sum()/data_total.shape[0]
p1 = condition.agent.sum()/condition.shape[0]
p2 = condition.agent_lag.sum()/condition.shape[0]
p1*p2
lr.fit(data_total[['agent_lag']], data_total['agent'])
lr.predict_proba([[1]])
lr.intercept_, lr.coef_