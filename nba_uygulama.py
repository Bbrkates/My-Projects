import pandas as pd
import numpy as np


dframe = pd.read_csv("nba.csv")

result = dframe
result = dframe.columns
result = dframe.info
result = dframe.head()
result = dframe.head(10)
result = dframe.tail()
result = dframe.tail(20)
result = dframe["Player"]
result = dframe["Player"].head(20)
result = dframe["Player"].tail(15)
result = dframe[["Player","Team","Number","Position","Height","Weight","Last Attended","Country"]]
result = dframe[["Player","Team","Number","Position","Height","Weight","Last Attended","Country"]].head()
result = dframe[["Player","Team","Number","Position","Height","Weight","Last Attended","Country"]].head(20)
result = dframe[["Player","Team","Number","Position","Height","Weight","Last Attended","Country"]].tail()
result = dframe[["Player","Team","Number","Position","Height","Weight","Last Attended","Country"]].tail(25)
result = dframe[dframe["Team"] == "PHX"].head()
result = dframe[dframe["Team"] == "PHX"].tail()
result = dframe[dframe["Position"]== "C"]
result = dframe[dframe["Position"]== "C"].head()
result = dframe[dframe["Position"]== "C"].tail()
result = dframe[dframe["Number"] == "5"].head()
result = dframe[dframe["Number"] >= "3"].tail()
result = dframe[dframe["Number"] <= "10"].tail(15)
result = dframe[dframe["Height"] >= "6-7"].head()
result = dframe[dframe["Height"] <= "6-10"].head(15)
result = dframe[dframe["Height"] >= "6-9"].tail()
result = dframe[dframe["Height"] <= "6-12"].tail(25)
result = dframe[dframe["Weight"] >= "190"].head()
result = dframe[dframe["Weight"] >= "210"].head(10)
result = dframe[dframe["Weight"] <= "260"].tail()
result = dframe[dframe["Weight"] <= "240"].tail(14)
result = dframe[dframe["Last Attended"] == "Miami"].head()
result = dframe[dframe["Last Attended"] == "Alabama"].head(10)
result = dframe[dframe["Last Attended"] == "UCLA"].tail(10)
result = dframe[dframe["Country"] == "USA"].head()
result = dframe[dframe["Country"] == "USA"].head(10)
result = dframe[dframe["Country"] == "USA"].tail()
result = dframe[dframe["Country"] == "USA"].tail(20)




print(result)










































