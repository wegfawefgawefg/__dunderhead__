import pandas

df = pandas.read_csv("./test.csv")
for x in range(100):
    df = pandas.read_csv("./new.csv")
    with open(f"new.csv", "w") as outfile:
        df.to_csv(outfile)
