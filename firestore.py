import firebase_admin
from firebase_admin import credentials, firestore
import json
from google.protobuf.timestamp_pb2 import Timestamp

cred = credentials.Certificate("cosas.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

def firestore_converter(obj):
    # Detectar campos de fecha Firestore y convertir a string ISO
    if hasattr(obj, "isoformat"):
        return obj.isoformat()
    # Algunos tipos timestamp pueden necesitar otro manejo:
    if hasattr(obj, "ToDatetime"):
        return obj.ToDatetime().isoformat()
    raise TypeError(f"Tipo {type(obj)} no serializable")

all_data = {}
collections = db.collections()

for collection in collections:
    collection_name = collection.id
    docs = collection.stream()

    collection_data = {}
    for doc in docs:
        collection_data[doc.id] = doc.to_dict()

    all_data[collection_name] = collection_data

with open('firestore_completa.json', 'w') as f:
    json.dump(all_data, f, indent=4, default=firestore_converter)

print("Exportación de todas las colecciones completada.")
