import pandas as pd

df = pd.read_csv("code_9201.csv", header=0)
df.columns=["Date", "Open", "High", "Low", "Close", "Volume"]
df["index"] = [i for i in range(len(df))]
print(df.head(10))

etf_list = [

1305,#ダイワ 上場投信-トピックス
1306,#TOPIX連動型上場投資信託
1308,#上場インデックスファンドTOPIX
1320,#ダイワ 上場投信-日経225
1321,#日経225連動型上場投資信託
1329,#iシェアーズ日経225ETF
1330,#上場インデックスファンド225
1346,#MAXIS 日経225上場投信
1348,#MAXIS トピックス上場投信
1369,#One ETF 日経225
#1473,#One ETF トピックス
1475,#iシェアーズ TOPIX ETF
1578,#上場インデックスファンド日経225(ミニ)
2035,#NEXT NOTES 日経平均VI先物指数 ETN

]

for etf in etf_list:
    print(etf)
    df_etf = pd.read_csv("etf_" + str(etf) + ".csv", header=0)#データ読み込み
    df_etf.columns=["Date", "Open", "High", "Low", "Close", "Volume"]#columns名を変更

    dates = []
    closeis = []
    for d in df["Date"]:
        #try:
        date = df_etf.loc[(df_etf.Date == d), "Date"]#日本航空(株)の日付をETFファイルから検索
        print(date)
        yesterday_date = date.values[0]
        dates.append(date.values[0])#日付をデータセットに追加

        close = df_etf.loc[(df_etf.Date == d), "Close"]#日付が一致した日のETFのCloseのデータを取り出す
        if str(close.values[0]) != str("nan"):#取り出したCloseがnanでないかを判断
            yesterday_close = close.values[0]
            closeis.append(close.values[0])

        else:
            #print("nan")
            closeis.append(yesterday_close)
        
    df_etf2 = pd.DataFrame({"Date_" + str(etf) : dates,
                            "Close_" + str(etf) : closeis})#新しくデータフレームを作成

    df = pd.concat([df, df_etf2], axis=1)#日本航空(株)のデータとETFデータを統合
    df["diff_" + str(etf)] = (df["Close_" + str(etf)] / df["Close_" + str(etf)].shift(-1)) - 1
    #print(df)

df.to_csv("code_9201_plus.csv")
