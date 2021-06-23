import random as rand
import statistics as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

data = pd.read_csv("data.csv")
data_list = data["data"].tolist()

mean = st.mean(data_list)
median = st.median(data_list)
mode = st.mode(data_list)
stdev = st.stdev(data_list)

stdev1Start, stdev1End = mean - stdev, mean + stdev
stdev2Start, stdev2End = mean - (2*stdev), mean + (2*stdev)
stdev3Start, stdev3End = mean - (3*stdev), mean + (3* stdev)

fig = ff.create_distplot([data["data"]], ["Result"], show_hist=False)
fig.add_trace(go.Scatter(x = [stdev1Start, stdev1Start], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1 START"))
fig.add_trace(go.Scatter(x = [stdev1End, stdev1End], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 1 END"))
fig.add_trace(go.Scatter(x = [stdev2Start, stdev2Start], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2 START"))
fig.add_trace(go.Scatter(x = [stdev2End, stdev2End], y = [0,0.17], mode = "lines", name = "STANDARD DEVIATION 2 END"))
fig.show()


list_data_stdev1 = [result for result in data_list if result > stdev1Start and result < stdev1End]
list_data_stdev2 = [result for result in data_list if result > stdev2Start and result < stdev2End]
list_data_stdev3 = [result for result in data_list if result > stdev3Start and result < stdev3End]

print("{} % of data lies between 1 STANDARD DEVIATION".format(len(list_data_stdev1)*100/len(data_list)))
print("{} % of data lies between 2 STANDARD DEVIATION".format(len(list_data_stdev2)*100/len(data_list)))
print("{} % of data lies between 3 STANDARD DEVIATION".format(len(list_data_stdev3)*100/len(data_list)))


