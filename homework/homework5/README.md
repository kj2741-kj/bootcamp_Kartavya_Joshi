#Data Storage:
This project utilizes a structured approach for storing data, separating raw files from processed ones. The paths are managed via environment variables for flexibility, with sensible defaults provided.

#Folder Structure:
The data is organized into two main directories within a top-level data/ folder:

data/raw/: This directory is the designated location for initial, unprocessed data. In this project, it is used to store the synthetically generated customer data as a CSV file. It serves as the single source of truth for the original dataset.

data/processed/: This directory contains data that has been cleaned, transformed, or optimized for performance. The raw CSV data is converted into the more efficient Parquet format and saved here, ready for analytical workloads.

#Data Formats Used:
Two primary file formats are used in this workflow:

CSV (.csv): Used for storing the raw data in data/raw/.

Parquet (.parquet): Used for storing the processed data in data/processed/.

#How the Code Reads and Writes Data:
The code is designed to be flexible and robust in handling data I/O:

*Environment Variables*: The paths to the raw and processed data directories are configured using environment variables (DATA_DIR_RAW and PROCESS_DIR_RAW). If these are not set, the code falls back to default paths (data/raw and data/processed respectively), making the script portable and easy to configure.

*Utility Functions*: The notebook defines helper functions, write_df and read_df, to manage file operations. These functions automatically detect the desired file format (CSV or Parquet) based on the file extension of the provided path. This abstraction simplifies the code and removes the need to call specific pd.to_csv or pd.to_parquet functions in the main logic.
