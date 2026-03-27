import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score

from matplotlib import pyplot as plt
import seaborn as sns


# ===============================================================
# Function name : DisplayInfo
# Description : It displays the formated title
# Parameters : title (str)
# Return: None
# ===============================================================


def DisplayInfo(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

# ===============================================================
# Description : It shows basic infromation about the data
# Parameters  : df
#             : df -> pandas dataframe object
#             : message
#             : showData -> Heading text to Display
# Return      : None
# ===============================================================

def ShowData(df,message):
    DisplayInfo(message)

    print("\nFirst 5 rows in dataset:")
    print(df.head())

    print("\nShape of dataset:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nMissing values in each column:")
    print(df.isnull().sum())

    print("\nAll statistical summary of dataset:")
    print(df.describe())

# ===============================================================
# Function name : PlotGraph
# Description : It plots the graph based on the given parameters
# Parameters : DataPath of dataset file
# ===============================================================

def PlotGraph(df):
        DisplayInfo("Data Visualization")
        plt.figure(figsize=(10, 6))
        sns.histplot(x='Outcome', data=df)
        plt.title('Distribution of Diabetes Outcome')
        plt.xlabel('Outcome (0 = No Diabetes, 1 = Diabetes)')
        plt.ylabel('Count')
        plt.show()

# ===============================================================
# Function name : DibetesData
# Description : This is main pipeline controller
#               It loads the dataset, show raw data 
#               It preprocess the dataset and train the model
# Parameters : DataPath of dataset file
# Return: None
# ===============================================================

def DibetesData(Datapath):
    # Load the diabetes dataset
    df = pd.read_csv(Datapath)
    ShowData(df,"Diabetes Dataset Information")

# ===============================================================
# Function name : main
# Description : Starting point of the application
# Parameters : None
# Return: None
# ===============================================================

def main():
    DibetesData("diabetes.csv")
    PlotGraph(pd.read_csv("diabetes.csv"))


if __name__ == "__main__":
    main()