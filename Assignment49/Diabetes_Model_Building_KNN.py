import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report,accuracy_score, precision_score,f1_score
from sklearn.preprocessing import StandardScaler
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
# Function name : CleanDiabetesData
# Description : It does preprocessing
#             : It removed unnecessary columns
#             : It handles missing values
#             : It converts text data to numeric format
#             : It does encoding to categorical columns
# Parameters : DataPath of dataset file
# Return: None
# ===============================================================
def CleanDiabetesData(df):
    DisplayInfo("Step 2 : Originial Data")
    print(df.head())

     # Checking for missing values in columns

     # for column 'Pregnancies'

    if "Pregnancies" in df.columns:
          print("Pregnancies column before filling missing values")
          print(df["Pregnancies"].head(10))

          # Invalid value gets converted as NaN
          df["Pregnancies"] = pd.to_numeric(df["Pregnancies"],errors="coerce")

          Pregnancies_median = df["Pregnancies"].median()

          # Replace missing values with median
          df["Pregnancies"] = df["Pregnancies"].fillna(Pregnancies_median)
          
          print("\nPregnancies column after processing")
          print(df["Pregnancies"].head(10))
    
    if "Glucose" in df.columns:
          print("Glucose column before filling missing values")
          print(df["Glucose"].head(10))

          # Invalid value gets converted as NaN
          df["Glucose"] = pd.to_numeric(df["Glucose"],errors="coerce")

          Glucose_median = df["Glucose"].median()

          # Replace missing values with median
          df["Glucose"] = df["Glucose"].fillna(Glucose_median)
          
          print("\nGlucose column after processing")
          print(df["Glucose"].head(10))
    
    if "BloodPressure" in df.columns:
          print("BloodPressure column before filling missing values")
          print(df["BloodPressure"].head(10))

          # Invalid value gets converted as NaN
          df["BloodPressure"] = pd.to_numeric(df["BloodPressure"],errors="coerce")

          BloodPressure_median = df["BloodPressure"].median()

          # Replace missing values with median
          df["BloodPressure"] = df["BloodPressure"].fillna(BloodPressure_median)
          
          print("\nBloodPressure column after processing")
          print(df["BloodPressure"].head(10))
    
    if "SkinThickness" in df.columns:
          print("SkinThickness column before filling missing values")
          print(df["SkinThickness"].head(10))

          # Invalid value gets converted as NaN
          df["SkinThickness"] = pd.to_numeric(df["SkinThickness"],errors="coerce")

          SkinThickness_median = df["SkinThickness"].median()

          # Replace missing values with median
          df["SkinThickness"] = df["SkinThickness"].fillna(SkinThickness_median)
          
          print("\nSkinThickness column after processing")
          print(df["SkinThickness"].head(10))
        

    if "Insulin" in df.columns:
            print("Insulin column before filling missing values")
            print(df["Insulin"].head(10))

        # Invalid value gets converted as NaN
            df["Insulin"] = pd.to_numeric(df["Insulin"],errors="coerce")

            Insulin_median = df["Insulin"].median()

          # Replace missing values with median
            df["Insulin"] = df["Insulin"].fillna(Insulin_median)
          
            print("\nInsulin column after processing")
            print(df["Insulin"].head(10))

    if "BMI" in df.columns:
            print("BMI column before filling missing values")
            print(df["BMI"].head(10))

        # Invalid value gets converted as NaN
            df["BMI"] = pd.to_numeric(df["BMI"],errors="coerce")

            BMI_median = df["BMI"].median()

          # Replace missing values with median
            df["BMI"] = df["BMI"].fillna(BMI_median)
          
            print("\nBMI column after processing")
            print(df["BMI"].head(10))

    if "DiabetesPedigreeFunction" in df.columns:
            print("DiabetesPedigreeFunction column before filling missing values")
            print(df["DiabetesPedigreeFunction"].head(10))

        # Invalid value gets converted as NaN
            df["DiabetesPedigreeFunction"] = pd.to_numeric(df["DiabetesPedigreeFunction"],errors="coerce")

            DiabetesPedigreeFunction_median = df["DiabetesPedigreeFunction"].median()

          # Replace missing values with median
            df["DiabetesPedigreeFunction"] = df["DiabetesPedigreeFunction"].fillna(DiabetesPedigreeFunction_median)
          
            print("\nDiabetesPedigreeFunction column after processing")
            print(df["DiabetesPedigreeFunction"].head(10))
    
    if "Age" in df.columns:
            print("Age column before filling missing values")
            print(df["Age"].head(10))

        # Invalid value gets converted as NaN
            df["Age"] = pd.to_numeric(df["Age"],errors="coerce")

            Age_median = df["Age"].median()

          # Replace missing values with median
            df["Age"] = df["Age"].fillna(Age_median)
          
            print("\nAge column after processing")
            print(df["Age"].head(10))
    
    return df


