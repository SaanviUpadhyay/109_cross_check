import statistics
import csv
import random

import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd


df      = pd.read_csv("StudentsPerformance.xls")
data    = df["reading score"].tolist()

mean    = sum(data) / len(data)
std_dev = statistics.stdev(data)
median  = statistics.median(data)
mode    = statistics.mode(data)

first_std_dev_start , first_std_dev_end =(
    mean - std_dev,
    mean + std_dev
)

second_std_dev_start , second_std_dev_end = mean - (2*std_dev) , mean + (2*std_dev)
third_std_dev_start , third_std_dev_end   = mean - (3*std_dev) , mean + (3*std_dev)

fig = ff.create_distplot([data] , ["reading scores"] , show_hist=False)
fig.add_trace(go.Scatter(x = [mean , mean] , y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(
    go.Scatter(
        x    =    [first_std_dev_start , first_std_dev_end],
        y    =    [ 0 , 0.17],
        mode =    "lines",
        name =    "STD DEV 1"
    )
)
    
fig.add_trace(go.Scatter(
        x    =    [first_std_dev_start , first_std_dev_end],
        y    =    [ 0 , 0.17],
        mode =    "lines",
        name =    "STD DEV 1"
    )
)


fig.add_trace(go.Scatter(
        x    =    [second_std_dev_start , second_std_dev_end],
        y    =    [ 0 , 0.17],
        mode =    "lines",
        name =    "STD DEV 2"
    )
)

fig.add_trace(go.Scatter(
        x    =    [second_std_dev_start , second_std_dev_end],
        y    =    [ 0 , 0.17],
        mode =    "lines",
        name =    "STD DEV 2"
    )
)

fig.show()

list_of_data_within_1_std_dev = [
    result
    for result in data
    if result > first_std_dev_start and result < first_std_dev_end
]

list_of_data_within_2_std_dev = [
    result
    for result in data
    if result > second_std_dev_start and result < second_std_dev_end
]

list_of_data_within_3_std_dev = [
    result
    for result in data
    if result > third_std_dev_start and result < third_std_dev_end
]

print("Mean of the given data is {}".format(mean))
print("Median of the given data is {}".format(median))
print("Mode of the given data is {}".format(mode))
print("Standard deviation of the given data is {}".format(std_dev))
print(
    "{}% of data lies within the first standard deviation".format(
        len(list_of_data_within_1_std_dev)*100/len(data)
    )
)
print(
    "{}% of data lies within the first standard deviation".format(
        len(list_of_data_within_2_std_dev)*100/len(data)
    )
)
print(
    "{}% of data lies within the first standard deviation".format(
        len(list_of_data_within_3_std_dev)*100/len(data)
    )
)


