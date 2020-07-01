#Script for displaying the LCS plots


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def plot(x, y, plot_title):
    plt.figure(figsize=(9, 6))
    plt.plot(x, y, label='Data')
    plt.xlabel('no. of strings')
    plt.ylabel('length')
    plt.title(plot_title)   
    plt.show()
    plt.savefig("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\"+plot_title+".jpg")
    

def makePlot(file_dir, plot_title):
    col_list = ["num_of_strings", "lcs_length"]
    df = pd.read_csv(file_dir, usecols = col_list)
    print(df.head())
    plot(df['num_of_strings'], df['lcs_length'], plot_title)
    

makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_b3_lcs.csv", "Genuine User Twitter Type LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_content_b3_lcs.csv", "Genuine User Twitter Content B3 LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\user_content_b6_lcs.csv", "Genuine User Twitter Content B6 LCS Plot")

makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_b3_lcs.csv", "Bot1 Twitter Type LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_content_b3_lcs.csv", "Bot1 Twitter Content B3 LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_content_b6_lcs.csv", "Bot1 Twitter Content B6 LCS Plot")

#bot2_user_b3_seq
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_b3_lcs.csv", "Bot2 Twitter Type LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_content_b3_lcs.csv", "Bot2 Twitter Content B3 LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_content_b6_lcs.csv", "Bot2 Twitter Content B6 LCS Plot")

makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_b3_lcs.csv", "Bot3 Twitter Type lCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_content_b3_lcs.csv", "Bot3 Twitter Content B3 LCS Plot")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_content_b6_lcs.csv", "Bot3 Twitter Content B6 LCS Plot")

