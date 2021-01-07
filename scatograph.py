import pandas as pd 
import plotly.express as px

dataFrame2 = pd.read_csv("data.csv")
scattergraph = px.scatter(dataFrame2, x = "Population", y = "Per capita", color = "Country", title = "Internet Users", size = "Percentage", size_max = 60)
scattergraph.show()