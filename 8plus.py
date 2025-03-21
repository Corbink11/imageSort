import os
import shutil
import sys

def move_folders_with_many_files(source_dir, destination_dir, min_file_count=8):
    """
    Checks all folders in source_dir and moves those containing min_file_count or more files
    to destination_dir.
    
    Args:
        source_dir (str): Path to source directory to check
        destination_dir (str): Path to destination directory where folders will be moved
        min_file_count (int): Minimum number of files required to move a folder (default: 8)
    """
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Create destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        try:
            os.makedirs(destination_dir)
            print(f"Created destination directory: {destination_dir}")
        except OSError as e:
            print(f"Error creating destination directory: {e}")
            return
    
    # Track statistics
    moved_folders = 0
    
    # Iterate through items in the source directory
    for item in os.listdir(source_dir):
        item_path = os.path.join(source_dir, item)
        
        # Check if the item is a directory
        if os.path.isdir(item_path):
            # Count files in the directory (non-recursive)
            file_count = sum(1 for entry in os.listdir(item_path) 
                            if os.path.isfile(os.path.join(item_path, entry)))
            
            # If folder contains min_file_count or more files, move it
            if file_count >= min_file_count:
                destination_path = os.path.join(destination_dir, item)
                
                # Check if there's already a folder with the same name in the destination
                if os.path.exists(destination_path):
                    print(f"Warning: Folder '{item}' already exists in the destination. Skipping.")
                    continue
                
                try:
                    shutil.move(item_path, destination_path)
                    moved_folders += 1
                    print(f"Moved: '{item}' ({file_count} files) to {destination_dir}")
                except Exception as e:
                    print(f"Error moving folder '{item}': {e}")
    
    print(f"\nOperation complete. Moved {moved_folders} folders with {min_file_count}+ files.")

if __name__ == "__main__":
    # Check command line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <source_directory> <destination_directory> [min_file_count]")
        sys.exit(1)
    
    source_dir = sys.argv[1]
    destination_dir = sys.argv[2]
    
    # Optional third argument for minimum file count
    min_file_count = 8
    if len(sys.argv) > 3:
        try:
            min_file_count = int(sys.argv[3])
        except ValueError:
            print(f"Error: min_file_count must be an integer. Using default value of {min_file_count}.")
    
    move_folders_with_many_files(source_dir, destination_dir, min_file_count)