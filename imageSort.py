import os
import csv
import re

#Function to edit invalid directory names
def sanitize_directory_name(name):
    # Replace invalid characters with an underscore
    return re.sub(r'[<>:"/\\|?*]', '_', name)

#Function to edit invalid file names
def sanitize_file_name(name):
    # Replace invalid characters with an underscore and limit the length
    return re.sub(r'[<>:"/\\|?*]', '_', name)[:255]

#Create a directory for each Primary ID and save images
def create_directories_and_save_images(csv_file, base_directory):
    try:
        #Read the CSV file
        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            
            #Iterate through each row in the CSV file
            for row in reader:
                primary_id = row['Primary ID']
                
                #Editthe directory name
                sanitized_primary_id = sanitize_directory_name(primary_id)
                
                #Create a directory for the Primary ID inside the base directory if it doesn't exist
                primary_id_directory = os.path.join(base_directory, sanitized_primary_id)
                try:
                    os.makedirs(primary_id_directory, exist_ok=True)
                except OSError as e:
                    print(f"Error creating directory {primary_id_directory}: {e}")
                    continue
                
                #Iterate through each column in the row
                for column, value in row.items():
                    if 'Image' in column and value:
                        try:
                            # Sanitize the file name
                            sanitized_file_name = sanitize_file_name(f"{column}_{value}.txt")
                            # Save the image URL to a text file inside the directory
                            image_file_path = os.path.join(primary_id_directory, sanitized_file_name)
                            with open(image_file_path, 'w') as image_file:
                                image_file.write(value)
                        except Exception as e:
                            print(f"Error saving image URL for {primary_id} in column {column}: {e}")
    except FileNotFoundError:
        print(f"Error: The file {csv_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#specify the CSV file name and base directory
csv_file = 'Image Audit (4).csv'
base_directory = r'C:\Users\\ckennedy\\Documents\\scripts\\PrimaryDigitalImages'

#Create directories and save images
create_directories_and_save_images(csv_file, base_directory)

print("Directories created and images saved successfully.")
