import pandas
from pathlib import Path

folder_path = Path(__file__).parent

data = pandas.read_csv(f'{folder_path}/Squirrel_Data.csv')

data_dict = {}

colors_lst = data["Primary Fur Color"].drop_duplicates().to_list()
colors_lst.pop(0)
data_dict['Fur Color'] = colors_lst

count_list = []
for color in data_dict['Fur Color']:
    # print(color)
    count_color = data[data["Primary Fur Color"] == color]
    
    count_list.append(len(count_color))
# print(count_list)
data_dict['Count'] = count_list

print(data_dict)
data = pandas.DataFrame(data_dict)
data.to_csv(f"{folder_path}/squirell_count.csv")

