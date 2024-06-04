# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
# Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
print(data)

data = pd.DataFrame({"columns": ["robot", "human"]})
un_values = data["columns"].unique()
one_hot_data = pd.DataFrame(0, index=data.index, columns=un_values)

for value in un_values:
    one_hot_data.loc[data["columns"] == value, value] = 1

print(one_hot_data)