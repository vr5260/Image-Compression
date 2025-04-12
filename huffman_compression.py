from PIL import Image

def huffman_compression(input_path, output_path):
    # This is a simplified placeholder for the real Huffman logic
    img = Image.open(input_path)

    # Save image with reduced quality (as a mock "compression")
    img.save(output_path, format='JPEG', quality=20)

    print("Image compressed and saved at:", output_path)
