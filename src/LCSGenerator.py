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

SA = ["abcd", "ab", "abc", "bcd"]
#m = len(SA)
#test_list = generateLcsLengthList(SA)
#print(test_list)
    

def combinationGenrator(seq_list):
    m = len(seq_list)
    lcs_data = []
    for k in range(1,m):
        max_lcs_len_i = 0
        print("\t------------ for k = %d------------" %(k))
        for i in range(0,m-k):
            seq_arr = []
            for j in range(0, k+1):
                seq_arr.append(seq_list[i+j])
#            print("i = ", i)
#            print("seq_arr = ",seq_arr)
            lcs_len_i = findstem(seq_arr)
            if max_lcs_len_i < lcs_len_i:
                max_lcs_len_i = lcs_len_i
#        print("----- k is ", k)
        lcs_data.append((k+1, max_lcs_len_i))
        print("\t\tMax LCS length: ",max_lcs_len_i)
    return lcs_data

SA.sort(key = len, reverse=True)
res = combinationGenrator(SA)
print(res)


def lcsProcessHandler(source_file_path, save_lcs_data_file_name):
    col_list = ["sequence"]
    seq_df = pd.read_csv(source_file_path, usecols = col_list)
    seq_list = seq_df['sequence'].tolist()
    seq_list.sort(key = len, reverse=True)
    print("================ Findins LCS data for "+source_file_path+" ================")
    lcs_data_list = combinationGenrator(seq_list)
    lcs_data_list_df = pd.DataFrame(lcs_data_list, columns =['num_of_strings', 'lcs_length'])
    lcs_data_list_df.to_csv("save_lcs_data_file_name")
    print("LCS process complete for "+source_file_path)
    
    
##change file name and location here. Do it for genuine user seq. I am doing bot2    
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_b3_seq.csv", "bot2_b3_lcs.csv")
# call spec: lcsProcessHandler(arg1: full path to seq csv file location, arg2: name for csv file where output will be saved)
#genuine user process lcs
#lcsProcessHandler("genuine_user_b3_seq.csv", "user_b3_lcs.csv")
#lcsProcessHandler("genuine_user_content_b3_seq.csv", "user_content_b3_lcs.csv")
#lcsProcessHandler("genuine_user_content_b6_seq.csv", "user_content_b3_lcs.csv")
