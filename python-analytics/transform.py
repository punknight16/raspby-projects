import pandas as pd

def createDataFrame(data):
	df = pd.DataFrame(data)	
	return df	

def getProjection(df, column_name_arr):
	df1 = df[column_name_arr]
	return df1

def getDateTime(df, column_name):
	df['datetime'] =  pd.to_datetime(df[column_name])
	return df

def getUniquePageviewsByWeek(df, column_name):
	return df.groupby(df[column_name].dt.strftime('%W'))["uniquePageviews"].sum()
