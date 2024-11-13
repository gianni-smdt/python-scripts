#Import necessary libraries
import os
from PIL import Image
import pyheif 

#Method to convert the HEIC file tp JPG
def heic_to_jpeg(input_folder, output_folder):
    
    for filename in os.listdir(input_folder):
        if filename.lower().endswith('.heic'):
            heic_path = os.path.join(input_folder, filename)
            jpeg_path = os.path.join(output_folder, f"{os.path.splitext(filename)[0]}.jpg")
            
            #Load and convert the HEIC file
            heif_file = pyheif.read(heic_path)
            image = Image.frombytes(
                heif_file.mode, 
                heif_file.size, 
                heif_file.data, 
                "raw", 
                heif_file.mode, 
                heif_file.stride
            )
            
            #Save as JPG
            image.save(jpeg_path, "JPEG")
            print(f"Konvertiert: {filename} -> {jpeg_path}")

#Call the method
input_folder = '<Source path of your HEIC files>'  
output_folder = '<Destination path for the converted files>'  
heic_to_jpeg(input_folder, output_folder)
