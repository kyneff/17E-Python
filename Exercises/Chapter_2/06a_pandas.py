## 1
# f = open("06a_pandas_fake_smoker_data.csv")
# print(f.readlines())
# f.close()

## 2
# import pandas as pd
# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")

## 3
# import pandas as pd
# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData)

## 4
# import pandas as pd
# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData["age_started_smoking"] < 20)

## 5
# If we want to see the rest of the data for those rows, we do this.
# print(fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20])

## 6
# We can see how many people started smoking before 20:
# below20 = fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20]
# print(len(below20))

## 7
# Print the rows of people who are currently older than 50.

## 8
# Try this:
# print(fakeSmokerData.sort_values("current_age"))

## 9
# Try this:
# print(fakeSmokerData.sort_values("age_started_smoking"))

## Appendix
## For those who are interested:
## This is the code that I used to generate the fake smoker data.
# import random
# for unused in range(20):
#     st = random.randrange(18, 23)
#     curr = random.randrange(20, 65)
#     g = random.choice("FM")
#     print(f"{st},{curr},{g}")