
import pandas as pd
from itertools import combinations


def findstem(arr):
    n = len(arr)
#    print(arr)
#    print(n)
    s = arr[0]
    l = len(s)
    res = 0
    flag = False
    
    for i in range( l):
        for j in range( i + 1, l + 1):
            stem = s[i:j]
#            print(stem)
            for k in range(1, n):
                if stem not in arr[k]:
                    flag = False
                    break
                else:
                    flag = True
            if flag == True and res < len(stem):
                res = len(stem)
#            if (k + 1 == n and len(res) < len(stem)):
#                res = stem
    return res

def generateLcsLengthList(seq_list):
    list_len = len(seq_list)
    print(list_len)
    seq_lcs_len_list = []
    for r in range(2, list_len+1):
        max_lcs_len = 0
        comb = combinations(seq_list, r)
        print(r)
        for i in list(comb):
            curr_lcs_len = findstem(i)
            if max_lcs_len < curr_lcs_len:
                max_lcs_len = curr_lcs_len
        print(max_lcs_len)
        seq_lcs_len_list.append((r, max_lcs_len))
        print("")
    
    return seq_lcs_len_list
        

def lcsProcessHandler(source_file_path, csv_save_as_name):
    col_list = ["user_id", "sequence"]
    seq_df = pd.read_csv(source_file_path, usecols = col_list)
    seq_list = seq_df['sequence'].tolist()
    lcs_list = generateLcsLengthList(seq_list)
    lcs_list_df = pd.DataFrame(lcs_list, columns =['num_of_strings', 'lcs_length'])
    lcs_list_df.to_csv("csv_save_as_name")


#this commented stub of code is used for testing the functions 
#SA = ["abcd", "ad", "abc", "bcd"]
#m = len(SA)
#test_list = generateLcsLengthList(SA)
#print(test_list)


# call spec: lcsProcessHandler(arg1: full path to seq csv file location, arg2: name for csv file where output will be saved)
#genuine user process lcs
lcsProcessHandler("genuine_user_b3_seq.csv", "user_b3_lcs.csv")
lcsProcessHandler("genuine_user_content_b3_seq.csv", "user_content_b3_lcs.csv")
lcsProcessHandler("genuine_user_content_b6_seq.csv", "user_content_b3_lcs.csv")

#bot1 process lcs
lcsProcessHandler("bot1_user_b3_seq.csv", "bot1_b3_lcs.csv")
lcsProcessHandler("bot1_user_content_b3_seq.csv", "bot1_content_b3_lcs.csv")
lcsProcessHandler("bot1_user_content_b6_seq.csv", "bot1_content_b6_lcs.csv")

#bot2 process lcs
lcsProcessHandler("bot2_user_b3_seq.csv", "bot2_b3_lcs.csv")
lcsProcessHandler("bot2_user_content_b3_seq.csv", "bot2_content_b3_lcs.csv")
lcsProcessHandler("bot2_user_content_b6_seq.csv", "bot2_content_b6_lcs.csv")

#bot3 process lcs
lcsProcessHandler("bot3_user_b3_seq.csv", "bot3_b3_lcs.csv")
lcsProcessHandler("bot3_user_content_b3_seq.csv", "bot3_content_b3_lcs.csv")
lcsProcessHandler("bot3_user_content_b6_seq.csv", "bot3_content_b6_lcs.csv")

