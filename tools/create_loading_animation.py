import os
from apng import APNG
from pathlib import Path

def create_loading_animation(input_dir, output_file, frame_duration=50):
    """
    Combine PNG images from a directory into an animated PNG.
    
    Args:
        input_dir (str): Directory containing the PNG images
        output_file (str): Path to save the output APNG
        frame_duration (int): Duration of each frame in milliseconds
    """
    # Get all PNG files and sort them
    png_files = sorted([f for f in os.listdir(input_dir) if f.endswith('.png')])
    
    if not png_files:
        raise ValueError(f"No PNG files found in {input_dir}")
    
    # Create APNG object
    apng = APNG()
    
    # Add each frame to the animation
    for png_file in png_files:
        frame_path = os.path.join(input_dir, png_file)
        apng.append_file(frame_path, delay=frame_duration)
    
    # Save the animation
    apng.save(output_file)
    print(f"Created animated PNG at: {output_file}")

if __name__ == "__main__":
    # Input directory containing the PNG files
    input_dir = r"C:\Users\Lindsay\source\repos\MultiworldGG\data\gui\data\loading"
    
    # Output file path
    output_file = os.path.join(input_dir, "loading_animation.png")
    
    # Create the animation
    create_loading_animation(input_dir, output_file) 