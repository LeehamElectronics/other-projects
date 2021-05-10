import pandas as pd
import openpyxl

df = pd.DataFrame([[11, 21, 31], [12, 22, 32], [31, 32, 33]],
                  index=false, columns=['group', 'data'])

print(df)
#         a   b   c
# one    11  21  31
# two    12  22  32
# three  31  32  33