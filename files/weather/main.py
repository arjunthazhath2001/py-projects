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

avg_temp=data["temp"].max()
max_temp=data["temp"].max()


print(avg_temp)
    
    
print(data.condition)

print(data[data.temp==max_temp])


monday= data[data.day=="Monday"]

print((monday["temp"]*1.8) +32)