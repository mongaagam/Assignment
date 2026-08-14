# S3 CSV Analysis

## Overview

This project demonstrates a simple CSV statistics workflow using **Amazon EC2**, **Amazon S3**, **IAM**, and **AWS STS**.

The application reads a CSV file directly from an S3 bucket, analyzes the CSV data, and stores the generated statistics report in the S3 `output/` location.

The original Week Challenge project is kept separate from this project.

---

## Architecture

```text
                    AWS
                     |
             +-------+-------+
             |               |
             v               v
        Amazon EC2       Amazon S3
        Python App       agam-csvstat
             |               |
             |         +-----+------+
             |         |            |
             |      input/        output/
             |         |            |
             |         v            v
             |    file1_3.csv  csvstat_output.txt
             |         |
             +---------+
                Read CSV
```

---

## AWS Services Used

- **Amazon EC2** – runs the Python CSV analysis application.
- **Amazon S3** – stores the input CSV and generated output report.
- **AWS IAM** – provides the EC2 instance with permissions to access S3.
- **AWS STS** – verifies the AWS identity being used by the EC2 instance.

---

## S3 Bucket Structure

### Bucket

```text
s3://agam-csvstat/
```

### Structure

```text
agam-csvstat/
├── input/
│   └── file1_3.csv
└── output/
    └── csvstat_output.txt
```

### Input File

```text
s3://agam-csvstat/input/file1_3.csv
```

### Output File

```text
s3://agam-csvstat/output/csvstat_output.txt
```

---

## Workflow

1. The sample CSV file is stored in the S3 `input/` folder.
2. The EC2 instance uses its attached IAM instance profile to access Amazon S3.
3. The Python program reads the CSV file directly from S3.
4. The program analyzes rows, columns, data types, missing values, and numeric statistics.
5. The generated report is stored in the S3 `output/` folder.

### Workflow Diagram

```text
S3 Input
   |
   v
input/file1_3.csv
   |
   v
EC2 Instance
   |
   v
Python CSV Analysis
   |
   v
Generated Report
   |
   v
S3 Output
   |
   v
output/csvstat_output.txt
```

---

## Security

The EC2 instance uses an **IAM instance profile** for AWS authentication.

- No AWS access keys are hardcoded in the Python code.
- No long-term AWS access keys are manually configured on the EC2 instance.
- AWS credentials are supplied through the attached IAM role.
- AWS STS is used to verify the active AWS identity.

### Verify AWS Identity

```bash
aws sts get-caller-identity
```

---

## Python Dependencies

The project uses Python and **boto3** for S3 access.

### Install Dependencies

```bash
pip3 install boto3
```

---

## Running the CSV Analysis

The input CSV is read directly from S3.

### Example

```bash
python3 csvstat_3.py s3://agam-csvstat/input/file1_3.csv
```

The generated report is stored in the S3 `output/` location.

---

## Sample Input

The sample CSV contains the following columns:

```text
Name,Age,Country,Revenue,Date
```

### Example Data

```csv
Name,Age,Country,Revenue,Date
Agam,19,India,1200,2026-08-01
Divanshu,19,India,1500,2026-08-03
Anish,21,Canada,900,2026-08-05
Rahul,20,USA,2100,2026-08-07
Priya,22,India,1800,2026-08-10
```

---

## CSV Analysis Performed

The program calculates:

- Number of rows
- Number of columns
- Column data type
- Missing values
- Missing percentage
- Minimum value for numeric columns
- Mean value for numeric columns
- Maximum value for numeric columns
- Top values for text columns when requested

---

## Sample Output

```text
Rows: 6
Columns: 5

Column: Name
Type: text
Missing: 0
Missing %: 0.0

Column: Age
Type: numeric
Missing: 0
Missing %: 0.0
Min: 19.0
Mean: 20.2
Max: 22.0

Column: Country
Type: text
Missing: 0
Missing %: 0.0

Column: Revenue
Type: numeric
Missing: 0
Missing %: 0.0
Min: 900.0
Mean: 1500.0
Max: 2100.0

Column: Date
Type: text
Missing: 0
Missing %: 0.0
```

---

# Screenshots

## 1. EC2 Instance Connection
<img width="1470" height="280" alt="S3 Input Output Structure" src="https://github.com/user-attachments/assets/fcc72486-3203-4bc8-b1b5-a0f5a97dbca6" />


---

## 2. S3 Integration in Python

This section shows the changes made in `csvstat_3.py` to read the CSV file directly from Amazon S3 using `boto3`.
<img width="1470" height="403" alt="S3 Bucket" src="https://github.com/user-attachments/assets/ee15ed09-3d40-481d-a23f-ca367dd30038" />

---

## 3. S3 Input/Output Structure

<img width="1470" height="491" alt="Screenshot 2026-08-14 at 9 02 18 PM" src="https://github.com/user-attachments/assets/90f5e93a-4399-4bc4-9050-e63e77711a52" />

---

---

## 4. S3 Input Structure

<img width="1465" height="595" alt="Screenshot 2026-08-14 at 7 47 13 PM" src="https://github.com/user-attachments/assets/2f79e6ff-4afc-4e48-9e56-f5d1ee50e618" />

---

## 5. S3 Output Structure

<img width="1466" height="585" alt="Screenshot 2026-08-14 at 7 47 17 PM" src="https://github.com/user-attachments/assets/b89f9a10-1387-48e7-8891-98aa3f37473e" />

---

## 6. CSV Analysis Output

The following screenshot shows the generated CSV statistics report from the Python analysis.

<img width="1470" height="766" alt="Screenshot 2026-08-14 at 8 57 59 PM" src="https://github.com/user-attachments/assets/5930beee-aaed-4341-be26-9a0f30ac28aa" />


## Repository Structure

```text
cloud/
├── README.md
├── input/
│   └── file1_3.csv
└── output/
    └── csvstat_output.txt
```

---

## Definition of Done

- [x] EC2 instance is running.
- [x] Project dependencies are installed.
- [x] S3 bucket `agam-csvstat` exists.
- [x] S3 contains `input/` and `output/` locations.
- [x] Sample CSV is stored in the `input/` location.
- [x] EC2 uses an IAM instance profile for S3 access.
- [x] No AWS access keys are hardcoded in the project.
- [x] CSV input is read from S3.
- [x] CSV statistics are generated.
- [x] The report is stored in the S3 `output/` location.

---

## Result

The project demonstrates the complete workflow:

```text
S3 Input
   |
   v
EC2 Instance
   |
   v
Python CSV Analysis
   |
   v
Generated Report
   |
   v
S3 Output
```

This project demonstrates a simple and secure cloud-based CSV analysis workflow using an EC2 IAM role instead of hardcoded AWS credentials.
