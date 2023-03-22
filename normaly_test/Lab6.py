#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
import seaborn as sns
from statsmodels.graphics.gofplots import qqplot
from scipy.stats import shapiro
from scipy.stats import normaltest
from scipy.stats import anderson

data=pd.read_csv("borsaVerileri.csv")
data

#Görsel Normallik Testleri
"""data.Bist100.plot.hist(bins=100)
sns.histplot(x=data.Bist100, bins=100, kde=True)
qqplot(data.Bist100, line="s")
"""
#İstatistiksel Normallik Testleri

#Shapiro
istatistik1, pdegeri1=shapiro(data.Bist100)
pdegeri1
alfa=0.05
if(pdegeri1>alfa):
    print("Veriler normal dağılıma uygundur.")
else:
    print("Veriler normal dağılıma uygun değildir.")

#D'Agostino
istatistik2, pdegeri2=normaltest(data.Bist100)
pdegeri2
alfa=0.05
if(pdegeri2>alfa):
    print("Veriler normal dağılıma uygundur.")
else:
    print("Veriler normal dağılıma uygun değildir.")

#Anderson
sonuc=anderson(data.Bist100)
sonuc
for i in range(len(sonuc.critical_values)):
    a,b=sonuc.significance_level[i],sonuc.critical_values[i]
    if(sonuc.statistic<sonuc.critical_values[i]):
        print("Veriler normal dağılıma uygundur.")
    else:
        print("Veriler normal dağılıma uygun değildir.")

        
#Aykırı Değerlerin Bulunması ve Kaldırılması

#BIST100
Q1=np.percentile(data.Bist100,25,interpolation="midpoint")
Q3=np.percentile(data.Bist100,75,interpolation="midpoint")
IQR1=Q3-Q1
IQR1

üst1=np.where(data.Bist100>=(Q3+1.5*IQR1))
alt1=np.where(data.Bist100<=(Q1-1.5*IQR1))
_bist100=data.Bist100
_bist100.drop(üst1[0],inplace=True)
_bist100.drop(alt1[0],inplace=True)

#BOVESPA
Q1=np.percentile(data.Bovespa,25,interpolation="midpoint")
Q3=np.percentile(data.Bovespa,75,interpolation="midpoint")
IQR2=Q3-Q1
IQR2

üst2=np.where(data.Bovespa>=(Q3+1.5*IQR2))
alt2=np.where(data.Bovespa<=(Q1-1.5*IQR2))
_Bovespa=data.Bovespa
_Bovespa.drop(üst2[0],inplace=True)
_Bovespa.drop(alt2[0],inplace=True)

#ITALY40
Q1=np.percentile(data.italy40,25,interpolation="midpoint")
Q3=np.percentile(data.italy40,75,interpolation="midpoint")
IQR3=Q3-Q1
IQR3

üst3=np.where(data.italy40>=(Q3+1.5*IQR3))
alt3=np.where(data.italy40<=(Q1-1.5*IQR3))
_italy40=data.italy40
_italy40.drop(üst3[0],inplace=True)
_italy40.drop(alt3[0],inplace=True)

#KOSPI
Q1=np.percentile(data.KOSPI,25,interpolation="midpoint")
Q3=np.percentile(data.KOSPI,75,interpolation="midpoint")
IQR4=Q3-Q1
IQR4

üst4=np.where(data.KOSPI>=(Q3+1.5*IQR4))
alt4=np.where(data.KOSPI<=(Q1-1.5*IQR4))
_KOSPI=data.KOSPI
_KOSPI.drop(üst4[0],inplace=True)
_KOSPI.drop(alt4[0],inplace=True)

#NIKKEI
Q1=np.percentile(data.Nikkei,25,interpolation="midpoint")
Q3=np.percentile(data.Nikkei,75,interpolation="midpoint")
IQR5=Q3-Q1
IQR

üst5=np.where(data.Nikkei>=(Q3+1.5*IQR5))
alt5=np.where(data.Nikkei<=(Q1-1.5*IQR5))
_Nikkei=data.Nikkei
_Nikkei.drop(üst5[0],inplace=True)
_Nikkei.drop(alt5[0],inplace=True)


#BMVIIPC
Q1=np.percentile(data.BMVIIPC,25,interpolation="midpoint")
Q3=np.percentile(data.BMVIIPC,75,interpolation="midpoint")
IQR6=Q3-Q1
IQR6

üst6=np.where(data.BMVIIPC>=(Q3+1.5*IQR6))
alt6=np.where(data.BMVIIPC<=(Q1-1.5*IQR6))
_BMVIIPC=data.BMVIIPC
_BMVIIPC.drop(üst6[0],inplace=True)
_BMVIIPC.drop(alt6[0],inplace=True)


#SHANGHAI
Q1=np.percentile(data.Shanghai,25,interpolation="midpoint")
Q3=np.percentile(data.Shanghai,75,interpolation="midpoint")
IQR7=Q3-Q1
IQR7

üst7=np.where(data.Shanghai>=(Q3+1.5*IQR7))
alt7=np.where(data.Shanghai<=(Q1-1.5*IQR7))
_Shanghai=data.Shanghai
_Shanghai.drop(üst7[0],inplace=True)
_Shanghai.drop(alt7[0],inplace=True)

temizveri=pd.DataFrame({"Bist100":_bist100,
"Bovespa":_Bovespa, "italy40":_italy40,"KOSPI":_KOSPI, "Nikkei":_Nikkei,
                        "BMVIIPC":_BMVIIPC,"Shanghai":_Shanghai})
    
temizveri.dropna(inplace=True)
temizveri




