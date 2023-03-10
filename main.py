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


# def numeralizeData(givenCsvFile, newCsvFile):  # depreceted
#     # read the csv file
#     df = pd.read_csv(givenCsvFile, encoding="latin-1")
#     # numeralize the data
#     df = pd.get_dummies(df)
#     # write the csv file
#     df.to_csv(newCsvFile, index=False)


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
        "Plot_Area_ha",  # added new, must have forget to add it
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
    # Env,Hybrid,Yield_Mg_ha,Year_x,Treatment,Previous_Crop,Type_of_planter (fluted cone; belt cone; air planter),System_Determining_Moisture,Pounds_Needed_Soil_Moisture,Irrigated,Plot_Area_ha,Year_y,1:1 Soil pH,1:1 S Salts mmho/cm,Organic Matter LOI %,Potassium ppm K,Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat,% Sand,% Silt,% Clay,Date,ALLSKY_SFC_PAR_TOT,RH2M,T2M_MAX,GWETPROF,GWETTOP,T2M_MIN,GWETROOT

    # irrigated bilgisi training metada yok , treatment i??ine g??m??lm????.
    # read csv
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "2_Training_Meta_Data_2014_2021.csv",
        ),
        encoding="latin-1",
    )

    columns = [
        "Env",
        "Year",
        "Treatment",
        "Previous_Crop",
        "Type_of_planter (fluted cone; belt cone; air planter)",
        "System_Determining_Moisture",
        "Pounds_Needed_Soil_Moisture",
    ]
    df1 = pd.DataFrame(df, columns=columns)
    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "2_Training_Meta_Data_2014_2021_Selected_Columns.csv",
        ),
        index=False,
    )


def dropColumnsForTrainingSoilData():
    # Env,Hybrid,Yield_Mg_ha,Year_x,Treatment,Previous_Crop,Type_of_planter (fluted cone; belt cone; air planter),System_Determining_Moisture,Pounds_Needed_Soil_Moisture,Irrigated,Plot_Area_ha,Year_y,1:1 Soil pH,1:1 S Salts mmho/cm,Organic Matter LOI %,Potassium ppm K,Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat,% Sand,% Silt,% Clay,Date,ALLSKY_SFC_PAR_TOT,RH2M,T2M_MAX,GWETPROF,GWETTOP,T2M_MIN,GWETROOT
    # read csv latin-1
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "3_Training_Soil_Data_2015_2021.csv",
        ),
        encoding="latin-1",
    )

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
            "Data",
            "Training_Data",
            "3_Training_Soil_Data_2015_2021_Selected_Columns.csv",
        ),
        index=False,
    )


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


def checkAndFillNaDataFrame(df):
    # read csv 2 check info if it has na's fill them
    df.info()

    isAnyValNan = df.isnull().values.any()
    # fill empty objects with both ways
    print(isAnyValNan)

    if isAnyValNan:
        df.fillna(method="ffill", inplace=True)
        df.fillna(method="bfill", inplace=True)
        print("NA values found in the data and filled")
    else:
        print("No NA values found in the data")

    df.info()

    return df


def dropColumnsForTrainingWeatherData():
    # this is wher we left off... we need to drop the columns that we dont need
    # Env,Hybrid,Yield_Mg_ha,Year_x,Treatment,Previous_Crop,Type_of_planter (fluted cone; belt cone; air planter),System_Determining_Moisture,Pounds_Needed_Soil_Moisture,Irrigated,Plot_Area_ha,Year_y,1:1 Soil pH,1:1 S Salts mmho/cm,Organic Matter LOI %,Potassium ppm K,Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat,% Sand,% Silt,% Clay,Date,ALLSKY_SFC_PAR_TOT,RH2M,T2M_MAX,GWETPROF,GWETTOP,T2M_MIN,GWETROOT

    # read csv latin-1
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "4_Training_Weather_Data_2014_2021.csv",
        ),
        encoding="latin-1",
    )

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
            "Data",
            "Training_Data",
            "4_Training_Weather_Data_2014_2021_Selected_Columns.csv",
        ),
        index=False,
    )


def mergeAllTrainingData():
    # read training trait data filled
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "1_Training_Trait_Data_2014_2021_NoMissingYield_Selected_Columns_Filled.csv",
        )
    )
    # read training meta data filled
    df1 = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "2_Training_Meta_Data_2014_2021_Selected_Columns_Filled.csv",
        )
    )

    # read training soil data filled

    df2 = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "3_Training_Soil_Data_2015_2021_Selected_Columns_Filled.csv",
        )
    )

    # read training weather data filled
    df3 = pd.read_csv(
        os.path.join(
            "Data",
            "Training_Data",
            "4_Training_Weather_Data_2014_2021_Selected_Columns_Filled.csv",
        )
    )
    # merge all data

    print(df.head())
    print("-----------------------------------------------")
    print(df1.head())

    df4 = pd.merge(df, df1, on=["Env"])
    df5 = pd.merge(df4, df2, on=["Env"])
    df6 = pd.merge(df5, df3, on=["Env"])

    # numeralize data
    df6 = numaricEncoder(df6)

    # check head of data
    print(df6.head())

    # write to csv neeeds to be around 5.4gb ()
    df6.to_csv(
        "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather_YieldLastNew_AreaPlot.csv",
        index=False,
    )


