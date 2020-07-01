#process dataset for genuine users and create sequences

import pandas as pd
import numpy as np


data = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\dataset\\tweets.csv", usecols = [3,6,8])
data.to_csv("genuine_user_b3_data.csv", header=['user_id', 'in_reply_to_user_id', 'retweeted_status_id'])

col_list = ["user_id", "in_reply_to_user_id", "retweeted_status_id"]
df = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_b3_data.csv", usecols = col_list)
print(df.head())
for c in df.columns:
    df[c] = pd.to_numeric(df[c], errors='coerce')

df.to_csv("genuine_user_b3_data.csv")
df = df.dropna()

nrows = df['user_id'].nunique()
print(nrows)

user_seq_list = []
seq_arr = []
user_id_arr = df['user_id'].unique()
user_group = df.groupby(['user_id'])

print(user_id_arr[2])
print(len(user_id_arr))


for i in range(0,nrows):
    s = ""
    curr_user_grp = user_group.get_group(user_id_arr[i])
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
    user_seq_list.append((user_id_arr[i], s))
    seq_arr.append(s)

longest_seq = max(seq_arr, key = len)
print(len(longest_seq))
shortest_seq = min(seq_arr, key = len)
print(len(shortest_seq))

seq_df = pd.DataFrame(user_seq_list, columns =['user_id', 'sequence'])
seq_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_b3_seq.csv")

#-------------------------------------------------------------------#
#----------------------------- content type ------------------------#
import pandas as pd
data2 = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\dataset\\tweets.csv", usecols = [3,18,19,20])
data2.to_csv("genuine_user_content_data.csv", header=['user_id', 'num_hashtags', 'num_urls', 'num_mentions'])

col_list2 = ["user_id", "num_hashtags", "num_urls", "num_mentions"]
df2 = pd.read_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_data.csv", usecols = col_list2)

print(df2.head())

for c in df2.columns:
    df2[c] = pd.to_numeric(df2[c], errors='coerce')

#df2 = df2.dropna()
df2['num_hashtags'].fillna(0, inplace=True)
df2['num_urls'].fillna(0, inplace=True)
df2['num_mentions'].fillna(0, inplace=True)

df2.to_csv("genuine_user_content_data.csv")
df2 = df2.dropna()

nrows2 = df2['user_id'].nunique()
print(nrows2)


user_content_seq_list = []
content_seq_arr = []
user_id_content_arr = df2['user_id'].unique()
user_content_group = df2.groupby(['user_id'])

print(user_id_content_arr[2])
print(len(user_id_content_arr))


for i in range(0,nrows2):
    s = ""
    curr_user_grp = user_content_group.get_group(user_id_content_arr[i])
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
    user_content_seq_list.append((user_id_content_arr[i], s))
    content_seq_arr.append(s)

longest_seq2 = max(content_seq_arr, key = len)
print(len(longest_seq2))
shortest_seq2 = min(content_seq_arr, key = len)
print(len(shortest_seq2))

content_seq_df = pd.DataFrame(user_content_seq_list, columns =['user_id', 'sequence'])
content_seq_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b3_seq.csv")


user_content_seq_b6_list = []
content_seq_b6_arr = []

print(user_id_content_arr[2])
print(len(user_id_content_arr))

for i in range(0,nrows2):
    s = ""
    curr_user_grp = user_content_group.get_group(user_id_content_arr[i])
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
    user_content_seq_b6_list.append((user_id_content_arr[i], s))
    content_seq_b6_arr.append(s)

longest_seq3 = max(content_seq_b6_arr, key = len)
print(len(longest_seq3))
shortest_seq3 = min(content_seq_b6_arr, key = len)
print(len(shortest_seq3))

content_seq_b6_df = pd.DataFrame(user_content_seq_b6_list, columns =['user_id', 'sequence'])
content_seq_b6_df.to_csv("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b6_seq.csv")









