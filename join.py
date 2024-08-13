import numpy as np
import pandas as pd 

main = pd.read_csv("./santa_rosa.csv", index_col=0)
streets = pd.read_csv("./santa_rosa_processed.csv", index_col=0)
output = pd.merge(main,streets, left_on = "Index", right_on = "Index")

output.to_csv("nice.csv")


