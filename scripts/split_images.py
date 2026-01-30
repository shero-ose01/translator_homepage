#!/usr/bin/env python3
"""
Script to split combined images into 2x2 grid sections
"""

from PIL import Image
import os
import sys

def split_image_2x2(img_path, output_dir, base_name):
    """Split an image into 2x2 grid (4 quadrants)"""
    try:
        with Image.open(img_path) as img:
            width, height = img.size
            
            # Handle irregular dimensions (IMG_2)
            if base_name == 'IMG_2':
                # For IMG_2 (1127x750), center crop to even dimensions first
                target_width = (width // 2) * 2
                target_height = (height // 2) * 2
                
                left = (width - target_width) // 2
                top = (height - target_height) // 2
                right = left + target_width
                bottom = top + target_height
                
                img = img.crop((left, top, right, bottom))
                width, height = img.size
            
            # Calculate quadrant dimensions
            half_width = width // 2
            half_height = height // 2
            
            # Define crop boxes for each quadrant
            # Top-left, Top-right, Bottom-left, Bottom-right
            crop_boxes = [
                (0, 0, half_width, half_height),           # Part 1 (top-left)
                (half_width, 0, width, half_height),       # Part 2 (top-right)
                (0, half_height, half_width, height),       # Part 3 (bottom-left)
                (half_width, half_height, width, height)   # Part 4 (bottom-right)
            ]
            
            # Split and save each quadrant
            for i, (left, top, right, bottom) in enumerate(crop_boxes, 1):
                quadrant = img.crop((left, top, right, bottom))
                output_path = os.path.join(output_dir, f"{base_name}_part{i}.jpg")
                quadrant.save(output_path, 'JPEG', quality=95)
                print(f"Created: {output_path} ({quadrant.size[0]}x{quadrant.size[1]})")
                
    except Exception as e:
        print(f"Error splitting {img_path}: {e}")
        return False
    
    return True

def main():
    """Main function to process all images"""
    images_dir = "/home/shero/Projects/Translator_Homepage/public/images"
    
    # List of images to split
    images_to_split = ['IMG_1.jpg', 'IMG_2.jpg', 'IMG_3.jpg']
    
    print("Starting image splitting process...")
    
    for img_name in images_to_split:
        img_path = os.path.join(images_dir, img_name)
        
        if not os.path.exists(img_path):
            print(f"Warning: {img_path} not found, skipping...")
            continue
            
        print(f"\nProcessing {img_name}...")
        base_name = img_name.replace('.jpg', '')
        
        success = split_image_2x2(img_path, images_dir, base_name)
        
        if success:
            print(f"Successfully split {img_name} into 4 parts")
        else:
            print(f"Failed to split {img_name}")
    
    print("\nImage splitting completed!")

if __name__ == "__main__":
    main()