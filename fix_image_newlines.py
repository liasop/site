#!/usr/bin/env python3
"""
Script to add newlines before and after images in Markdown files.
Targets index.md files in the blog directory and ensures images are on their own lines.
"""

import os
import re
import glob
from pathlib import Path

def process_markdown_file(file_path):
    """
    Process a single Markdown file to ensure images have newlines before and after them.
    
    Args:
        file_path (str): Path to the Markdown file
        
    Returns:
        bool: True if file was modified, False otherwise
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines.copy()
        modified = False
        
        # Process each line to ensure images are on their own lines
        for i, line in enumerate(lines):
            # Pattern to match Markdown images: ![alt text](path)
            image_pattern = r'!\[([^\]]*)\]\(([^)]+)\)'
            
            # Find all images in the current line
            images = list(re.finditer(image_pattern, line))
            
            if images:
                # Split the line by images and rebuild it
                new_line_parts = []
                last_end = 0
                
                for match in images:
                    start, end = match.span()
                    image_text = match.group(0)
                    
                    # Add text before the image
                    before_text = line[last_end:start]
                    if before_text.strip():  # Only add if there's non-whitespace content
                        new_line_parts.append(before_text.rstrip())
                    
                    # Add the image on its own line
                    new_line_parts.append(image_text)
                    
                    last_end = end
                
                # Add any remaining text after the last image
                after_text = line[last_end:]
                if after_text.strip():  # Only add if there's non-whitespace content
                    new_line_parts.append(after_text.rstrip())
                
                # Rebuild the line with proper spacing
                if new_line_parts:
                    # Join parts with newlines, but avoid double newlines
                    new_line = '\n'.join(new_line_parts)
                    if not new_line.endswith('\n'):
                        new_line += '\n'
                    
                    lines[i] = new_line
                    modified = True
        
        # Only write if content changed
        if modified:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.writelines(lines)
            return True
        
        return False
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    """
    Main function to process all index.md files in the blog directory.
    """
    # Get the script directory (where the script is located)
    script_dir = Path(__file__).parent
    blog_dir = script_dir / "content" / "blog"
    
    if not blog_dir.exists():
        print(f"Blog directory not found: {blog_dir}")
        return
    
    # Find all index.md files in the blog directory
    pattern = str(blog_dir / "**" / "index.md")
    markdown_files = glob.glob(pattern, recursive=True)
    
    if not markdown_files:
        print("No index.md files found in the blog directory")
        return
    
    print(f"Found {len(markdown_files)} index.md files to process")
    
    modified_count = 0
    
    for file_path in markdown_files:
        print(f"Processing: {file_path}")
        if process_markdown_file(file_path):
            modified_count += 1
            print(f"  ✓ Modified")
        else:
            print(f"  - No changes needed")
    
    print(f"\nProcessing complete!")
    print(f"Modified {modified_count} out of {len(markdown_files)} files")

if __name__ == "__main__":
    main()
