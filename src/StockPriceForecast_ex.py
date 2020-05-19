import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

df = pd.read_csv("code_USD_plus.csv")
df = df.sort_values(by=["index"], ascending=False)
print(df.tail(20))


df = df.iloc[0:len(df) - 1]
print(df.tail())

df_train = df.iloc[1:len(df)-1]
df_test = df.iloc[len(df)-1:len(df)]

#print("train", df_train)
#print("test", df_test)

xlist = [

"diff_AUD",
"diff_BHD",
"diff_CAD",
"diff_CHF",
"diff_CNY",
"diff_DKK",
"diff_EUR",
"diff_GBP",
"diff_HKD",
"diff_INR",
"diff_NOK",
"diff_NZD",
"diff_PHP",
"diff_SEK",
"diff_SGD",
#"diff_USD",
"diff_ZAR",

]

x_train = []
y_train = []
for s in range(0, len(df_train) - 1):
	print("x_train : ", df_train["Date"].iloc[s])
	print("y_train : ", df_train["Date"].iloc[s + 1])
	print("")
	x_train.append(df_train[xlist].iloc[s])

	if df_train["Close"].iloc[s + 1] > df_train["Close"].iloc[s]:
		y_train.append(1)
	else:
		y_train.append(-1)

#print(x_train)
#print(y_train)

rf = RandomForestClassifier(n_estimators=len(x_train), random_state=0)
rf.fit(x_train, y_train)


test_x = df_test[xlist].iloc[0]
print(test_x)
test_y = rf.predict(test_x.values.reshape(1, -1))
print("--------------------")
print("result : ", test_y[0])
print("--------------------")
