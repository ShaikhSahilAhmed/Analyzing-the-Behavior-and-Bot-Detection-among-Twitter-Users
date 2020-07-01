import pandas as pd


def LCSSubStr(X, Y, m, n):
	LCSuff = [[0 for i in range(n + 1)] 
				for j in range(m + 1)] 

	length = 0
	row, col = 0, 0

	for i in range(m + 1): 
		for j in range(n + 1): 
			if i == 0 or j == 0: 
				LCSuff[i][j] = 0
			elif X[i - 1] == Y[j - 1]: 
				LCSuff[i][j] = LCSuff[i - 1][j - 1] + 1
				if length < LCSuff[i][j]: 
					length = LCSuff[i][j] 
					row = i 
					col = j 
			else: 
				LCSuff[i][j] = 0

	if length == 0: 
		return ""
 
	resultStr = ['0'] * length 

	while LCSuff[row][col] != 0: 
		length -= 1
		resultStr[length] = X[row - 1] 

		row -= 1
		col -= 1

	return (''.join(resultStr))



def findstem(arr):
    n = len(arr)
    
#    i = 0
    j = 1;
    X = arr[0]
    Y = arr[j]
#    xlen = len(X)
#    ylen = len(Y)
    k = 2
    lcs_data = []
    
    while j < n:
        Y = arr[j]
        xlen = len(X)
        ylen = len(Y)
        xySubStr = LCSSubStr(X,Y,xlen,ylen)
        lcs_data.append((k, len(xySubStr)))
        print("\t\tProgress message: k = %d length of lcs = %d" %(k, len(xySubStr)))
        k = k+1
        j = j+1
        X = xySubStr
    
    return lcs_data

    
#this section generates combination of strings for each number of strings. Omitted to get a faster result
#def combinationGenrator(seq_list):
#    m = len(seq_list)
#    lcs_data = []
#    for k in range(1,m):
#        max_lcs_len_i = 0
#        print("\t------------ for k = %d------------" %(k+1))
#        for i in range(0,m-k):
#            seq_arr = []
#            for j in range(0, k+1):
#                seq_arr.append(seq_list[i+j])
##            print("i = ", i)
##            print("seq_arr = ",seq_arr)
#            lcs_len_i = findstem(seq_arr)
#            if max_lcs_len_i < lcs_len_i:
#                max_lcs_len_i = lcs_len_i
##        print("----- k is ", k)
#        lcs_data.append((k+1, max_lcs_len_i))
#        print("\t\tMax LCS length: ",max_lcs_len_i)
#    return lcs_data

#this stub is used for testing the functions
#SA = ["abcd", "ab", "abc", "bcd"]
#SA.sort(key = len, reverse=True)
#res = findstem(SA)
#print(res)


def lcsProcessHandler(source_file_path, save_lcs_data_file_name):
    col_list = ["sequence"]
    seq_df = pd.read_csv(source_file_path, usecols = col_list)
    seq_list = seq_df['sequence'].tolist()
    seq_list.sort(key = len, reverse=True)
    print("================ Findins LCS data for "+source_file_path+" ================")
    lcs_data_list = findstem(seq_list)
    lcs_data_list_df = pd.DataFrame(lcs_data_list, columns =['num_of_strings', 'lcs_length'])
    lcs_data_list_df.to_csv(save_lcs_data_file_name)
    print("LCS process complete for "+source_file_path)
    
    
    
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_b3_lcs.csv")

lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_content_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b6_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_content_b6_lcs.csv")
#genuine user process lcs
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_content_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b6_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_content_b6_lcs.csv")

#bot1 process lcs
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_content_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_content_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_content_b6_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_content_b6_lcs.csv")

#bot2 process lcs
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_content_b3_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_content_b3_lcs.csv")
lcsProcessHandler("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_content_b6_seq.csv", "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_content_b6_lcs.csv")
