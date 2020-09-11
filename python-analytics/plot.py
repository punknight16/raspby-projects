import plotly.express as px

def createFunnel(stage, number):
	data = dict(
		number=number,
		stage=stage)
	fig = px.funnel(data, x='number', y='stage')
	#fig.show()
	return fig
    
def exportFunnel(fig, year, week, filename):
	fullname = str(year)+"-"+str(week)+"_"+filename
	fig.write_html(fullname)
	return
