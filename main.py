import pandas as pd

# main declaration


def mergeTwoCsvFiles(data1, data2, merged, id):
    # read the csv files
    df1 = pd.read_csv(data1)
    df2 = pd.read_csv(data2)
    # merge the csv files
    df = pd.merge(df1, df2, on=id)
    # write the merged csv file
    df.to_csv(merged, index=False)


def dropColumnAndWriteCsvFile(givenColumn, givenCsvFile, newCsvFile):
    # read the csv file
    df = pd.read_csv(givenCsvFile)
    # drop the column
    df.drop(givenColumn, axis=1, inplace=True)
    # write the csv file
    df.to_csv(newCsvFile, index=False)


def main():

    # use pandas to merge the two csv files
    import pandas as pd


if __name__ == "__main__":
    main()
