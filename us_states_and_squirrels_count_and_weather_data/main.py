# # with open("weather_data.csv") as weather_data:
# #     data=weather_data.readlines()
# #     print(data)

# # import csv
# # with open("weather_data.csv") as data_file:
# #     data=csv.reader(data_file)
# #     temperatures=[]
# #     for row in data:
# #         if row[1]!="temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# import pandas
# data=pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])

# # conversion of dataframe
# data_dict=data.to_dict()
# print(data_dict)

# # conversion of series
# data_list=data["temp"].to_list()
# print(data_list)
# length=len(data_list)
# # sum=0
# # for i in data_list:
# #     sum+=i
# # average=(round(sum/length,2))
# # print(average)
# # print(sum(data_list)/length)
# average=data["temp"].mean()
# print(average)

# maximum=data["temp"].max()
# print(data[data["temp"]==data["temp"].max()])
# print(maximum)

# # get data in row
# print(data[data["days"]=="tuesday"])

# monday=data[data.days=="monday"]
# print(monday.temp)
# fah=monday.temp*(9/5)+32
# print(fah)

import pandas 
data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrel_count=len(data[data["Primary Fur Color"]=="Gray"])
red_squirrel_count=len(data[data["Primary Fur Color"]=="Cinnamon"])
black_squirrel_count=len(data[data["Primary Fur Color"]=="Black"])

data_dict={
"Fur Color":["Gray","Cinnamon","Black"],
"Count":[gray_squirrel_count,red_squirrel_count,black_squirrel_count]
}

df=pandas.DataFrame(data_dict)
df.to_csv("squirell_Count.csv")



