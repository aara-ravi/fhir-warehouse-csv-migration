# FHIR Warehouse CSV Migration Project

## Overview
This project demonstrates a simple, stateful FHIR warehouse architecture for migrating legacy CSV data into FHIR resources.
The focus of this repository is on architectural design, semantic integrity, and transactional safety rather than runtime execution.

---

## Infrastructure (Container Advantage)
A HAPI FHIR server is provisioned using Docker to avoid local dependency issues such as Java and database setup.
Docker ensures a consistent execution environment across different machines.

Port mapping (8080:8080) is used to expose the FHIR server running inside the container to the host machine, allowing local scripts to interact with the server via `http://localhost:8080/fhir`.

---

## Rulebook (FHIR Shorthand Profiles)
FHIR is intentionally permissive by design.
To ensure data quality and safety, local constraints were authored using FHIR Shorthand (FSH).

A simple Patient profile enforces mandatory fields such as:
- gender
- birthDate

These constraints ensure that only valid and clinically meaningful data enters the warehouse.

---

## Translator (CSV to FHIR Migration)
Legacy data is provided in a flat CSV format.
A Python-based translator reads the CSV and converts each row into a FHIR Patient resource.

To maintain data consistency:
- Transaction Bundles are used
- UUID-based references are generated
- All resources are created atomically in a single request

This prevents partial writes and orphaned clinical data.

A sample anonymised CSV file is included for demonstration purposes.

---

## Semantic Integrity
Legacy systems often store values as informal strings such as "M" or "F".
These values are translated into FHIR-compliant codes ("male", "female") within the migration logic.

This ensures semantic correctness and interoperability with downstream systems.

---

## Execution Note
This repository focuses on demonstrating architectural principles.
All infrastructure and scripts are provided for reproducible local execution, though actual runtime execution is not required for evaluation.

