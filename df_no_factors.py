#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  5 03:49:58 2018

@author: KartikeyaThakur
"""


import csv
from pandas import Series
import numpy as np
from statsmodels.tsa.stattools import adfuller

count = 0
""" list of s_anp_p companies """
s_and_p = ['MMM','ABT','ABBV','ACN','ATVI','AYI','ADBE','AMD','AAP','AES','AET',
		'AMG','AFL','A','APD','AKAM','ALK','ALB','ARE','ALXN','ALGN','ALLE',
		'AGN','ADS','LNT','ALL','GOOGL','GOOG','MO','AMZN','AEE','AAL','AEP',
		'AXP','AIG','AMT','AWK','AMP','ABC','AME','AMGN','APH','APC','ADI','ANDV',
		'ANSS','ANTM','AON','AOS','APA','AIV','AAPL','AMAT','APTV','ADM','ARNC',
		'AJG','AIZ','T','ADSK','ADP','AZO','AVB','AVY','BHGE','BLL','BAC','BK',
		'BAX','BBT','BDX','BRK.B','BBY','BIIB','BLK','HRB','BA','BWA','BXP','BSX',
		'BHF','BMY','AVGO','BF.B','CHRW','CA','COG','CDNS','CPB','COF','CAH','CBOE',
		'KMX','CCL','CAT','CBG','CBS','CELG','CNC','CNP','CTL','CERN','CF','SCHW',
		'CHTR','CHK','CVX','CMG','CB','CHD','CI','XEC','CINF','CTAS','CSCO','C','CFG',
		'CTXS','CLX','CME','CMS','KO','CTSH','CL','CMCSA','CMA','CAG','CXO','COP',
		'ED','STZ','COO','GLW','COST','COTY','CCI','CSRA','CSX','CMI','CVS','DHI',
		'DHR','DRI','DVA','DE','DAL','XRAY','DVN','DLR','DFS','DISCA','DISCK','DISH',
		'DG','DLTR','D','DOV','DWDP','DPS','DTE','DRE','DUK','DXC','ETFC','EMN','ETN',
		'EBAY','ECL','EIX','EW','EA','EMR','ETR','EVHC','EOG','EQT','EFX','EQIX','EQR',
		'ESS','EL','ES','RE','EXC','EXPE','EXPD','ESRX','EXR','XOM','FFIV','FB','FAST',
		'FRT','FDX','FIS','FITB','FE','FISV','FLIR','FLS','FLR','FMC','FL','F','FTV',
		'FBHS','BEN','FCX','GPS','GRMN','IT','GD','GE','GGP','GIS','GM','GPC','GILD',
		'GPN','GS','GT','GWW','HAL','HBI','HOG','HRS','HIG','HAS','HCA','HCP','HP','HSIC',
		'HSY','HES','HPE','HLT','HOLX','HD','HON','HRL','HST','HPQ','HUM','HBAN','HII',
		'IDXX','INFO','ITW','ILMN','IR','INTC','ICE','IBM','INCY','IP','IPG','IFF','INTU',
		'ISRG','IVZ','IQV','IRM','JEC','JBHT','SJM','JNJ','JCI','JPM','JNPR','KSU','K','KEY',
		'KMB','KIM','KMI','KLAC','KSS','KHC','KR','LB','LLL','LH','LRCX','LEG','LEN','LUK',
		'LLY','LNC','LKQ','LMT','L','LOW','LYB','MTB','MAC','M','MRO','MPC','MAR','MMC','MLM',
		'MAS','MA','MAT','MKC','MCD','MCK','MDT','MRK','MET','MTD','MGM','KORS','MCHP','MU',
		'MSFT','MAA','MHK','TAP','MDLZ','MON','MNST','MCO','MS','MOS','MSI','MYL','NDAQ',
		'NOV','NAVI','NTAP','NFLX','NWL','NFX','NEM','NWSA','NWS','NEE','NLSN','NKE','NI',
		'NBL','JWN','NSC','NTRS','NOC','NCLH','NRG','NUE','NVDA','ORLY','OXY','OMC','OKE',
		'ORCL','PCAR','PKG','PH','PDCO','PAYX','PYPL','PNR','PBCT','PEP','PKI','PRGO','PFE',
		'PCG','PM','PSX','PNW','PXD','PNC','RL','PPG','PPL','PX','PCLN','PFG','PG','PGR',
		'PLD','PRU','PEG','PSA','PHM','PVH','QRVO','PWR','QCOM','DGX','RRC','RJF','RTN','O',
		'RHT','REG','REGN','RF','RSG','RMD','RHI','ROK','COL','ROP','ROST','RCL','CRM','SBAC',
		'SCG','SLB','SNI','STX','SEE','SRE','SHW','SIG','SPG','SWKS','SLG','SNA','SO','LUV',
		'SPGI','SWK','SBUX','STT','SRCL','SYK','STI','SYMC','SYF','SNPS','SYY','TROW','TPR',
		'TGT','TEL','FTI','TXN','TXT','TMO','TIF','TWX','TJX','TMK','TSS','TSCO','TDG','TRV',
		'TRIP','FOXA','FOX','TSN','UDR','ULTA','USB','UAA','UA','UNP','UAL','UNH','UPS','URI',
		'UTX','UHS','UNM','VFC','VLO','VAR','VTR','VRSN','VRSK','VZ','VRTX','VIAB','V','VNO',
		'VMC','WMT','WBA','DIS','WM','WAT','WEC','WFC','HCN','WDC','WU','WRK','WY','WHR','WMB',
		'WLTW','WYN','WYNN','XEL','XRX','XLNX','XL','XYL','YUM','ZBH','ZION','ZTS']
dat = {}

for comp in s_and_p:
    dat[comp] = ([],"")

with open('quandl.csv', 'r') as csvfile:
    all_data = csv.reader(csvfile, delimiter=',')
    next(all_data, None) 
    for row in all_data:
        if row[-2] in s_and_p:
            dat[row[-2]][0].append(float(row[-4]))
            if dat[row[-2]][1] == "":
                dat[row[-2]] = (dat[row[-2]][0],str(row[-1]))
        

new_s_and_p = {}
cleaned = []
for comp in s_and_p:
    if len(dat[comp][0])<1259:
        cleaned.append(comp)
    else:
        new_s_and_p[comp] = dat[comp]
        
print("Removed ", len(cleaned), " tickers with incomplete data.")
print(cleaned)

coeff = {}

for comp in new_s_and_p:
    coeff[comp] = []

for comp1 in new_s_and_p:
    count = 0
    coeffs = {}
    for comp2 in new_s_and_p:
        if(s_and_p.index(comp1)<s_and_p.index(comp2)):
            nums = []
            for i in range (0, len(new_s_and_p[comp1][0])):
                nums.append(new_s_and_p[comp1][0][i]-new_s_and_p[comp2][0][i])
            series = Series.from_array(nums[0:755])
            X = series.values
            result = adfuller(X)
            coeffs[comp2] = (np.corrcoef(new_s_and_p[comp1][0][0:755],new_s_and_p[comp2][0][0:755])[0][1], result[0], new_s_and_p[comp1][1]) 
                
    coeff[comp1] = coeffs
    
print("Done with Coeffs. Now selecting pairs.")
pairs_0_50 = []
pairs_50_80 = []
pairs_80_90 = []
pairs_90_97 = []
pairs_97_100 = []
for comp1 in coeff.keys():
    for comp2 in coeff[comp1].keys():
        if coeff[comp1][comp2][1]<-2.579 and coeff[comp1][comp2][0] <.5:
            pairs_0_50.append((comp1,comp2,coeff[comp1][comp2][2]))
        elif coeff[comp1][comp2][1]<-2.579 and coeff[comp1][comp2][0] >=.5 and coeff[comp1][comp2][0] <.80:
            pairs_50_80.append((comp1,comp2,coeff[comp1][comp2][2]))
        elif coeff[comp1][comp2][1]<-2.579 and coeff[comp1][comp2][0] >=.80 and coeff[comp1][comp2][0] <.90:
            pairs_80_90.append((comp1,comp2,coeff[comp1][comp2][2]))
        elif coeff[comp1][comp2][1]<-2.579 and coeff[comp1][comp2][0] >=.90 and coeff[comp1][comp2][0] <.97:
            pairs_90_97.append((comp1,comp2,coeff[comp1][comp2][2]))
        elif coeff[comp1][comp2][1]<-2.579 and coeff[comp1][comp2][0] >=.97 and coeff[comp1][comp2][0] <1.0:
            pairs_97_100.append((comp1,comp2,coeff[comp1][comp2][2]))

all = {"lowest": pairs_0_50, "low":pairs_50_80, "medium":pairs_80_90, "high":pairs_90_97, "highest":pairs_97_100}
count = 0
dat = {}
longEntryThr = -1
longCap = 0.5
shortEntryThr = 1
shortCap = -0.5
holdingPeriod = 5
done_pair = []
result = ""
pos_result = ""
neg_result = ""
mixed_result = ""

for comp in s_and_p:
    dat[comp] = []

with open('quandl.csv', 'r') as csvfile:
    all_data = csv.reader(csvfile, delimiter=',')
    next(all_data, None) 
    for row in all_data:
        if row[-2] in s_and_p:
            dat[row[-2]].append(float(row[-4]))
        

new_s_and_p = []
cleaned = []
for comp in s_and_p:
    if len(dat[comp])<1259:
        cleaned.append(comp)
    else:
        #removing the values used to do the cointegration and correlation analysis
        new_s_and_p.append(comp)
        dat[comp] = dat[comp][755:]
        
print("Removed ", len(cleaned), " tickers with incomplete data.")
#print(cleaned)

for key in all.keys():
    for pair in all[key]:
#pair = ('AET', 'ISRG', 'Healthcare')
#if pair in all['lowest']:
    #if pair in all['lowest']:
        in_market = 0
        short_pos = 0
        equity_curve = float(100)
        ret = []
        f_ret = []
        a_ret = []
        b_ret = []
        zdiff = []
        signal = []
        lCap5 = []
        sCap5 =[]
        age = [0]   #should be -1 indexed
        aged = []
        pos = [0]   #should be -1 indexed
        for i in range (5,504):
            a_ret.append((dat[pair[0]][i]-dat[pair[0]][i-5])/dat[pair[0]][i-5])
            b_ret.append((dat[pair[1]][i]-dat[pair[1]][i-5])/dat[pair[1]][i-5])
        for j in range (59,498):
            zdiff.append(a_ret[j+1]/np.std(a_ret[0:j+1])-b_ret[j+1]/np.std(b_ret[0:j+1]))
        for k in range (65,503):
            f_ret.append((dat[pair[0]][k+1]-dat[pair[0]][k])/dat[pair[0]][k]-(dat[pair[1]][k+1]-dat[pair[1]][k])/dat[pair[1]][k])
        for l in range (0,len(zdiff)):
            if zdiff[l] < longEntryThr:
                signal.append(1)
            elif zdiff[l] > shortEntryThr:
                signal.append(-1)
            else:
                signal.append(0)
            
            if pos[l] == 1 and zdiff[l] > longCap:
                lCap5.append(1)
            else:
                lCap5.append(0)
            if pos[l] == -1 and zdiff[l] < shortCap:
                sCap5.append(1)
            else:
                sCap5.append(0)
            
            if signal[l]!=0:
                if pos[l] == 0:
                    age.append(1)
                else:
                    if pos[l]+signal[l] == 0:
                        age.append(1)
                    else:
                        #check here if age should be age + 1
                        age.append(1)
            else:
                if age[l] == 5:
                    age.append(0)
                else:
                    if pos[l] == 1 and lCap5[l] != 0 or pos[l] == -1 and sCap5[l] != 0:
                        age.append(0)
                    else:
                        if signal[l] + pos[l] != 0:
                            age.append(age[l] + 1)
                        else:
                            age.append(0)
            
            if age[l] == 5:
                if signal[l] == 0:
                    aged.append(1)
                else:
                    aged.append(0)
            else:
                aged.append(0)
            
            if signal[l] == 0:
                if aged[l] + sCap5[l] + lCap5[l] == 0:
                    pos.append(pos[l])
                else:
                    if aged[l] + sCap5[l] > 0 and pos[l] == -1:
                        pos.append(0)
                    elif aged[l] + lCap5[l] > 0 and pos[l] == 1:
                        pos.append(0)
                    else:
                        pos.append(pos[l])
            else:
                if signal[l]!=pos[l]:
                    pos.append(signal[l])
                else:
                    if aged[l] + sCap5[l] + lCap5[l] == 0:
                        pos.append(signal[l])
                    else:
                        if aged[l] + sCap5[l] > 0 and pos[l] == -1  and signal[l] == -1:
                            pos.append(0)
                        elif aged[l] + lCap5[l] > 0 and pos[l] == 1 and signal[l] == 1:
                            pos.append(0)
                        else:
                            pos.append(signal[l])
        count = 0
        for m in range(1,len(pos)-1):
            if(pos[m]*f_ret[m-1]>0):
                count = count + 1
            elif (pos[m]*f_ret[m-1]<0):
                count = count -1
            ret.append(pos[m]*f_ret[m-1])
            equity_curve = equity_curve*(1+pos[m]*f_ret[m-1])
            if pos[m]!=0:
                in_market = in_market + 1
            if pos[m]==-1:
                short_pos = short_pos + 1
        details = {}
        details["Sharpe"] = np.sqrt(260)*np.mean(ret)/np.std(ret)
        details["CumRet"] = (equity_curve-100)/100
        details["In_market"] = in_market/440
        details["Short"] = short_pos/440
        done_pair.append((pair[0], pair[1], pair[2], key, details))
        if details["Sharpe"]>0 and details["CumRet"]>0:
            pos_result = pos_result  + str(done_pair[-1]) + "\n\n"
        elif details["Sharpe"]<0 and details["CumRet"]<0:
            neg_result = neg_result  + str(done_pair[-1]) + "\n\n"
        else:
            mixed_result = mixed_result  + str(done_pair[-1]) + "\n\n"
        result = result + str(done_pair[-1]) + "\n\n"
        
file = open('unbound_analysis.txt', 'w')
file.write(result)
file.close()

file = open('pos_unbound_analysis.txt', 'w')
file.write(pos_result)
file.close()

file = open('neg_unbound_analysis.txt', 'w')
file.write(neg_result)
file.close()

file = open('mixed_unbound_analysis.txt', 'w')
file.write(mixed_result)
file.close()
