# Source to Target Mapping (STM)

This document describes how legacy CSV columns are mapped to FHIR resources.

| CSV Column | Description        | FHIR Resource | FHIR Element        |
|------------|--------------------|---------------|---------------------|
| id         | Patient Identifier | Patient       | Patient.id          |
| gender     | M / F              | Patient       | Patient.gender      |
| dob        | Date of Birth      | Patient       | Patient.birthDate   |
