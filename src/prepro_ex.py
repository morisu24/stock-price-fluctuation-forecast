import pandas as pd

df = pd.read_csv("code_USD.csv", header=0)
df.columns=["Date", "Close"]
df["index"] = [i for i in range(len(df))]
print(df.head(10))

ex_list = [

'AUD',#オーストラリアドル
'BHD',#バーレーンディナール
'CAD',#カナダドル
'CHF',#スイスフラン
'CNY',#中華人民元
'DKK',#デンマーククローネ
'EUR',#ユーロ
'GBP',#英ポンド
'HKD',#香港ドル
'INR',#インドルピー
'NOK',#ノルウェークローネ
'NZD',#ニュージーランドドル
'PHP',#フィリピンペソ
'SEK',#スウェーデンクローネ
'SGD',#シンガポールドル
#'USD',#米ドル
'ZAR',#南アフリカランド

]

for ex in ex_list:
    print(ex)
    df_ex = pd.read_csv("ex_" + str(ex) + ".csv", header=0)#データ読み込み
    df_ex.columns=["Date", "Close"]#columns名を変更

    dates = []
    closeis = []
    for d in df["Date"]:
        #try:
        date = df_ex.loc[(df_ex.Date == d), "Date"]#米ドルの日付をexファイルから検索
        print(date)
        yesterday_date = date.values[0]
        dates.append(date.values[0])#日付をデータセットに追加

        close = df_ex.loc[(df_ex.Date == d), "Close"]#日付が一致した日のexのCloseのデータを取り出す
        if str(close.values[0]) != str("nan"):#取り出したCloseがnanでないかを判断
            yesterday_close = close.values[0]
            closeis.append(close.values[0])

        else:
            #print("nan")
            closeis.append(yesterday_close)
        
    df_ex2 = pd.DataFrame({"Date_" + str(ex) : dates,
                            "Close_" + str(ex) : closeis})#新しくデータフレームを作成

    df = pd.concat([df, df_ex2], axis=1)#米ドルのデータとexデータを統合
    df["diff_" + str(ex)] = (df["Close_" + str(ex)] / df["Close_" + str(ex)].shift(-1)) - 1
    #print(df)

df.to_csv("code_USD_plus.csv")
