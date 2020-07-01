#Script for displaying sequence length plots

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



    
    
def plot(freq, plot_title, range_max):
    plt.figure(figsize=[15,6])
    range = (0, range_max)
    bins = 10
    plt.hist(freq, bins, range, color = 'blue', histtype = 'bar', rwidth = 0.8)
    plt.xlabel('length')
    plt.xticks(np.arange(0, 4000, step=200))
    plt.ylabel('No. of strings')
    plt.title(plot_title)
    plt.savefig("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\"+plot_title+".jpg")
    
    
def makePlot(file_dir, plot_title):
    col_list = ["serial", "sequence"]
    df = pd.read_csv(file_dir, usecols = col_list)
    df['length'] = df.apply(lambda row: len(row.sequence), axis=1)
    max_len = df['length'].max()
    plot(df['length'], plot_title, max_len+200)
    
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_b3_seq.csv", "Genuine User Twitter Type Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b3_seq.csv", "Genuine User Twitter Content B3 Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\genuine_user_content_b6_seq.csv", "Genuine User Twitter Content B6 Seq")

makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_b3_seq.csv", "Bot1 Twitter Type Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_content_b3_seq.csv", "Bot1 Twitter Content B3 Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot1_user_content_b6_seq.csv", "Bot1 Twitter Content B6 Seq")

#bot2_user_b3_seq
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_b3_seq.csv", "Bot2 Twitter Type Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_content_b3_seq.csv", "Bot2 Twitter Content B3 Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot2_user_content_b6_seq.csv", "Bot2 Twitter Content B6 Seq")

makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_b3_seq.csv", "Bot3 Twitter Type Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b3_seq.csv", "Bot3 Twitter Content B3 Seq")
makePlot("E:\\MTech\\2nd_sem\\WSC\\Project\\impl\\bot3_user_content_b6_seq.csv", "Bot3 Twitter Content B6 Seq")

