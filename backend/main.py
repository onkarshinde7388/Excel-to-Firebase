from fastapi import FastAPI
import firebase_admin
from firebase_admin import credentials, db
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # This allows requests from any domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Firebase
cred = credentials.Certificate("../firebase_creds.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://software-engineer-intern-default-rtdb.firebaseio.com/"})

@app.get("/")
def home():
    return {"message": "FastAPI is running"}

@app.get("/get-data")
def get_data():
    try:
        ref = db.reference("excel_data")  # Reference to Firebase
        data = ref.get()  # Get data from Firebase

        if data is None:
            return {"status": "error", "message": "No data found"}
        
        return {"status": "success", "data": data}
    
    
    
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    




