#process dataset for bot groups and create sequences

import pandas as pd
import numpy as np


col_list = ["user_id", "in_reply_to_user_id", "retweeted_status_id"]
data = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\dataset\\bot3\\tweets.csv", usecols = col_list)
data.to_csv("bot3_b3_data.csv")

for c in data.columns:
    data[c] = pd.to_numeric(data[c], errors='coerce')

data = data.dropna()
len(data)
data.head()

nrows = data['user_id'].nunique()
print(nrows)

bot_user_seq_list = []
bot_seq_arr = []
bot_user_id_arr = data['user_id'].unique()
bot_user_group = data.groupby(['user_id'])

print(bot_user_id_arr[2])
print(len(bot_user_id_arr))


for i in range(0,nrows):
    s = ""
    curr_user_grp = bot_user_group.get_group(bot_user_id_arr[i])
    for row in curr_user_grp.itertuples():
        print(row.user_id)
        if row.in_reply_to_user_id != 0.0:
            s = s + "C"
        elif row.retweeted_status_id != 0.0:
            s = s + "T"
        else:
            s = s + "A"
    print(s)
    print("--------------------------")
    bot_user_seq_list.append((bot_user_id_arr[i], s))
    bot_seq_arr.append(s)

longest_seq = max(bot_seq_arr, key = len)
print(len(longest_seq))
shortest_seq = min(bot_seq_arr, key = len)
print(len(shortest_seq))

bot_seq_df = pd.DataFrame(bot_user_seq_list, columns =['user_id', 'sequence'])
bot_seq_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_b3_seq.csv")

#--------------------------------------------------------------------------------#
#----------------------------- Content type -------------------------------------#

import pandas as pd

col_list2 = ["user_id", "num_hashtags", "num_urls", "num_mentions"]
data2 = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\dataset\\bot3\\tweets.csv", usecols = col_list2)
data2.to_csv("bot3_user_content_data.csv", header=['user_id', 'num_hashtags', 'num_urls', 'num_mentions'])

for c in data2.columns:
    data2[c] = pd.to_numeric(data2[c], errors='coerce')

data2['num_hashtags'].fillna(0, inplace=True)
data2['num_urls'].fillna(0, inplace=True)
data2['num_mentions'].fillna(0, inplace=True)
data2 = data2.dropna()

data2.head()
len(data2)

nrows2 = data2['user_id'].nunique()
print(nrows2)

bot_user_content_seq_list = []
bot_content_seq_arr = []
bot_user_id_content_arr = data2['user_id'].unique()
bot_user_content_group = data2.groupby(['user_id'])

print(bot_user_id_content_arr[2])
print(len(bot_user_id_content_arr))


for i in range(0,nrows2):
    s = ""
    curr_user_grp = bot_user_content_group.get_group(bot_user_id_content_arr[i])
    for row in curr_user_grp.itertuples():
        print(row.user_id)
        if row.num_hashtags == 0.0 and row.num_urls == 0.0 and row.num_mentions == 0.0:
            s = s + "N"
        elif row.num_hashtags != 0.0 and row.num_urls == 0.0 and row.num_mentions == 0.0:
            s = s + "E"
        elif row.num_hashtags == 0.0 and row.num_urls != 0.0 and row.num_mentions == 0.0:
            s = s + "E"
        elif row.num_hashtags == 0.0 and row.num_urls == 0.0 and row.num_mentions != 0.0:
            s = s + "E"
        else:
            s = s + "X"
        
    print(s)
    print("--------------------------")
    bot_user_content_seq_list.append((bot_user_id_content_arr[i], s))
    bot_content_seq_arr.append(s)

longest_seq2 = max(bot_content_seq_arr, key = len)
print(len(longest_seq2))
shortest_seq2 = min(bot_content_seq_arr, key = len)
print(len(shortest_seq2))

bot_content_seq_df = pd.DataFrame(bot_user_content_seq_list, columns =['user_id', 'sequence'])
bot_content_seq_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b3_seq.csv")



bot_user_content_seq_b6_list = []
bot_content_seq_b6_arr = []

print(bot_user_id_content_arr[2])
print(len(bot_user_id_content_arr))

for i in range(0,nrows2):
    s = ""
    curr_user_grp = bot_user_content_group.get_group(bot_user_id_content_arr[i])
    for row in curr_user_grp.itertuples():
        print(row.user_id)
        if row.num_hashtags == 0.0 and row.num_urls == 0.0 and row.num_mentions == 0.0:
            s = s + "N"
        elif row.num_hashtags != 0.0 and row.num_urls == 0.0 and row.num_mentions == 0.0:
            s = s + "H"
        elif row.num_hashtags == 0.0 and row.num_urls != 0.0 and row.num_mentions == 0.0:
            s = s + "U"
        elif row.num_hashtags == 0.0 and row.num_urls == 0.0 and row.num_mentions != 0.0:
            s = s + "M"
        else:
            s = s + "X"
        
    print(s)
    print("--------------------------")
    bot_user_content_seq_b6_list.append((bot_user_id_content_arr[i], s))
    bot_content_seq_b6_arr.append(s)

longest_seq3 = max(bot_content_seq_b6_arr, key = len)
print(len(longest_seq3))
shortest_seq3 = min(bot_content_seq_b6_arr, key = len)
print(len(shortest_seq3))

bot_content_seq_b6_df = pd.DataFrame(bot_user_content_seq_b6_list, columns =['user_id', 'sequence'])
bot_content_seq_b6_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b6_seq.csv")
