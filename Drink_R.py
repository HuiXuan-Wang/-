import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_excel('drink.xlsx')


data_x = df['temperature']
data_y = df['quantity']

# 分割trian/test

train_x, test_x, train_y, test_y = train_test_split(data_x,
                                                    data_y,
                                                    test_size=0.25,
                                                    random_state=1)

# 氣溫對杯數的散佈圖

plt.scatter(train_x, train_y, facecolor='None', edgecolor='k', alpha=0.3)
plt.show()

train_x.values.reshape(-1, 1)

train_x_reshape = train_x.values.reshape(-1, 1)

model = LinearRegression()
model.fit(train_x_reshape, train_y)

print(f"Coefficient:{model.coef_}")
print(f"Beta0:{model.intercept_}")
print(f"R2:{model.score(train_x_reshape, train_y)}")

data_x_reshape = data_x.values.reshape(-1, 1)

xp = np.linspace(data_x_reshape.min(), data_x_reshape.max(), 70)
xp = xp.reshape(-1, 1)
pred_plot = model.predict(xp)

plt.title('LinearRegression')
plt.xlabel('Temperature')
plt.ylabel('Quantity')

plt.scatter(data_x_reshape, data_y, facecolor='None', edgecolor='k', alpha=0.8)
plt.plot(xp, pred_plot)
plt.show()

test_x_reshape = test_x.values.reshape(-1, 1)
pred = model.predict(test_x_reshape)
print("predict")
for i in range(5):
    print("true:", test_y.values[i])
    print("prediction:", pred[i])
