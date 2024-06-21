def connection(file):
    from sqlalchemy import create_engine
    import pandas as pd

    LD=pd.read_csv(f'{file}')     # reading the csv file.

    my_conn=create_engine("mysql://root:Karthimoha%4097@localhost/karthi")   # creating the engine.

    try:
        LD.to_sql('loan_approval_dataset_PESV', con=my_conn, if_exists="replace", index=False)      # appending in to the sql.
    
                        # Query to select all data from the table
        query = f"SELECT * FROM {LD}"
        HS = pd.read_sql(query, con=my_conn)
    
                        # Print the retrieved DataFrame
        print(HS)

    except Exception as e:
        print("Error:", e)