# import csv 

# with open("weather_data.csv") as file:
#     data= csv.reader(file)
#     temperatures=[]
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

import pandas

data= pandas.read_csv("weather_data.csv")

# temp= data[1].to_list()
# print(temp)

print(type(data)) #DATA FRAME
print(type(data["temp"])) # SERIES

print(data["temp"].to_list())