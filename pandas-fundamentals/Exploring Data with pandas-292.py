## 2. Using iloc to select by integer position ##

import pandas as pd
import numpy as np

f500 = pd.read_csv("f500.csv", index_col=0)
f500.index.name = None
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

fifth_row = f500.iloc[4]
first_three_rows = f500.iloc[:3]
first_seventh_row_slice = f500.iloc[[0,6],:5]

## 3. Reading CSV files with pandas ##

f500 = pd.read_csv("f500.csv")
f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

## 4. Working with Integer Labels ##

sorted_emp = f500.sort_values("employees", ascending=False)

top5_emp = sorted_emp.iloc[:5]

## 5. Using pandas methods to create boolean masks ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["rank"] - previously_ranked["previous_rank"]

## 6. Boolean Operators ##

# Example code:
# answer_0 = 1
answer_1 = 3
answer_2 = 2
answer_3 = 3

## 7. Using Boolean Operators ##

filter_big_rev_neg_profit = (f500["revenues"] > 100000) & (f500["profits"] < 0)
big_rev_neg_profit = f500[filter_big_rev_neg_profit]

filter_tech_outside_usa = (f500["sector"] == "Technology") & ~(f500["country"] == "USA")
tech_outside_usa = f500[filter_tech_outside_usa].head()

## 8. Pandas Index Alignment ##

previously_ranked = f500[f500["previous_rank"].notnull()]
rank_change = previously_ranked["previous_rank"] - previously_ranked["rank"]

f500["rank_change"] = rank_change

## 9. Using Loops with pandas ##

top_employer_by_country = {}

countries = f500["country"].unique()
for c in countries:
    selected_rows = f500[f500["country"] == c]
    sorted_rows = selected_rows.sort_values("employees", ascending=False)
    top_employer = sorted_rows.iloc[0]
    employer_name = top_employer["company"]
    top_employer_by_country[c] = employer_name

## 10. Challenge: Calculating Return on Assets by Country ##

f500["roa"] = f500["profits"] / f500["assets"]

top_roa_by_sector = {}
for sector in f500["sector"].unique():
    is_sector = f500["sector"] == sector
    sector_companies = f500.loc[is_sector]
    top_company = sector_companies.sort_values("roa",ascending=False).iloc[0]
    company_name = top_company["company"]
    top_roa_by_sector[sector] = company_name