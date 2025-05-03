import pandas


data= pandas.read_csv("sq_data.csv")


# colors= data["Primary Fur Color"].value_counts()

# data=pandas.DataFrame(colors)


# print(data)
data.to_csv("sq_fur_data.csv")
