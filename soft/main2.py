import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Загрузка данных
sunspot_data = pd.read_csv("D:/sunspot/main2.py")

# Просмотр структуры данных
print(sunspot_data.head())


sunspot_data.replace(-1, np.nan, inplace=True)

# Удаление строк с пропусками (или можно использовать метод заполнения, например, средним)
sunspot_data.dropna(inplace=True)

# Разделение данных на признаки (X) и целевую переменную (Y)
X = sunspot_data.drop(columns='Number of Sunspots', axis=1)  # замените на правильные признаки
Y = sunspot_data['Number of Sunspots']

# Разделение на обучающую и тестовую выборки
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
X_train_prediction = model.predict(X_train)

# Построение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, Y_train)

# Предсказание на тестовой выборке
Y_pred = model.predict(X_test)

# Оценка модели
mse = mean_squared_error(Y_test, Y_pred)
rmse = np.sqrt(mse)

print(f"Root Mean Squared Error: {rmse}")
