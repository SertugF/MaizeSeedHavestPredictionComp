import pandas as pd
import os
from sklearn.preprocessing import LabelEncoder

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


def dropColumnsForTestingMetaData():
    # read the csv file
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "2_Testing_Meta_Data_2022.csv"),
        encoding="latin-1",
    )

    # selected columns to stay env, year, Treatment, previous crop, type of planter, System_Determining_Moisture, Pounds_Needed_Soil_Moisture, Irrigated,  Plot_Area_ha
    # drop rest of the columns
    columns = [
        "Env",
        "Year",
        "Treatment",
        "Previous_Crop",
        "Type_of_planter (fluted cone; belt cone; air planter)",
        "System_Determining_Moisture",
        "Pounds_Needed_Soil_Moisture",
        "Irrigated",
        "Plot_Area_ha",
    ]
    df1 = pd.DataFrame(df, columns=columns)
    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data", "Testing_Data", "2_Testing_Meta_Data_Selected_ColumnsV1.csv"
        ),
        index=False,
    )


def dropColumnsForTestingSoilData():
    # selected columns
    # env, year, 1:1 Soil pH, 1:1 S Salts mmho/cm, Organic Matter LOI %, Potassium ppm K, Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat, %Sand, %Silt, %clay
    # read the csv file
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "3_Testing_Soil_Data_2022.csv"),
        encoding="latin-1",
    )
    # drop rest of the columns
    columns = [
        "Env",
        "Year",
        "1:1 Soil pH",
        "1:1 S Salts mmho/cm",
        "Organic Matter LOI %",
        "Potassium ppm K",
        "Nitrate-N ppm N",
        "Mehlich P-III ppm P",
        "%Ca Sat",
        "%Mg Sat",
        "% Sand",
        "% Silt",
        "% Clay",
    ]
    df1 = pd.DataFrame(df, columns=columns)
    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data", "Testing_Data", "3_Testing_Soil_Data_Selected_ColumnsV1.csv"
        ),
        index=False,
    )


def dropColumnsForWeatherData():
    # selected columns env, date, ALLSKY_SFC_PAR_TOT, RH2M, T2M_MAX, GWETPROF, GWETTOP, T2M_MIN, GWETROOT,
    # read the csv file
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "4_Testing_Weather_Data_2022.csv"),
        encoding="latin-1",
    )
    # drop rest of the columns
    columns = [
        "Env",
        "Date",
        "ALLSKY_SFC_PAR_TOT",
        "RH2M",
        "T2M_MAX",
        "GWETPROF",
        "GWETTOP",
        "T2M_MIN",
        "GWETROOT",
    ]

    df1 = pd.DataFrame(df, columns=columns)
    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data", "Testing_Data", "4_Testing_Weather_Data_SelectedColumnsV1"
        ),
        index=False,
    )


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


def labelEncodeData(givenCsvFile, newCsvFile, givenColumn):
    # read the csv file
    df = pd.read_csv(givenCsvFile, encoding="latin-1")
    # label encode the data
    label_encoder = LabelEncoder()
    df[givenColumn] = label_encoder.fit_transform(df[givenColumn])
    # write the csv file
    df.to_csv(newCsvFile, index=False)


def labelEncodeDataForAllObjects(givenCsvFile, newCsvFile):
    # read the csv file
    df = pd.read_csv(givenCsvFile, encoding="latin-1")
    # label encode the data
    label_encoder = LabelEncoder()
    for column in df.columns:
        if df[column].dtype == object:
            df[column] = label_encoder.fit_transform(df[column])
    # write the csv file
    df.to_csv(newCsvFile, index=False)


def createMergedTestSubTemp_MetaData():

    # read csv 1 check info if it has na's fill them
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "1_Submission_Template_2022.csv")
    )
    df.info()

    # read csv 2 check info if it has na's fill them
    df2 = pd.read_csv(
        os.path.join(
            "Data", "Testing_Data", "2_Testing_Meta_Data_Selected_ColumnsV1.csv"
        )
    )
    df2.info()

    # fill empty objects with both ways
    df2.fillna(method="ffill", inplace=True)
    df2.fillna(method="bfill", inplace=True)

    df2.info()

    df2.to_csv(
        os.path.join(
            "Data", "Testing_Data", "2_Testing_Meta_Data_Selected_ColumnsV1_Filled.csv"
        ),
        index=False,
    )

    mergeTwoCsvFiles(
        os.path.join("Data", "Testing_Data", "1_Submission_Template_2022.csv"),
        os.path.join(
            "Data", "Testing_Data", "2_Testing_Meta_Data_Selected_ColumnsV1_Filled.csv"
        ),
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_MetaData.csv"),
        "Env",
    )

    df3 = pd.read_csv(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_MetaData.csv")
    )

    df3.info()


def createMergedTestSubTemp_SoilData():

    # read csv 1 check info if it has na's fill them
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_MetaData.csv")
    )
    df.info()

    # read csv 2 check info if it has na's fill them
    df2 = pd.read_csv(
        os.path.join(
            "Data", "Testing_Data", "3_Testing_Soil_Data_Selected_ColumnsV1.csv"
        )
    )
    df2.info()

    # fill empty objects with both ways
    df2.fillna(method="ffill", inplace=True)
    df2.fillna(method="bfill", inplace=True)

    df2.info()

    df2.to_csv(
        os.path.join(
            "Data", "Testing_Data", "3_Testing_Soil_Data_Selected_ColumnsV1_Filled.csv"
        ),
        index=False,
    )

    mergeTwoCsvFiles(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_MetaData.csv"),
        os.path.join(
            "Data", "Testing_Data", "3_Testing_Soil_Data_Selected_ColumnsV1_Filled.csv"
        ),
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_Metadata_SoilData.csv"),
        "Env",
    )

    df3 = pd.read_csv(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_Metadata_SoilData.csv")
    )

    df3.info()


