import numpy as np
import pandas as pd

raw = pd.read_csv("Group2-311DataPreCOVID-Cold Season.csv")

cols2Drop = ["ADDRESS", "Sum SOURCE ", "Sum DAYTOCLOSE",
             "CREATTIME", "CREATEMO", "CREATEYR", "CLOSEMO", "ADDGEOC", "CASEURL"]


s1 = raw.drop(cols2Drop, axis=1)
