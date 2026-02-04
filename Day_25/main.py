# # with open('weather_data.csv') as file:
# #     data = file.readlines()
# #     print(data)
#
# # import csv
# # with open('weather_data.csv') as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != 'temp':
# #             temperatures.append(int(row[1]))
# #         # print(row)
# #     print(temperatures)

import pandas

# data = pandas.read_csv('weather_data.csv')
# # print(type(data))
# # print(type(data['temp']))
# #
# # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data['temp'].to_list()
# # # print(len(temp_list))
# # # print(data['temp'].mean())
# #
# # # print(data['temp'].nlargest(1))
# # print(data['temp'].max())
# # print(data.temp.max())
#
# # print(data[data['day'] == 'Monday'])
# # print(data[data.day == 'Monday'])
#
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == 'Monday']
# #
# # result = (monday.temp[0] * (9/5)) + 32
# # print(result)
#
# # create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")



data = pandas.read_csv('Squirrel_Data.csv')

data_dict = {
    'Fur Color' : [],
    'Count' : []
}

colors_lst = data["Primary Fur Color"].drop_duplicates().to_list()
colors_lst.pop(0)
data_dict['Fur Color'] = colors_lst
# print(data_dict)

count_list = []
for color in data_dict['Fur Color']:
    # print(color)
    count_color = data[data["Primary Fur Color"] == color]
    count_list.append(len(count_color))
# print(count_list)
data_dict['Count'] = count_list

print(data_dict)
data = pandas.DataFrame(data_dict)
data.to_csv("squirell_count.csv")


