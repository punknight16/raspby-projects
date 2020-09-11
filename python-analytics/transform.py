import pandas as pd

def displayDataFrame(df):
	print(type(df))
	print(df.to_string())
	for col in df.columns:
		print(col)
	print(df.size)
	print(df.shape)
	return

def createDataFrame(data):
	df = pd.DataFrame(data)	
	return df	

def getProjection(df, column_name_arr):
	df1 = df[column_name_arr]
	return df1

def addDateTime(df, column_name):
	df['datetime'] =  pd.to_datetime(df[column_name])
	return df

def filterByWeekAndYear(df, column_name, year, week):
	df1 = df[df[column_name].dt.year == year]
	df2 = df1[df1[column_name].dt.isocalendar().week == week]
	return df2

def addNonBouncedSessions(df, sess_col1, bounce_col2):
	df["nonbouncedSessions"] = df[sess_col1] * (1-.01 * df[bounce_col2])
	return df

def getSumGroupByWeek(df, column_name):
	return df.groupby(df[column_name].dt.strftime('%W'))[["uniquePageviews", "nonbouncedSessions", "uniqueEvents"]].apply(sum)

def getListOfValues(df, column_names):
	list_of_values = []
	for col in column_names:
		list_of_values.append(df[col].values[0])
	return list_of_values