def mergeAllTestData():
    # read training trait data filled
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "1_Submission_Template_2022.csv",
        )
    )
    # read training meta data filled
    df1 = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "2_Testing_Meta_Data_2014_2021_Selected_Columns_Filled_NoIrrigate.csv",
        )
    )

    # read training soil data filled

    df2 = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "3_Testing_Soil_Data_Selected_ColumnsV1_Filled.csv",
        )
    )

    # read training weather data filled
    df3 = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "4_Testing_Weather_Data_Selected_ColumnsV1_Filled.csv",
        )
    )
    # merge all data

    print(df.head())
    print("-----------------------------------------------")
    print(df1.head())

    df4 = pd.merge(df, df1, on=["Env"], how="outer")
    df5 = pd.merge(df4, df2, on=["Env"], how="outer")
    df6 = pd.merge(df5, df3, on=["Env"], how="outer")

    print(df6.head())
    print(df6.shape)
    print(df6.isnull().sum())

    df6 = checkAndFillNaDataFrame(df6)

    print(df6.head())
    print(df6.shape)
    print(df6.isnull().sum())

    # numeralize data
    df6 = numaricEncoder(df6)

    # check head of data
    print(df6.head())

    # write to csv neeeds to be around 5.4gb ()
    # df6.to_csv(
    #     os.path.join(
    #         "Data",
    #         "Testing_Data",
    #         "MergedTestingTrait_Meta_Soil_Weather.csv",
    #     ),
    #     index=False,
    # )

    df6.to_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "MergedTestingTrait_Meta_Soil_Weather_WithOuter.csv",
        ),
        index=False,
    )


def removeIrrigateFromMetedata():
    # read training meta data filled
    df1 = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "2_Testing_Meta_Data_Selected_ColumnsV1_Filled.csv",
        )
    )

    # drop Irrigate column
    df1.drop(columns=["Irrigated"], axis=1, inplace=True)

    # write the csv file
    df1.to_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "2_Testing_Meta_Data_2014_2021_Selected_Columns_Filled_NoIrrigate.csv",
        ),
        index=False,
    )


def numaricEncoder(df):  # encode the categorical data, best way to do it
    columnsToEncode = list(df.select_dtypes(include=["category", "object"]))
    le = LabelEncoder()

    for feature in columnsToEncode:
        try:
            df[feature] = le.fit_transform(df[feature])
        except:
            print("Error encoding " + feature)
    return df


def dropExtraColumnsforTestDataset():
    # read MergedTestingTrait_Meta_Soil_Weather.csv
    df = pd.read_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "MergedTestingTrait_Meta_Soil_Weather_WithOuter.csv",
        )
    )

    # drop columns
    data = df.drop(
        columns=["Year_x", "Year_y", "GWETPROF", "GWETTOP", "T2M_MAX", "Yield_Mg_ha"],
    )

    # write the csv file
    data.to_csv(
        os.path.join(
            "Data",
            "Testing_Data",
            "MergedTestingTrait_Meta_Soil_Weather_NoExtraColumns_WithOuter.csv",
        ),
        index=False,
    )


def rowCheker(df):  # derpericated
    # checks if train and test columns are same and true
    # if they are true return Hybrid name
    # else return false
    trainColumns = list(df.columns)
    testColumns = list(df.columns)
    if trainColumns == testColumns and trainColumns == "True":
        return df["Hybrid"]


def printToDF(str):
    # given a string creates numpy array and writes to csv
    # used to print the results to csv
    np.savetxt(
        os.path.join("Data", "Testing_Data", "Results.csv"),
        np.array(str),
        delimiter=",",
        fmt="%s",
    )

    # check if data frame has nan values
    # print(df.isnull().sum())
    # read latin

    # df = pd.read_csv(
    #     os.path.join("Data", "Testing_Data", "MergedTestingTrait_Meta_Soil_Weather.csv"), encoding="latin-1"
    # )
    # df2 drop columns
    # data = df2.drop(
    #     columns=["Year_x", "Year_y", "GWETPROF", "GWETTOP", "T2M_MAX", "Yield_Mg_ha"],
    # )

    # save to csv with data frame
    # df = pd.DataFrame(str)
    # df.to_csv(
    #     os.path.join("Data", "Testing_Data", "Results.csv"),
    #     index=False,
    # )

    # df size