def createMergeTestSubTemp_WeatherData():

    # read csv 1 check info if it has na's fill them
    df = pd.read_csv(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_Metadata_SoilData.csv")
    )
    df.info()

    # read csv 2 check info if it has na's fill them
    df2 = pd.read_csv(
        os.path.join(
            "Data", "Testing_Data", "4_Testing_Weather_Data_SelectedColumnsV1.csv"
        )
    )
    df2.info()

    # fill empty objects with both ways
    df2.fillna(method="ffill", inplace=True)
    df2.fillna(method="bfill", inplace=True)

    df2.info()

    df2.to_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "4_Testing_Weather_Data_Selected_ColumnsV1_Filled.csv",
        ),
        index=False,
    )

    mergeTwoCsvFiles(
        os.path.join("Data", "Testing_Data", "mergedTestSubTemp_Metadata_SoilData.csv"),
        os.path.join(
            "Data",
            "Testing_Data",
            "4_Testing_Weather_Data_Selected_ColumnsV1_Filled.csv",
        ),
        os.path.join(
            "Data",
            "Testing_Data",
            "mergedTestSubTemp_Metadata_SoilData_WeatherData.csv",
        ),
        "Env",
    )

    df3 = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "mergedTestSubTemp_Metadata_SoilData_WeatherData.csv",
        )
    )

    df3.info()


# all needed data columns for Training
# Env,Hybrid,Yield_Mg_ha,Year_x,Treatment,Previous_Crop,Type_of_planter (fluted cone; belt cone; air planter),System_Determining_Moisture,Pounds_Needed_Soil_Moisture,Irrigated,Plot_Area_ha,Year_y,1:1 Soil pH,1:1 S Salts mmho/cm,Organic Matter LOI %,Potassium ppm K,Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat,% Sand,% Silt,% Clay,Date,ALLSKY_SFC_PAR_TOT,RH2M,T2M_MAX,GWETPROF,GWETTOP,T2M_MIN,GWETROOT


def createMonthlyWeatherData():  # cancelled for env needs to be index.
    # read csv
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "4_Testing_Weather_Data_Selected_ColumnsV1_Filled_Temp.csv",
        )
    )
    df.info()

    print(df.head())
    print(df.tail())

    # convert date to datetime
    df.Date = pd.to_datetime(df.Date)
    df1 = df.resample("M", on="Date").mean()

    print(df1.head())
    print(df1.tail())

    df1.info()

    print("end?")


def dropColumnsForTrainingTraitData():
    # read csv
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield.csv",
        )
    )

    columns = [
        "Env",
        "Hybrid",
        "Year",
        "Yield_Mg_ha",
    ]
    df1 = pd.DataFrame(df, columns=columns)
    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield_Selected_Columns.csv",
        ),
        index=False,
    )

def dropColumnsForTrainingMetaData():
    # this is where we left ##############################################################

def checkAndFillNaData(csvFileIn, csvFileOut):

    # read csv 2 check info if it has na's fill them
    df2 = pd.read_csv(csvFileIn)
    df2.info()

    isAnyValNan = df2.isnull().values.any()
    # fill empty objects with both ways
    print(isAnyValNan)

    if isAnyValNan:
        df2.fillna(method="ffill", inplace=True)
        df2.fillna(method="bfill", inplace=True)
        print("NA values found in the data and filled")
    else:
        print("No NA values found in the data")

    df2.info()

    df2.to_csv(
        csvFileOut,
        index=False,
    )


def main():

    # drop testing meta data columns

    # dropColumnsForTestingMetaData()
    # dropColumnsForTestingSoilData()
    # dropColumnsForWeatherData()

    # merge meta and template
    # createMergedTestSubTemp_SoilData()
    # createMergeTestSubTemp_WeatherData()

    # createMonthlyWeatherData()

    # drop columns for training trait data
    # dropColumnsForTrainingTraitData()



    # checkAndFillNaData(
    #     os.path.join(
    #         "Data",
    #         "Training_Data",
    #         "1_Training_Trait_Data_2014_2021_NoMissingYield_Selected_Columns.csv",
    #     ),
    #     os.path.join(
    #         "Data",
    #         "Training_Data",
    #         "1_Training_Trait_Data_2014_2021_NoMissingYield_Selected_Columns_Filled.csv",
    #     ),
    # )

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

# label encoder

"""# check type
    print(df.dtypes)

    # make Env variable numeric (can only be used on object type)
    label_encoder = LabelEncoder()
    df["Env"] = label_encoder.fit_transform(df["Env"])
    print(df.dtypes)

    # save to csv
    df.to_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield_EnvNumeric.csv",
        ),
        index=False,
    )"""

# test numeralize data
""" labelEncodeDataForAllObjects(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield.csv",
        ),
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYieldNumarized.csv",
        ),
    )
"""
# # interpolate missing values
# df1.interpolate(method="linear", inplace=True)
