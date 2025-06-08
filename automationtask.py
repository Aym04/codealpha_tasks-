# -*- coding: utf-8 -*-
"""
Created on Sun Jun  8 02:12:07 2025

@author: aymane
"""

# Task Automation: Rename files in a folder

import os

# Function to rename files by adding a prefix
def rename_files(folder_path, prefix):
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print(f"Error: The folder '{folder_path}' does not exist.")
        return

    # List all files in the folder
    files = os.listdir(folder_path)

    # Rename each file by adding the prefix
    for file_name in files:
        old_path = os.path.join(folder_path, file_name)
        # Skip directories, only rename files
        if os.path.isfile(old_path):
            new_name = prefix + file_name
            new_path = os.path.join(folder_path, new_name)
            try:
                os.rename(old_path, new_path)
                print(f"Renamed '{file_name}' to '{new_name}'")
            except Exception as e:
                print(f"Error renaming '{file_name}': {e}")

# Example usage
folder_path = input("Enter the path to the folder: ")
prefix = input("Enter the prefix to add to the files: ")
rename_files(folder_path, prefix)