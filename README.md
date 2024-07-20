# PRODIGY_CS_02
## Pixel Manipulation for Image Encryption

Aim: This project demonstrates image encryption and decryption using XOR operations. The script loads an image, generates a random key, encrypts the image using the key, and then decrypts it to retrieve the original image.

### Features
- Load an image from a specified path
- Generate a radnom key for encryption
- Encyrpt the image using the generated key
- Save the encyrpted image to a specified path
- Decrypt the encrypted image using the same key
- Save the decrypted image to a specified path


### Prerequisities
- `Pillow` Library
- `numpy` Libarary

You can install the required libraries using the following command:
```bash
pip install pillow numpy
```

### Usage
1. Clone the repo:
```bash
https://github.com/AnaghaU18/PRODIGY_CS_02.git
```
3. Update the paths in the script if necessary:
```bash
# Paths to images (using raw string literals)
image_path = r"Test Case Images\Sample_Image-2.jpg"
encrypted_image_path = r"Encrypted Images\B-XOR_Manipulated_Image.jpg"
decrypted_image_path = r"Decrypted Images\Decrypted_image.jpg"
```
3. Run the script:
```bash
python main.py
```

### Script Overview
**Functions:**
- `load_image(image_path)`: Loads an image from the specified path
- `save_image(image, save_path)`: Saves an image to a specified path
- `generate_key(image)`: Generates a random key for image encryption based on the image dimensions
- `encrypt_image(image, key)`: Encrypts an image using XOR operation with the given key
- `decrypt_image(encrypted_image, key)` Decrypts an encrypted image using XOR operation with the given key

### Main Process
1. Load the original image
2. Generate a random key based on the image dimensions
3. Encrypt the image using the generated key
4. Save the encrypted image to a specified path
5. Decrypt the encrypted image using the same key
6. Save the decrypted image to the specified path

## Acknowledgments
- *Pillow* - The friendly PIL fork
- *NumPy* - The fundamental package for scientific computing with Python
