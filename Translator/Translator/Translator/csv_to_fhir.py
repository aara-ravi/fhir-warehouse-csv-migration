import csv
import uuid
import requests

FHIR_SERVER = "http://localhost:8080/fhir"

bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}

with open("patients.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        patient_uuid = str(uuid.uuid4())

        patient = {
            "resourceType": "Patient",
            "id": patient_uuid,
            "gender": "male" if row["gender"] == "M" else "female",
            "birthDate": row["dob"]
        }

        bundle["entry"].append({
            "fullUrl": f"urn:uuid:{patient_uuid}",
            "resource": patient,
            "request": {
                "method": "POST",
                "url": "Patient"
            }
        })

# Transactional POST
response = requests.post(FHIR_SERVER, json=bundle)
print(response.status_code)
