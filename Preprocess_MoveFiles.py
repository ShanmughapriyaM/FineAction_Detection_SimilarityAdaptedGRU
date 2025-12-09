# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 21:30:52 2025

@author: Shanm
"""

import os
import shutil

# CHANGE THIS to your root folder path
ROOT_FOLDER = r"C:\Users\Shanm\Documents\SCI Paper 2\Breakfast_DataSet"

# Destination folder
DEST_FOLDER = os.path.join(r'C:\Users\Shanm\Documents\SCI Paper 2\BreakFastExtracted Frames', "friedegg")

# Create destination folder if it doesn't exist
os.makedirs(DEST_FOLDER, exist_ok=True)

# Walk through all subfolders
for root, dirs, files in os.walk(ROOT_FOLDER):
    for file in files:
        # Check if filename contains "coffee" (case-insensitive)
        if "friedegg" in file.lower():
            source_path = os.path.join(root, file)
            dest_path = os.path.join(DEST_FOLDER, file)

            # Avoid moving files already inside destination
            if not os.path.abspath(source_path).startswith(os.path.abspath(DEST_FOLDER)):
                print(f"Moving: {source_path} -> {dest_path}")
                shutil.move(source_path, dest_path)

print("✅ All matching files moved to 'coffee' folder.")
