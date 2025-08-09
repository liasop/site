import os
import glob

# List of directories to process
directories = [
    '/Users/liachin-purcell/personal/site/images/8.5.25_images',
    '/Users/liachin-purcell/personal/site/images/8.6.25_images',
    '/Users/liachin-purcell/personal/site/images/8.7.25_images',
    '/Users/liachin-purcell/personal/site/images/8.8.25_images'
]

for directory in directories:
    print(f"\nProcessing directory: {os.path.basename(directory)}")
    
    # Get all image files in the directory (both .png and .jpeg)
    image_files = glob.glob(os.path.join(directory, '*.png'))
    image_files.extend(glob.glob(os.path.join(directory, '*.jpeg')))
    
    # Sort files to ensure consistent ordering
    image_files.sort()
    
    # Rename files
    for index, old_file in enumerate(image_files, start=1):
        # Get file extension from original file
        _, ext = os.path.splitext(old_file)
        
        # Create new filename
        new_name = f'@img{index}{ext}'
        new_file = os.path.join(directory, new_name)
        
        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed {os.path.basename(old_file)} to {new_name}')