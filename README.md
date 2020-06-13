# PairTrading
This simple python script (df_no_factors.py) checks all the possible pairs in the SNP500 index for cointegration using the Augmented Dickey Fuller test and performs a performance analysis on the cointegrated pairs - returns if one was trading the said pair. 

The time series data has been obtained using the Kaggle dataset and code at https://www.kaggle.com/camnugent/sandp500 . Many thanks. This data is in the file named quandl.csv. Just keep the py file and the csv in the same repository and do not change any names. Run the py file and you are good to go. Since there are more than 100,000 possible pairs the script takes some time to run. Could be a couple of hours but after that you have all the results and you just need to analyze them to get your performance analysis.

I have separated pairs into 3 groups. One has pairs with positive Cumulative returns and sharpe ratios, the other has pairs with negative cumulative returns and sharp ratios and the third category has pairs with either a negative sharpe ratio or a neagtive cumulative return.

Also, I have restricted pairs within the same sector to see if pairs in the same sector perform better compared to the others. The files with 'unbound' in their names do not have this constraint. In these pairs ignore the sector names as they are just the sector of the first stock in the pair.

Additionally, I performed a correlation analysis and bucketed the pairs in 5 buckets based on correlation to see if correlation had any effect on profits in a pair trading strategy. The buckets are -1.0 to 0.5, 05 to 0.8, 0.8 to 0.9 and 0.9 to 0.97 and 0.97 to 1.0. These have names like lowest, low, meduim, high and highest and if you see these words in the results they are nothing but the bucket of correlation in which they fall.

Conintegration and correlation checks are done for the first three years of data and the performance analysis on the latest two years of data.
