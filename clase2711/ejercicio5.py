import pandas as pd
import datetime


dataframe=pd.read_csv('marketing_campaign.csv',sep=',')

dataframe.sort_values(["Year_Birth","ID"])
print(dataframe)

def mayoredad(year):
    if datetime.now()-year>=18:
        return True
    else:
        return False


dataframe["mayor_Edad"]=dataframe.Year_Birth.apply(mayoredad)