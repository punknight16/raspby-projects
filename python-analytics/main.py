from time import sleep
import extract
import inquirer
import load
import transform
import plot

def main():
	print("running extract function...")
	sleep(1)
	print("extract complete")
	year = inquirer.getYear()
	week = inquirer.getWeek()
	print("year:", year, "week:", week)
	print("running load function...")
	data = load.getFromFile()
	print("load complete")
	print("running transform functions...")
	print("creating dataframe...")
	df = transform.createDataFrame(data)
	print("adding a datetime column...")
	df1 = transform.addDateTime(df, "date")
	print("filter datetime by week year")
	df2 = transform.filterByWeekAndYear(df1, "datetime", year, week)
	print("adding a non-bounced session column")
	df3 = transform.addNonBouncedSessions(df2, "sessions", "bounceRate")
	print("getting projection of only useful columns")
	df4 = transform.getProjection(df3, ["datetime", "uniquePageviews", "nonbouncedSessions", "uniqueEvents"])
	print("sum [columns] groupby week")
	df5 = transform.getSumGroupByWeek(df4, "datetime")
	#transform.displayDataFrame(df5)
	print("list [values of columns]")
	list_of_values = transform.getListOfValues(df5, ["uniquePageviews", "nonbouncedSessions", "uniqueEvents"])
	print("creating funnel plot")
	fig = plot.createFunnel(["uniquePageviews", "nonbouncedSessions", "uniqueEvents"], list_of_values)
	print("exporting funnel plot to file")
	plot.exportFunnel(fig, year, week, "report.html")

if __name__ == "__main__":
	
	main()
