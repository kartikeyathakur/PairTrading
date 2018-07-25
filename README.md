# PairTrading
This simple python script (df_no_factors.py) checks all the pairs in the SNP500 index for cointegration using the Augmented Dickey Fuller test and performs a performance analysis on the cointegrated pairs. 

The time series data has been obtained using the Kaggle dataset and code at https://www.kaggle.com/camnugent/sandp500 . Many thanks. This data is in the file named quandl.csv. It can be found at https://drive.google.com/open?id=1dvM7k-jauLHPyea-I7kTd3LRDADfLaMs . I cannot upload this to the repository as it is more than 25 MB. 

The results can be found at https://drive.google.com/open?id=1jXEDXwUtfAZ8VkpY1wGA4kYVcojV-QMV . I cannot add them to the repository as they are bigger than 25 MB. The results are from an anlysis performed in May 2018. I have separed pairs into 3 groups. One has pairs with positive Cumulative returns and sharpe ratios, one has pairs with negative cumulative returns and sharp ratios and one has pairs with either a negative sharpe ratio or a neagtive cumulative return.

Also, I have created pairs where sectors were same for both the stocks to see if pairs in the same sector perform better compared to the others. The files with 'unbound' in their names do not have this constraint. In these pairs ignore the sector names as they are just the sector of the first stock in the pair.

Additionally, I performed a correlation analysis and bucketed the pairs in 5 buckets based on correlation to see if correlation had any effect on profits in a apir trading strategy. The buckets are -1.0 to 0.5, 05 to 0.8, 0.8 to 0.9 and 0.9 to 0.97 and 0.97 to 1.0. These have names like lowest, low, meduim, high and highest and if you see these words in the results they are nothing but the bucket of correlation in which they fall.

Conintegration and correlation checks are done for the first three years of data and the performance analysis on the latest two years of data.
