#!/bin/bash

# Function to rename files in a directory
rename_files() {
    local dir=$1
    local counter=1
    
    # Loop through all jpeg files in the directory
    for file in "$dir"/*.jpeg; do
        if [ -f "$file" ]; then
            # Create new filename
            new_name="$dir/@img$counter.jpeg"
            
            # Rename the file
            mv "$file" "$new_name"
            echo "Renamed $(basename "$file") to @img$counter.jpeg"
            
            # Increment counter
            ((counter++))
        fi
    done
}

# Rename files in 8.18.25_images
echo "Processing 8.18.25_images..."
rename_files "/Users/liachin-purcell/personal/site/images/8.18.25_images"

# Rename files in 8.19.25_images
echo "Processing 8.19.25_images..."
rename_files "/Users/liachin-purcell/personal/site/images/8.19.25_images"

echo "Renaming complete!"
