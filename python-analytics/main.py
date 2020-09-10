#import extract
import load
import transform
import plot

def main():
	print("ran extract")
	data = load.getFromFile()
	print("ran load")
	#print(data)
	df = transform.createDataFrame(data)
	#print(df.to_string())
	#for col in df.columns:
	#	print(col)
	#print(df.size)
	#print(df.shape)
	df1 = transform.getDateTime(df, "date")
	#for col in df1.columns:
	#	print(col)
	df2 = transform.getUniquePageviewsByWeek(df1, "datetime")
	#df3 = transform.getProjection(df2, ["date", "uniquePageviews"])
	print(type(df2))
	print(df2.tail(1))
	#plot.createFunnel(stages_arr, numbers_arr)

if __name__ == "__main__":
	
	main()