# ===============================================================
# Function name : ScalingData
# Description : It will scale the data 
# Parameters : DataPath of dataset file
# ===============================================================

def ScalingData(df):
      X = df.drop("Outcome", axis=1)
      print("Scaled features")
      print(X.head())

      scaler = StandardScaler()
      X_scaled = scaler.fit_transform(X)
      print("Data after scaling :")
      print(X_scaled[:5])


# ===============================================================
# Function name : SplitingData_BuildingModel
# Description : It will split the data into train and test set also build the model
# Parameters : DataPath of dataset file
# ===============================================================

def SplitingData_BuildingModel(df):
    DisplayInfo("Step 4 : Model Building")
    
    X= df.drop("Outcome", axis=1)
    Y = df["Outcome"]

    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=.02,random_state=42)

    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)
    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)
    
    scaler = StandardScaler()
    X_train_Scaled = scaler.fit_transform(X_train)
    X_test_Scaled = scaler.transform(X_test)

    accuracy_scores = []
    k_values = range(1,21)

    for k in k_values:
          model = KNeighborsClassifier(n_neighbors=k)

          model.fit(X_train_Scaled,Y_train)

          Y_pred = model.predict(X_test_Scaled)

          accuracy = accuracy_score(Y_test,Y_pred)
          
          accuracy_scores.append(accuracy)

          print("Accuracy for k =",k,":",accuracy)

    for value in accuracy_scores:
          print(value)
    

    # find best value of k

    best_k = list(k_values)[accuracy_scores.index(max(accuracy_scores))]
    print("Best value of k:",best_k)

    # Final model with best k value
    final_model = KNeighborsClassifier(n_neighbors=best_k)

    final_model.fit(X_train_Scaled,Y_train)

    Y_pred = final_model.predict(X_test_Scaled)

    accuracy = accuracy_score(Y_test,Y_pred)
    print("\nAccuracy of the model:",accuracy)

    cm = confusion_matrix(Y_test,Y_pred)
    print("\nConfusion Matrix:")
    print(cm)

    # Visualize Confusion Matrix using seaborn
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=True)
    plt.title('Confusion Matrix - KNN Model')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    print("\nClassification Report:")
    print(classification_report(Y_test,Y_pred))

    print("\nAccuracy Score:")
    print(accuracy)

    print("\nPrecision Score:")
    print(precision_score(Y_test,Y_pred))

    print("\nF1 Score:")
    print(f1_score(Y_test,Y_pred))

    # ===============================================================
    # Final Output: Predictions on test data
    # ===============================================================
    DisplayInfo("Step 5 : Final Output - Predictions")
    
    # Display predictions on screen
    print("\nPredictions on test data:")
    print("First 10 predictions:")
    print(Y_pred[:10])
    
    print("\nActual values for first 10 test samples:")
    print(Y_test.values[:10])
    
    # Create a dataframe with predictions and actual values
    predictions_df = pd.DataFrame({
        'Actual': Y_test.values,
        'Predicted': Y_pred,
        'Diabetic': ['Yes' if pred == 1 else 'No' for pred in Y_pred]
    })
    
    print("\nPredictions DataFrame (first 10 rows):")
    print(predictions_df.head(10))
    
    # Save predictions to CSV file
    csv_filename = "Diabetes_Predictions_Using_KNN.csv"
    predictions_df.to_csv(csv_filename, index=False)
    print(f"\nPredictions saved to '{csv_filename}'")
    print(f"Total predictions: {len(predictions_df)}")

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
    df = CleanDiabetesData(df)
    ScalingData(df)
    SplitingData_BuildingModel(df)

# ===============================================================
# Function name : main
# Description : Starting point of the application
# Parameters : None
# Return: None
# ===============================================================

def main():
    DibetesData("diabetes.csv")
    #PlotGraph(pd.read_csv("diabetes.csv"))


if __name__ == "__main__":
    main()