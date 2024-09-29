import yfinance as yf
import pandas as pd
import os
import sklearn.ensemble
from sklearn.metrics import precision_score

stock = input('Please enter the stock symbol ')

if os.path.exists("stock.csv"):
    stock = pd.read_csv("stock.csv", index_col=0)
else:
    stock = yf.Ticker("^GSPC")
    stock = stock.history(period="max")
    stock.to_csv("stock.csv")

stock.index = pd.to_datetime(stock.index)

del stock["Dividends"]
del stock["Stock Splits"]
stock["Tomorrow"] = stock["Close"].shift(-1)
stock["Target"] = (stock["Tomorrow"] > stock["Close"]).astype(int)

from sklearn.ensemble import RandomForestClassifier

horizons = [2, 5, 60, 250, 1000]
new_predictors = []

for horizon in horizons:
    rolling_averages = stock.rolling(horizon).mean()

    ratio_column = f"Close_Ratio_{horizon}"
    stock[ratio_column] = stock["Close"] / rolling_averages["Close"]

    trend_column = f"Trend_{horizon}"
    stock[trend_column] = stock.shift(1).rolling(horizon).sum()["Target"]

    new_predictors += [ratio_column, trend_column]

stock = stock.dropna(subset=stock.columns[stock.columns != "Tomorrow"])

model = RandomForestClassifier(n_estimators=200, min_samples_split=50, random_state=1)

def calculate_rsi(data, window=14):
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

def predict(train, test, predictors, model):
    model.fit(train[predictors], train["Target"])
    preds = model.predict_proba(test[predictors])[:,1]
    preds[preds >= .6] = 1
    preds[preds < .6] = 0
    preds = pd.Series(preds, index=test.index, name="Predictions")
    combined = pd.concat([test["Target"], preds], axis=1)
    return combined

def backtest(data, model, predictors, start=2500, step=250):
    all_predictions = []

    for i in range(start, data.shape[0], step):
        train = data.iloc[0:i].copy()
        test = data.iloc[i:(i+step)].copy()
        predictions = predict(train, test, predictors, model)
        all_predictions.append(predictions)

    return pd.concat(all_predictions)

predictions = backtest(stock, model, new_predictors)

predictions["Predictions"].value_counts()

print("Precision Score:", precision_score(predictions["Target"], predictions["Predictions"]))

print(predictions["Target"].value_counts() / predictions.shape[0])

print(predictions)
