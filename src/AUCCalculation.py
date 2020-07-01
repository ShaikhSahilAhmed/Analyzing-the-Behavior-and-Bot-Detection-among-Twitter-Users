# -*- coding: utf-8 -*-
"""
AUC calculation

@author: Kushal
"""
import pandas as pd



def calculate_auc(x_range, a, b, c):
    t1 = x_range[0]
    t2 = x_range[len(x_range)-1]
    print("t1 = ",t1)
    print("t2 = ",t2)
    auc = (a/(1-b)) * (pow(t2, 1-b) - pow(t1, 1-b)) + c * (t2 - t1)
    return auc



# bot1 b3 LCSs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot1_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 1.26673412*1000
b = 9.10666138/10
c = -2.89101426

bot1_b3_lcs_auc = calculate_auc(x_range, a,b,c)


# bot1_content_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot1_content_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 477.33106927
b = 2.25318785
c = 0.98916567

bot1_content_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#bot1_content_b6_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot1_content_b6_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 2.36681544*100
b = 9.11458069*10
c = 2.14141497/10

bot1_content_b6_lcs_auc = calculate_auc(x_range, a,b,c)


#bot2_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot2_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 252.35969492
b = 80.3845435
c = 2.72222221

bot2_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#bot2_content_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot2_content_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 40.25927765
b = 1.02371112
c = 1.06153093

bot2_content_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#bot2_content_b6_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot2_content_b6_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 2.83572771*1000
b = 7.01078904
c = 3.04038695/1000

bot2_content_b6_lcs_auc = calculate_auc(x_range, a,b,c)


#bot3_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot3_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 8.68028893*1000
b = 3.35658518/10
c = -1.34485178*1000

bot3_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#bot3_content_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot3_content_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 34.90371667
b = 0.31338239
c = -5.93285711

bot3_content_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#bot3_content_b6_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\bot3_content_b6_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 34.90371667
b = 0.31338239
c = -5.93285711

bot3_content_b6_lcs_auc = calculate_auc(x_range, a,b,c)


#user_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\user_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 30.58216252
b = 0.58492169
c = 1.35090249

user_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#user_content_b3_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\user_content_b3_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 6.66004816
b = 0.83897044
c = -0.01912371

user_content_b3_lcs_auc = calculate_auc(x_range, a,b,c)


#user_content_b6_lcs
col_list = ['num_of_strings']
source_file_path = "E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\phase2\\user_content_b6_lcs.csv"
df = pd.read_csv(source_file_path, usecols = col_list)
x_range = df['num_of_strings']

a = 6.66004816
b = 0.83897044
c = -0.01912371

user_content_b6_lcs_auc = calculate_auc(x_range, a,b,c)


avg_bot1_auc = (bot1_b3_lcs_auc + bot1_content_b3_lcs_auc + bot1_content_b6_lcs_auc)/3
avg_bot2_auc = (bot2_b3_lcs_auc + bot2_content_b3_lcs_auc + bot2_content_b6_lcs_auc)/3
avg_bot3_auc = (bot3_b3_lcs_auc + bot3_content_b3_lcs_auc + bot3_content_b6_lcs_auc)/3
avg_user_auc = (user_b3_lcs_auc + user_content_b3_lcs_auc + user_content_b6_lcs_auc)/3


















