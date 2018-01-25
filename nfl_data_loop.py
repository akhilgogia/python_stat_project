import requests
import pandas as pd
from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf8')

print("Pos")
p = raw_input()
print("Year")
y = raw_input()

counter = 1

while counter < 18:



# x = ("http://www.footballdb.com/fantasy-football/index.html?pos=%s&yr=%d&wk=%d&rules=2")



# url = 'x'
# html = requests.get(url).content
# df_list = pd.read_html(html)
# df = df_list[0]
# print df
# df.to_csv('QB_Wk_16_2017')

    # print("Week")
    z = counter


    # x = 'http://www.footballdb.com/fantasy-football/'


    x = 'http://www.footballdb.com/fantasy-football/index.html?pos=%s&yr=%s&wk=%s&rules=2' % (p, y, z)

    # print(x)


    # y.to_csv('QB_URLS')

    url = x
    html = requests.get(url).content
    df_list = pd.read_html(html)
    df = df_list[0]
    # print(df)
    df.columns = ['Player', 'Game', 'Pts_Given', 'Passing_Att', 'Passing_Cmp', 'Passing_Yds', 'Passing_TD', 'Passing_Int', 'Passing_2Pt', 'Rushing_Att', 'Rushing_Yds', 'Rushing_TD', 'Rushing_2Pt', 'Receiving_Rec', 'Receiving_Yds', 'Receiving_TD',	'Receiving_2Pt', 'Fumbles_FL', \
    'Fumbles_TD', 'X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7']

    df['Player'] = df['Player'].apply(lambda x: x.decode('unicode_escape').\
                                          encode('ascii', 'ignore').\
                                          strip())

    # df['Player_1'] = df.Player.str.split()\
    #         .apply(lambda x: OrderedDict.fromkeys(x).keys()).str.join(' ')
    df.drop(['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7'], axis = 1, inplace = True)

    df['Home'], df['Away'] = df['Game'].str.split('@', 1).str
    df['First_Name'], df['Last'] = df['Player'].str.split(' ', 1).str
    df['NA'], df['Last_Name'] = df['Last'].str.split('.', 1).str
    df.drop(['NA', 'Last'], axis = 1, inplace = True)


    #print df
    #
    # print("file week number")
    w = counter
    v = p
    # print(w)
    df.to_csv('2017_WK'+'%d_%s' % (w, v))

    counter = counter + 1
