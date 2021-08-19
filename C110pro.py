import random
import plotly.figure_factory as ff
import pandas
import statistics

file1 = pandas.read_csv('medium_data.csv')
rTime = file1['reading_time'].tolist()



mean = statistics.mean(rTime)
print(mean)
median = statistics.median(rTime)
print(median)
mode = statistics.mode(rTime)
print(mode)
std =statistics.stdev(rTime)
print(std)

def range_mean():
    dataset=[]
    for i in range(1,100):
        random_index = random.randint(0,len(rTime)-1)
        value= rTime[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_mean = range_mean()
        mean_list.append(set_of_mean)
    mean = statistics.mean(mean_list)
    print(mean)
    fig1 = ff.create_distplot([mean_list],['Mean List'],show_hist=False)
    fig1.show()


setup()