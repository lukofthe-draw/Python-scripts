import os
import re

def convert_sql_file(filename):
    # Read the SQL file
    with open(filename, "r") as f:
        sql = f.read()

    # Convert the SQL file to the correct format
    sql = re.sub(r"AUTO_INCREMENT", "AUTOINCREMENT", sql)
    sql = re.sub(r"INT PRIMARY KEY", "INTEGER PRIMARY KEY", sql)
    sql = re.sub(r"FOREIGN KEY", "FOREIGN KEY REFERENCES", sql)

    # Write the converted SQL to a new file
    new_filename = filename.replace(".sql", "_converted.sql")
    with open(new_filename, "w") as f:
        f.write(sql)

def main():
    # Prompt the user to choose a SQL file
    filename = input("Enter the name of the SQL file: ")
    if not os.path.exists(filename):
        print("Error: File not found.")
        return

    # Convert the SQL file
    convert_sql_file(filename)
    print("SQL file converted successfully.")

if __name__ == "__main__":
    main()
