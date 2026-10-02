#Importing libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from nooverlap import push_text_free
from sklearn.linear_model import LinearRegression
from scipy.stats import pearsonr


#Loading Data
df = pd.read_csv("PosVSSpend.csv")
x = df["Avg Spend"]
y = df["Avg Pos"]
Teams = df["Teams"]

#Averages for x,y
avg_spend = x.mean()
avg_pos = y.mean()




#Performance by colours
colours = []
for xi, yi in zip(x, y):
    if yi > avg_pos and xi < avg_spend:
        colours.append('red')
    elif yi < avg_pos and xi > avg_spend: 
        colours.append('green')
    else:                                    
        colours.append('grey')


#Linear Regression Model
X = x.values.reshape(-1,1)
Y = y.values

linreg = LinearRegression()
linreg.fit(X,Y)

df["Avg Exp Pos"] = linreg.predict(X)

x_fit = np.linspace(min(x),max(x),1000).reshape(-1,1)
y_fit = linreg.predict(x_fit)

df["Residual"] = df["Avg Pos"] - df["Avg Exp Pos"]
res_std = df["Residual"].std()
outliers = df[np.abs(df["Residual"]) > 2 * res_std]
print(outliers[["Teams", "Avg Spend", "Avg Pos", "Avg Exp Pos", "Residual"]])


#Scatter Graph Plotting
plt.figure(figsize=(8,6))
plt.scatter(x, y, color=colours, marker='x')


#Linear Regression Line
plt.plot(x_fit,y_fit, color='orange', label='Linear Regression')
if len(outliers) > 0:   #Only add outliers
    plt.scatter(outliers["Avg Spend"], outliers["Avg Pos"],
                color='purple', s=100, edgecolor='black', label='Outliers')

#Axis
plt.gca().invert_yaxis()
x_min = 0
x_max = int(max(x) + 25)
plt.xticks(np.arange(x_min, x_max + 1, 25))
plt.ylim(21, 0)
plt.yticks(range(1, 21))


#Lines for mean spend and position
plt.axhline(avg_pos, color='grey', linestyle='--', label = 'Avg. Finish')
plt.axvline(avg_spend, color='black', linestyle=':', label = 'Avg. Expenditure')


#Grid, labels, and title
plt.xlabel("Average Expenditure per Season (Millions of Euros)")
plt.ylabel("Average League Finish")
plt.title("The Seasons from 2014/15–2024/25")
plt.grid()
plt.legend()


#Team Labels
for i, team in enumerate(Teams):
    plt.text(x[i], y[i], team, fontsize=8)


#Label Adjustment
fig = plt.gcf()
ax = plt.gca()
push_text_free(fig, ax)

plt.savefig("fig1_11_season.png", dpi=200)


#Correlation (one-sided)
corr, p_value = pearsonr(df["Avg Spend"],df["Avg Pos"], alternative='less')
print(f"n = {len(df)}")
print(f"The correlation coefficient: {corr:.4f}")
print(f"r squared: {corr**2:.4f}")
print(f"Slope (places per million euros): {linreg.coef_[0]:.4f}")
print(f"The P_value (one-sided): {p_value:.4f}")

if p_value <0.05:
    print("The correlation is statistically significant (reject H0).")
else:
    print("The correlation is not statistically significant (fail to reject H0).")
