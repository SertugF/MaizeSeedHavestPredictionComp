import pandas as pd
import os

# main declaration


def mergeTwoCsvFiles(data1, data2, merged, id):
    # read the csv files
    df1 = pd.read_csv(data1, encoding="latin-1")
    df2 = pd.read_csv(data2, encoding="latin-1")
    # merge the csv files
    df = pd.merge(df1, df2, on=id)
    # write the merged csv file
    df.to_csv(merged, index=False)


def dropColumnAndWriteCsvFile(givenColumn, givenCsvFile, newCsvFile):
    # read the csv file
    df = pd.read_csv(givenCsvFile, encoding="latin-1")
    # drop the column
    df.drop(givenColumn, axis=1, inplace=True)
    # write the csv file
    df.to_csv(newCsvFile, index=False)


# check pearson correlation for a given csv file
def checkPearsonCorrelation(givenCsvFile, newCsvFile):
    # read the csv file
    df = pd.read_csv(givenCsvFile, encoding="latin-1")
    # check the pearson correlation
    # print(df.corr(method="pearson"))

    # save corelation results to csv file
    df.corr(method="pearson").to_csv(newCsvFile, index=False)


def numeralizeData(givenCsvFile, newCsvFile):
    # read the csv file
    df = pd.read_csv(givenCsvFile, encoding="latin-1")
    # numeralize the data
    df = pd.get_dummies(df)
    # write the csv file
    df.to_csv(newCsvFile, index=False)


def hybridToNumeric(x):
    if x == "1319YHR":
        return 1
    if x == "b":
        return 2


def main():

    import pandas as pd

    checkPearsonCorrelation(
        os.path.join(
            "Data",
            "Training_Data",
            "6_Training_EC_Data_2014_2021.csv",
        ),
        os.path.join(
            "Data", "Training_Data", "1_Training_Trait_Data_2014_2021_Pearson.csv"
        ),
    )

    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield.csv",
        ),
        encoding="latin-1",
    )

    print(df.head())

    # create dummies
    # df = pd.get_dummies(df, columns=["Hybrid"], prefix = ["Dummy_Hybrid"], drop_first=True)

    print("Done")


if __name__ == "__main__":
    main()


# old code that worked
# test drop column. Works turns out csv files are on latin 1 encoding...
""" dropColumnAndWriteCsvFile(
    "Experiment_Code",
    os.path.join("Data", "Training_Data", "2_Training_Meta_Data_2014_2021.csv"),
    os.path.join(
        "Data", "Training_Data", "2_Training_Meta_Data_2014_2021_NoExpCode.csv"
    ),
) """

# if row for Yield_Mg_ha missing drop row for trait data and save to new csv file
"""     df = pd.read_csv(
        os.path.join("Data", "Training_Data", "1_Training_Trait_Data_2014_2021.csv"),
        encoding="latin-1",
    )
    df = df.dropna(axis=0, subset=["Yield_Mg_ha"])
    df.to_csv(
        os.path.join(
            "Data", "Training_Data", "1_Training_Trait_Data_2014_2021_NoMissing.csv"
        ),
        index=False,
    ) """

# test check pearson correlation

""" 
    checkPearsonCorrelation(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield.csv",
        ),
        os.path.join(
            "Data", "Training_Data", "1_Training_Trait_Data_2014_2021_Pearson.csv"
        ),
    ) """
