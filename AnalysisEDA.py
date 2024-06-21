def Analysis_EDA(file):
    import pandas as pd 
    import numpy as np
    import datetime as dt
    import matplotlib.pyplot as plt
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")
    import math
    # Reading the "housing" dataset, housing as HS

    HS = pd.read_csv("loan_approval_dataset_PESV.csv")
    # Basic Information of dataset

    HS.info()
    # Describing the housing dataset

    HS.describe()
    # To view the columns of dataset

    HS.columns
    # To view the index of dataset

    HS.index
    # Shape of dataset

    HS.shape
    # Size of dataset

    HS.size
    # First 5 records of the dataset

    HS.head()
    # Last 5 records of dataset

    HS.tail()
    # to see the unique values in columns

    HS.apply(lambda x:x.unique()) 
    # Number of missing values in each column in each rows

    HS.isnull().sum()
    # No of missing values in each row in every column

    HS.isnull().sum(axis=1)
    # Total number of missing values in dataset

    HS.isnull().sum().sum()
    # Percentage of missing values in each column

    round(100*(HS.isnull().sum()/len(HS.index)),2).sort_values(ascending=False).head(15)
    HS=HS.dropna()
    # Numeric columns are stored in the variable "numeric_columns"

    numeric_columns = HS.select_dtypes(include=["float","int"])
    # Boxplots are plotted for numeric columns to check outliers

    plt.figure(figsize=(15,30))
    for i in range(len(numeric_columns.columns)):
        plt.subplot(10,3,i+1)
        sns.boxplot(y = numeric_columns.columns[i], data=HS)
    plt.show()
    # Numeric columns are stored in the variable "numeric_columns"

    numeric_columns = HS.select_dtypes(include=["number"]).columns
    from scipy.stats import zscore
    HS = HS[(zscore(HS[numeric_columns]) < 2.5).all(axis=1)]
    
    HS[" income_annum"].describe()
    # Adding a column " cibil_category" based on  " cibil_score"
    
    """ we shall create a derived column " cibil_category" -which contains bins of different categories of " cibil_score".
    categories - [300-550],[551-650],[651-750],[751-900]"""

    HS[" cibil_category"] = pd.cut(x=HS[" cibil_score"],bins=[300,550,650,750,900])
    HS[" cibil_category"] = HS[" cibil_category"].cat.codes
    HS[" cibil_category"] = HS[" cibil_category"].map({0:"Poor",1:"Average",2:"Good",3:"Execellent"})

    # Univariate analysis of " loan_amount" using skewness and kurtosis

    # Calculation of skewness for  loan_amount
    import scipy
    from scipy.stats import skew
    
    UA=HS[" loan_amount"]
    print(skew(UA,axis=0,bias=True))

    # Calculation of kurtosis for loan_amount

    import scipy
    from scipy.stats import kurtosis
    
    UA=HS[" loan_amount"]
    print(kurtosis(UA,axis=0,bias=True))

    VA_C=HS[[" income_annum"," loan_amount"," loan_term"," cibil_score"," residential_assets_value"," commercial_assets_value",
        " luxury_assets_value"," bank_asset_value"]]
    VA_D=HS[" loan_status"]
    from sklearn.feature_selection import SelectKBest, f_classif
    from sklearn.feature_selection import chi2
    
    # Apply Anova (x^2) statistical test for feature selection using anova function

    best_features=SelectKBest(score_func=f_classif,k=1) 
    fit=best_features.fit(VA_C,VA_D)
    selected_features=VA_C.columns[fit.get_support()]
    print("The highly correlated column for loan approval is",selected_features)

    # Apply Anova (x^2) statistical test for feature selection using anova function

    best_features=SelectKBest(score_func=f_classif,k=2) 
    fit=best_features.fit(VA_C,VA_D)
    selected_features=VA_C.columns[fit.get_support()]
    print("The highly correlated two columns for loan approval is",selected_features)

    # Apply Anova (x^2) statistical test for feature selection using anova function

    best_features=SelectKBest(score_func=f_classif,k=3) 
    fit=best_features.fit(VA_C,VA_D)
    selected_features=VA_C.columns[fit.get_support()]
    print("The highly correlated three columns for loan approval is",selected_features)

    from sqlalchemy import create_engine
    my_conn=create_engine("mysql://root:Karthimoha%4097@localhost/karthi")

    try:
        HS.to_sql("Cleaned_loan_approval_dataset_PESV", con=my_conn, if_exists="replace", index=False)
    
        # Query to select all data from the table
        query = "SELECT * FROM Cleaned_loan_approval_dataset_PESV"
        HSD = pd.read_sql(query, con=my_conn)
    
        # Print the retrieved DataFrame
        print(HSD)

    except Exception as e:
        print("Error:", e)


    
    
    