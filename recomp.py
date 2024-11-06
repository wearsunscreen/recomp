import os
import argparse
from PIL import Image

def compress_images(file_list_path, compression_level):
    with open(file_list_path, 'r') as file:
        jpg_files = file.readlines()
    
    for jpg_file in jpg_files:
        jpg_file = jpg_file.strip()
        if os.path.isfile(jpg_file) and jpg_file.lower().endswith('.jpg'):
            before_size = os.path.getsize(jpg_file)
            img = Image.open(jpg_file)
            img.save(jpg_file, 'JPEG', quality=compression_level)
            after_size = os.path.getsize(jpg_file)
            print(f"Compressed and saved: {jpg_file} with compression level {compression_level}")
            print(f"Size before: {before_size} bytes, Size after: {after_size} bytes")
        else:
            print(f"File not found or not a JPG: {jpg_file}")

def main(args):
    compress_images(args.file_list_path, args.c)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Compress JPG images to a specified quality level.')
    parser.add_argument('file_list_path', type=str, help='Path to the text file containing list of JPG files')
    parser.add_argument('--c', type=int, default=80, help='Compression level for JPG images (default: 80)')
    args = parser.parse_args()
    
    main(args)