from difflib import Differ
import pandas as pd

def load_and_compare(basefile_loc, otherfile_loc):
    base_file = pd.read_excel(basefile_loc)
    otherfile = pd.read_excel(otherfile_loc)

    # Sort the DataFrames by 'has pipeline' and 'onboarded'
    df1_sorted = base_file.sort_values(by=['has pipeline', 'onboarded'])
    df2_sorted = otherfile.sort_values(by=['has pipeline', 'onboarded'])

    # Reset index to ensure proper alignment for comparison
    df1_sorted.reset_index(drop=True, inplace=True)
    df2_sorted.reset_index(drop=True, inplace=True)

    d = Differ()
    df1_str = df1_sorted.to_csv(index=False).splitlines()
    df2_str = df2_sorted.to_csv(index=False).splitlines()

    difference = d.compare(df1_str, df2_str)

    diff_rows = [line for line in difference if line.startswith('+ ') or line.startswith('- ')]
    delta_df = pd.DataFrame(diff_rows, columns=["Difference"])

    delta_df.to_csv('delta.csv', index=False)
    print("Delta between the two files has been written to 'delta.csv'.")

#load_and_compare("C:/Users/joaop/Downloads/reportbase.xlsx", "C:/Users/joaop/Downloads/reportmarch.xlsx")