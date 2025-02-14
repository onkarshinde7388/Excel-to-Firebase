import pandas as pd
import firebase_admin
from firebase_admin import credentials, db


cred = credentials.Certificate("firebase_creds.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://software-engineer-intern-default-rtdb.firebaseio.com/"})

def upload_excel_to_firebase(file_path):
    
    df = pd.read_excel(file_path)

   
    for col in df.select_dtypes(include=['datetime64']):
        df[col] = df[col].astype(str)

   
    data_dict = df.to_dict(orient="records")

  
    ref = db.reference("excel_data")
    ref.set(data_dict)

    print(" Data uploaded successfully!")


upload_excel_to_firebase("data.xlsx")



