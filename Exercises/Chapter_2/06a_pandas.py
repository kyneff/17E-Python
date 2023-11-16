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
# import pandas as pd

# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20])

## 6
# import pandas as pd

# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# below20 = fakeSmokerData[fakeSmokerData["age_started_smoking"] < 20]
# print(len(below20))

# 7
# import pandas as pd

# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData[fakeSmokerData["current_age"] > 50])

## 8
# import pandas as pd

# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData.sort_values("current_age"))

## 9
# import pandas as pd

# fakeSmokerData = pd.read_csv("06a_pandas_fake_smoker_data.csv")
# print(fakeSmokerData.sort_values("age_started_smoking"))