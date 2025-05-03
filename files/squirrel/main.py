import pandas


data= pandas.read_csv("sq_data.csv")




gray=len(data[data["Primary Fur Color"]=="Gray"])
cina=len(data[data["Primary Fur Color"]=="Cinnamon"])
black=len(data[data["Primary Fur Color"]=="Black"])



data_dict={
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count": [gray,cina,black]
}


newdata= pandas.DataFrame(data_dict)
newdata.to_csv('trial.csv')


# colors= data["Primary Fur Color"].value_counts()
# data=pandas.DataFrame(colors)


# print(data)
# data.to_csv("sq_fur_data.csv")
