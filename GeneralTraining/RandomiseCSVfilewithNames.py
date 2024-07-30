import pandas as pd
import random

csv_file_path = "GeneralTraining/random_names.csv"

df = pd.read_csv(csv_file_path)
# print(df.to_string())

# converting column data to list

names = df["Name"].tolist()

print(names)


def derange_list(list):
    while True:
        shuffled = list[:]
        random.shuffle(shuffled)
        # zip allows to iterate two lists at the same time
        if all(x != y for x, y in zip(list, shuffled)):
            return shuffled


shuffledList = derange_list(names)

print(shuffledList)

# create dataFrame
df = pd.DataFrame(shuffledList, columns=["Name"])

# Save to CSV
csv_file_path = "GeneralTraining/random_names_shuffled.csv"
df.to_csv(csv_file_path, index=False)
