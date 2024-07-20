from PIL import Image
import numpy as np
import os

def load_image(image_path):
    """
    Load an image from the specified path.

    Args:
        image_path (str): Path to the image file.

    Returns:
        Image: Loaded image object or None if loading fails.
    """
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        print(f"Error: The file at {image_path} was not found.")
        return None
    except Exception as e:
        print(f"Error loading image: {e}")
        return None

def save_image(image, save_path):
    """
    Save an image to the specified path.

    Args:
        image (Image): Image object to save.
        save_path (str): Path to save the image file.
    """
    try:
        image.save(save_path)
    except Exception as e:
        print(f"Error saving image: {e}")

def generate_key(image):
    """
    Generate a random key for image encryption.

    Args:
        image (Image): Image object to base the key dimensions on.

    Returns:
        np.ndarray: Generated key.
    """
    height, width = image.size
    key = np.random.randint(0, 256, size=(width, height, 3), dtype=np.uint8)
    return key

def encrypt_image(image, key):
    """
    Encrypt an image using XOR operation with the given key.

    Args:
        image (Image): Image object to encrypt.
        key (np.ndarray): Key for encryption.

    Returns:
        Image: Encrypted image.
    """
    image_array = np.array(image)
    encrypted_array = np.bitwise_xor(image_array, key)
    encrypted_image = Image.fromarray(encrypted_array.astype('uint8'))
    return encrypted_image

def decrypt_image(encrypted_image, key):
    """
    Decrypt an encrypted image using XOR operation with the given key.

    Args:
        encrypted_image (Image): Encrypted image object to decrypt.
        key (np.ndarray): Key used for encryption.

    Returns:
        Image: Decrypted image.
    """
    encrypted_array = np.array(encrypted_image)
    decrypted_array = np.bitwise_xor(encrypted_array, key)
    decrypted_image = Image.fromarray(decrypted_array.astype('uint8'))
    return decrypted_image

def main():
    # Paths to images (using raw string literals)
    image_path = r"Test Case Images\Test_Image-1.jpg"
    encrypted_image_path = r"Encrypted Images\B-XOR_Manipulated_Image-1.jpg"
    decrypted_image_path = r"Decrypted Images\Decrypted_image-1.jpg"

    # Load the original image
    image = load_image(image_path)
    if image is not None:
        # Generate a key
        key = generate_key(image)

        # Encrypt the image
        print("Encrypting...")
        encrypted_image = encrypt_image(image, key)

        # Save the encrypted image
        save_image(encrypted_image, encrypted_image_path)

        # Decrypt the encrypted image
        print("Decrypting...")
        decrypted_image = decrypt_image(encrypted_image, key)

        # Save the decrypted image
        save_image(decrypted_image, decrypted_image_path)

        print("Image encryption and decryption completed!")
    else:
        print("Image loading failed, exiting program.")

if __name__ == "__main__":
    main()
