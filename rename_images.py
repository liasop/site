import os
import glob

# Set the directory path
directory = '/Users/liachin-purcell/personal/site/images/8.4.25_images'

# Get all PNG files in the directory
png_files = glob.glob(os.path.join(directory, '*.png'))

# Sort files to ensure consistent ordering
png_files.sort()

# Rename files
for index, old_file in enumerate(png_files, start=1):
    # Create new filename
    new_name = f'@img{index}.png'
    new_file = os.path.join(directory, new_name)
    
    # Rename the file
    os.rename(old_file, new_file)
    print(f'Renamed {os.path.basename(old_file)} to {new_name}')