import plotly.express as px

def createFunnel():
	data = dict(
		number=[41, 12, 2],
		stage=["Unique Page Views", "Non-bounced Sessions", "Conversion Events"])
	fig = px.funnel(data, x='number', y='stage')
	fig.write_html("plot.html")