def main():

    # mergeAllTrainingData()
    # removeIrrigateFromMetedata()
    # mergeAllTestData()
    # dropExtraColumnsforTestDataset()

    # read MergedTestingTrait_Meta_Soil_Weather_NoExtraColumns.csv
    # df = pd.read_csv(
    #     os.path.join(
    #         "Data",
    #         "Testing_Data",
    #         "MergedTestingTrait_Meta_Soil_Weather_NoExtraColumns.csv",
    #     )
    # )

    # # check feature size
    # print(df.shape)

    mergeAllTestData()
    dropExtraColumnsforTestDataset()

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
# read csv
# df = pd.read_csv(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "1_Training_Trait_Data_2014_2021_NoMissingYield.csv",
#     )
# )
# # fill na
# df = checkAndFillNaDataFrame(df)
# # numeralize data
# df = numaricEncoder(df)
# # save
# df.to_csv(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "1_Training_Trait_Data_2014_2021_NoMissingYield_Numeralized.csv",
#     ),
#     index=False,
# )

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

# dropColumnsForTrainingMetaData()

"""checkAndFillNaData(
        os.path.join(
            "Data",
            "Training_Data",
            "2_Training_Meta_Data_2014_2021_Selected_Columns.csv",
        ),
        os.path.join(
            "Data",
            "Training_Data",
            "2_Training_Meta_Data_2014_2021_Selected_Columns_Filled.csv",
        ),
    )"""

# dropColumnsForTrainingSoilData()

# checkAndFillNaData(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "3_Training_Soil_Data_2015_2021_Selected_Columns.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "3_Training_Soil_Data_2015_2021_Selected_Columns_Filled.csv",
#     ),
# )

# dropColumnsForTrainingWeatherData()

# checkAndFillNaData(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "4_Training_Weather_Data_2014_2021_Selected_Columns.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "4_Training_Weather_Data_2014_2021_Selected_Columns_Filled.csv",
#     ),
# )

# mergeTwoCsvFiles(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "1_Training_Trait_Data_2014_2021_NoMissingYield_Selected_Columns_Filled.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "2_Training_Meta_Data_2014_2021_Selected_Columns_Filled.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "MergedTrainingTrait_Meta.csv",
#     ),
#     "Env",
# )

# mergeTwoCsvFiles(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "MergedTrainingTrait_Meta.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "3_Training_Soil_Data_2015_2021_Selected_Columns_Filled.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "MergedTrainingTrait_Meta_Soil.csv",
#     ),
#     "Env",
# )

# mergeTwoCsvFiles(
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "MergedTrainingTrait_Meta_Soil.csv",
#     ),
#     os.path.join(
#         "Data",
#         "Training_Data",
#         "4_Training_Weather_Data_2014_2021_Selected_Columns_Filled.csv",
#     ),
#     # save directory
#     # E:\MaizeStuffTempDelete
#     "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather.csv",
#     "Env",
# )

# # make yield_mg_ha the last column
# df = pd.read_csv(
#     "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather_.csv",
#     encoding="latin-1",
# )
# cols = list(df.columns.values)
# cols.pop(cols.index("Yield_Mg_ha"))
# df = df[cols + ["Yield_Mg_ha"]]

# df = pd.read_csv(
#     "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather_YieldLast.csv",
#     encoding="latin-1",
# )

# # numeralize data
# df = numaricEncoder(df)

# # Check Head of Merged Data
# df.head().to_csv("E:\MaizeStuffTempDelete\HeadlastNumeralized.csv")

# # if head is good, save to csv
# df.to_csv(
#     "E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather_YieldLast.csv",
#     index=False,
# )

# # head for training
# # Env,Hybrid,Year_x,Yield_Mg_ha,Year_y,Treatment,Previous_Crop,Type_of_planter (fluted cone; belt cone; air planter),System_Determining_Moisture,Pounds_Needed_Soil_Moisture,Year,1:1 Soil pH,1:1 S Salts mmho/cm,Organic Matter LOI %,Potassium ppm K,Nitrate-N ppm N,Mehlich P-III ppm P,%Ca Sat,%Mg Sat,% Sand,% Silt,% Clay,Date,ALLSKY_SFC_PAR_TOT,RH2M,T2M_MAX,GWETPROF,GWETTOP,T2M_MIN,GWETROOT

# # numeralize columns
# df = pd.read_csv("E:\MaizeStuffTempDelete\MergedTrainingTrait_Meta_Soil_Weather.csv", encoding="latin-1")
# df = numeralizeColumns(df)

# mergeAllTrainingData()
