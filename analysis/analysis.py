import pandas as pd
import sys

N = 1000

df = pd.read_csv(sys.argv[1], sep = ', ', header = 0) #, nrows = N)

# Words in content
print("Words in Content")
print("Median", df.n_tokens_content.median())
print("Stddev", df.n_tokens_content.std())

print("Shares")
print("Median", df.shares.median())
print("Stddev", df.shares.std())