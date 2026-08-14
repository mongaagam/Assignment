import argparse
import csv
from collections import Counter
import boto3
import io

#s3 Reader function
def get_file(path):
    if path.startswith("s3://"):
        s3=boto3.client("s3")

        bucket_key=path[5:]
        bucket,key=bucket_key.split("/",1)

        response=s3.get_object(
            Bucket=bucket,
            Key=key
        )

        content=response["Body"].read().decode("utf-8")
     
        return io.StringIO(content)
    return open(path,"r")

# Count rows
def rows(path):
    with get_file(path) as file:
        reader = csv.reader(file)

        # Skip header
        next(reader, None)
        count = 0
        for row in reader:
            count += 1

        return count


# Count columns
def columns(path):
    with get_file(path) as file:
        reader = csv.reader(file)
        header = next(reader, None)
        if header is None:
            return 0

        return len(header)


# Check numeric value
def is_numeric(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


# Detect column type
def detect_type(values):
    non_empty_values = []

    for value in values:
        if value.strip() != "":
            non_empty_values.append(value)

    if len(non_empty_values) > 0:
        if all(is_numeric(value) for value in non_empty_values):
            return "numeric"

    return "text"


# Check columns
def check_columns(path, top_n=None):
    with get_file(path) as file:
        reader = csv.DictReader(file)

        data = list(reader)

        for column in reader.fieldnames:

            # Values of current column
            values = []

            for row in data:
                values.append(row[column])

            # Column type
            column_type = detect_type(values)

            print("\nColumn:", column)
            print("Type:", column_type)

            # Missing values
            missing = 0

            for value in values:
                if value.strip() == "":
                    missing += 1

            print("Missing:", missing)

            # Missing percentage
            total = len(values)

            if total > 0:
                missing_percentage = (missing / total) * 100
            else:
                missing_percentage = 0

            print("Missing %:", missing_percentage)

            # Numeric statistics
            if column_type == "numeric":

                numeric_values = []

                for value in values:
                    if value.strip() != "":
                        numeric_values.append(float(value))

                if len(numeric_values) > 0:
                    print("Min:", min(numeric_values))
                    print(
                        "Mean:",
                        sum(numeric_values) / len(numeric_values)
                    )
                    print("Max:", max(numeric_values))

            # Text statistics
            if column_type == "text" and top_n is not None:

                counts = Counter(values)

                print("Top values:")

                for value, count in counts.most_common(top_n):
                    print(value, count)


# Main function
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "csv_path",
        help="Path to the CSV file"
    )

    parser.add_argument(
        "--top",
        type=int,
        help="Show top N values for text columns"
    )

    args = parser.parse_args()

    path = args.csv_path
    top_n = args.top

    print("Rows:", rows(path))
    print("Columns:", columns(path))

    check_columns(path, top_n)


if __name__ == "__main__":
    main()
