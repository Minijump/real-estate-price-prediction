import os
import warnings
import pandas as pd

# This part will create one maincsv file from all the csv file we scraped
# it will also delete the collumns we do not use for the deployment
# panda data frame containing every infos
col_names = [
    "Locality",
    "Type_of_property",
    "Subtype_of_property",
    "Price",
    "Type_of_sale",
    "Number_of_rooms",
    "Living_Area",
    "Fully_equipped_kitchen",
    "Furnished",
    "Open_fire",
    "Terrace",
    "Terrace_Area",
    "Garden",
    "Garden_Area",
    "Surface_of_the_land",
    "Surface_area_of_the_plot_of_land",
    "Number_of_facades",
    "Swimming_pool",
    "State_of_the_building",
]
df_final = pd.DataFrame(columns=col_names)

def create_df():
    """
    create a dataframe from all the csv we created
    """
    # List all files in the directory
    global df_final
    df_final = pd.DataFrame(columns=col_names)

    # path = "./all_csv"
    path = r"C:\Users\Sacha\Documents\BeCode\real-estate-price-prediction\data_acquisition\all_csv"
    files = os.listdir(path)

    for file in files:
        if os.path.isfile(os.path.join(path, file)):
            file_path = (
                r"C:\Users\Sacha\Documents\BeCode\real-estate-price-prediction\data_acquisition\all_csv\\"
                + file
            )
            file_df = pd.read_csv(file_path)
            with warnings.catch_warnings():  # warnings from panda because columns with only bool
                warnings.simplefilter("ignore")
                df_final = pd.concat([df_final, file_df])

def del_columns():
    """
    this function clean the data a first time, it will delete useless lines or columns
    """
    global df_final

    # we only keep residential sales
    df_final = df_final[df_final["Type_of_sale"] == "residential_sale"]
    del df_final["Type_of_sale"]
    # drop lines full of nan
    df_final = df_final.dropna(how="all")

    #keep only the columns used for the doplyment
    df_final = df_final[['Living_Area', 'Type_of_property', 'Locality', 'Swimming_pool', 'Number_of_rooms', 'Price']]
    # this line will drop lines where Price, the living area, Type_of_property, locality the type_of_property is missing
    df_final = df_final.dropna(subset=["Price"])
    df_final = df_final.dropna(subset=["Living_Area"])
    df_final = df_final.dropna(subset=["Type_of_property"])
    df_final = df_final.dropna(subset=["Locality"])
    df_final = df_final.dropna(subset=["Number_of_rooms"])

    # remove_duplicates
    df_final = df_final.drop_duplicates()

def save_df():
    """
    save tthe global df into a csv
    """
    global df_final
    df_final.to_csv("ready_to_learn_csv.csv", index=False)

if __name__ == "__main__":
    create_df()
    del_columns()
    save_df()