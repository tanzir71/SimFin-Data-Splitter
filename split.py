import pandas as pd

csv_path = "C:\\Users\\ThirdHandBD\\Desktop\\Data Splitting\\pd-split\\chunk4.csv"

#df = pd.read_csv(csv_path, header=1, dtype='unicode', sep=';', low_memory=False, error_bad_lines=False)
df = pd.read_csv(csv_path, header = 1, dtype='unicode', sep=';')
print("I read in a dataframe with {} columns and {} rows.".format(
len(df.columns), len(df)
))

filename = 1

#column increment
x = 30 * 59

for column in df:
    loc = df.columns.get_loc(column)
    if loc == (x * filename) + 1:
        y = filename - 1
        a = (x * y) + 1
        b = (x * filename) + 1
        date_df = df.iloc[:, :1]
        out_df = df.iloc[:, a:b]
        final_df = pd.concat([date_df, out_df], axis=1, join='inner')
        out_path = "C:\\Users\\ThirdHandBD\\Desktop\\Data Splitting\\pd-split\\chunk4-part" + str(filename) + ".csv"
        final_df.to_csv(out_path)
        #out_df.to_csv(out_path)
        filename += 1


# This should be the same as df, but with only the first column.
# Check it with similar code to above.