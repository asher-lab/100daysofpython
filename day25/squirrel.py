#  #import csv
#
#  #with open("weather_data.csv") as weather_data:
#  #    data = csv.reader(weather_data)
#  #    temperature = []
#  #    for row in data:
#  #        #print(row)
#  #        if row[1] != 'temp':
#  #            temperature.append(float(row[1]))
#  #print(temperature)
#
#  import pandas
#  from statistics import mean
#  from numpy import mean as mean1
#
#
#  data = pandas.read_csv("weather_data.csv")
#  #print(data)
#  #print("\n\n")
#  #print(data["temp"])
#  #print(type(data))
#  #print(type(data["temp"])) #columns is called series in pandas
#
#  data_dict = data.to_dict()
#  #print(data_dict)
#
#  data_list = data["temp"].to_list()
#  #print(data_list)
#  #print(len(data_list))
#
#  avg_temp = mean(data_list)
#  avg_temp1 = mean1(data_list)
#  #print(f"Average temp is {avg_temp}")
#  #print(f"Average temp is {avg_temp1}")
#  #print("Maximum value in list:", data["temp"].max())
#  #print(data.condition)
#
#  #get data in rows
#  print(data[data.temp == data.temp.max()])
#
#  monday = data[data.day == "Monday" ]
#  print(monday.condition)
#  import pytemperature as pytemp
#  print("Temperature in celsisus", pytemp.c2f(monday.temp))
#
#  #Create dictionary from scratch
#  data_dict = {
#      "student": ["Amy", "James", "Angela"],
#      "scores": [99, 98, 90]
#  }
#
#  data = pandas.DataFrame(data_dict)
#  print(data)
#  data.to_csv("new_data.csv")

import pandas
# Creating a new data dictionary from squirrel
data = pandas.read_csv("squirreldat.csv")
grey_squirrel = data[data["Primary Fur Color"] == "Gray"]
print(grey_squirrel)
color = data["Primary Fur Color"].value_counts()



squirrel_count = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [color[0],color[1],color[2]]
}
dataDF = pandas.DataFrame(squirrel_count)
print(data)

#Putting it into a file
dataDF.to_csv("squirrel_count.csv")

