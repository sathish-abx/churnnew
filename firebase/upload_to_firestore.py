import csv
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase
cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

# Function to upload CSV to Firestore with sequential document names
def upload_csv_to_firestore(collection_name, csv_file_path):
    with open(csv_file_path, mode="r") as file:
        csv_reader = csv.DictReader(file)
        counter = 1  # Initialize counter for document names
        for row in csv_reader:
            # Create document name as data1, data2, etc.
            document_name = f"data{counter}"
            # Add each row as a document in the Firestore collection
            db.collection(collection_name).document(document_name).set(row)
            counter += 1  # Increment counter

# Upload CSV file to Firestore

# upload_csv_to_firestore("2023Quarter1", "2023Quarter1.csv")
# upload_csv_to_firestore("2023Quarter2", "2023Quarter2.csv")
# upload_csv_to_firestore("2023Quarter3", "2023Quarter3.csv")
# upload_csv_to_firestore("2023Quarter4", "2023Quarter4.csv")
# upload_csv_to_firestore("2024Quarter1", "2024Quarter1.csv")
# upload_csv_to_firestore("2024Quarter2", "2024Quarter2.csv")
# upload_csv_to_firestore("2024Quarter3", "2024Quarter3.csv")
# upload_csv_to_firestore("2024Quarter4", "2024Quarter4.csv")

print("Data uploaded to Firestore successfully!")