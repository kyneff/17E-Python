## 1
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022)

## 2
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["grand_total"] > 1000000])

## 3a
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022.sort_values("grand_total", ascending=False))

## 3b
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022.sort_values("grand_total", ascending=True))

## 5a
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022.nlargest(10, "grand_total"))

## 5b
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022.nsmallest(10, "grand_total"))

## 6a
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["brand"]=="Subaru"])

## 6b
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["brand"] == "Subaru"][["grand_total", "brand"]])

## 7a
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["brand"].str.startswith("L", na=False)])

## If you want to use .lower() this is how you would do it
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["brand"].str.lower().str.startswith("l", na=False)])

## 7b
# import pandas as pd

# sales2022 = pd.read_csv("06b_pandas_sales_data_2022.csv")
# print(sales2022[sales2022["brand"].str.lower().str.startswith("i", na=False)])