def visual(file):
    from pymysql import connect
    import matplotlib.pyplot as plt
    import seaborn as sns
    import plotly.express as px
    import plotly.graph_objects as go
    import warnings
    warnings.filterwarnings("ignore")
    import pandas as pd
    data=connect(host="localhost",user="root",password="Karthimoha@97",database="karthi")
    query="select * from Cleaned_loan_approval_dataset_PESV"
    HS=pd.read_sql(query,data)
    data.close()

    # Segmented uni-varient analysis of loan_term.
    
    sns.histplot(HS[" loan_term"],bins=20,kde=True)
    plt.title("Histogram plot of  loan_term")
    plt.xlabel(" loan_term")
    plt.ylabel("count")
    plt.show()

    # Box Plot for loan_amount

    sns.boxplot(x=" loan_amount",data=HS)
    plt.title("Box plot of  loan_amount")
    plt.xlabel(" loan_amount")
    plt.show()

    
    # Segmented bi-variate analysis.

    sns.barplot(y=" cibil_score",x=" loan_status",data=HS)
    plt.title("Bar plot of  cibil_score vs condition")
    plt.ylabel(" cibil_score")
    plt.xlabel(" loan_status")
    plt.show()

    # Heatmap for income_annum,loan_amount,loan_term Correlation

    correlation_matrix = HS[[' income_annum', ' loan_amount', ' loan_term']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap for income_annum,loan_amount,loan_term')
    plt.show()

    # Heatmap for residential_assets_value,loan_amount, commercial_assets_value Correlation

    correlation_matrix = HS[[' residential_assets_value', ' loan_amount', ' commercial_assets_value']].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(correlation_matrix, annot=True, cmap='BuPu', vmin=-1, vmax=1)
    plt.title('Correlation Heatmap for  residential_assets_value,loan_amount, commercial_assets_value')
    plt.show()

    # Bar plot of  loan_term vs loan_status
    
    sns.barplot(y=" loan_term",x=" loan_status",data=HS)
    plt.title("Bar plot of  loan_term vs loan_status")
    plt.ylabel(" loan_term")
    plt.xlabel(" loan_status")
    plt.show()

    # Bar plot of   income_annum vs loan_status
    
    sns.barplot(y=" income_annum",x=" loan_status",data=HS)
    plt.title("Bar plot of   income_annum vs loan_status")
    plt.ylabel(" income_annum")
    plt.xlabel(" loan_status")
    plt.show()

    # countplot of no_of_dependents and loan_status
    
    plt.figure(figsize=(12,7))
    sns.countplot(data=HS,x=' no_of_dependents',hue=' loan_status')

    # numerical attributes visualization of income_annum
    
    sns.distplot(HS[" income_annum"])

    # Area chart of loan approval
    
    import plotly.express as px
    fig = px.area(HS, x=' loan_amount', y=' loan_status')
    fig.show()
    
   
    #Pie chart for distribution of company sizes

    Loan_amount = HS[' loan_amount'].value_counts()
    plt.figure(figsize=(8, 8))
    plt.pie(Loan_amount, labels=Loan_amount.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
    plt.title('Composition of Loan_amount')
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.show()

    