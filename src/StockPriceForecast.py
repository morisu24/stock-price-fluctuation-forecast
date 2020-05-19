import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np

df = pd.read_csv("code_9201_plus.csv")
df = df.sort_values(by=["index"], ascending=False)
print(df.tail(20))


df = df.iloc[0:len(df) - 1]
print(df.tail())

df_train = df.iloc[1:len(df)-1]
df_test = df.iloc[len(df)-1:len(df)]

#print("train", df_train)
#print("test", df_test)

xlist = [

"diff_1305",#ダイワ 上場投信-トピックス
"diff_1306",#TOPIX連動型上場投資信託
"diff_1308",#上場インデックスファンドTOPIX
"diff_1320",#ダイワ 上場投信-日経225
"diff_1321",#日経225連動型上場投資信託
"diff_1329",#iシェアーズ日経225ETF
"diff_1330",#上場インデックスファンド225
"diff_1346",#MAXIS 日経225上場投信
"diff_1348",#MAXIS トピックス上場投信
"diff_1369",#One ETF 日経225
#"diff_1473",#One ETF トピックス
"diff_1475",#iシェアーズ TOPIX ETF
"diff_1578",#上場インデックスファンド日経225(ミニ)
"diff_2035",#NEXT NOTES 日経平均VI先物指数 ETN

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
