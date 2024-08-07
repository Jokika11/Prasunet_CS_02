from PIL import Image

def swap_red_blue(pixel):
    r, g, b = pixel
    return (b, g, r)  # Swap red and blue channels

def encrypt_image(input_path, output_path):
    original_image = Image.open(input_path)
    encrypted_pixels = [swap_red_blue(pixel) for pixel in original_image.getdata()]
    encrypted_image = Image.new(original_image.mode, original_image.size)
    encrypted_image.putdata(encrypted_pixels)
    encrypted_image.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

def decrypt_image(input_path, output_path):
    encrypted_image = Image.open(input_path)
    decrypted_pixels = [swap_red_blue(pixel) for pixel in encrypted_image.getdata()]
    decrypted_image = Image.new(encrypted_image.mode, encrypted_image.size)
    decrypted_image.putdata(decrypted_pixels)
    decrypted_image.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

def main():
    original=input("input_image_path:")  # Provide your input image path
    encrypted_image_path = "encrypted_image.jpg"
    decrypted_image_path = "decrypted_image.jpg"

    encrypt_image(original, encrypted_image_path)
    decrypt_image(encrypted_image_path, decrypted_image_path)

if __name__ == "__main__":
    main()
