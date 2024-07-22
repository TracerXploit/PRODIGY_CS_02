from PIL import Image
import numpy as np

def encrypt_image(image_path, output_path, key):
    
    """
    Encrypts an image using a basic XOR cipher.

    Args:
    - image_path (str): Path to the input image file.
    - key (int): Encryption key.

    Saves the encrypted image as the specified output path.
    
    """
    try:
        # Open the image using PIL
        image = Image.open(image_path).convert('RGB')
        
        # Convert the image to a NumPy array for easier manipulation
        img_array = np.array(image)
        
        # Perform XOR encryption on the image array
        encrypted_array = (img_array ^ key) % 256  # XOR encryption with wrapping
        
        # Convert the encrypted NumPy array back to an image
        encrypted_image = Image.fromarray(np.uint8(encrypted_array))
        encrypted_image.save(output_path)
        
        # Print success message
        print(f"Image encrypted and saved as {output_path}")
        
    except Exception as e:
        print(f"Error: {e}")

def decrypt_image(image_path, output_path, key):
    """
    Decrypts an encrypted image using a basic XOR cipher.

    Args:
    - image_path (str): Path to the encrypted image file.
    - key (int): Encryption key.

    Saves the decrypted image as the specified output path.
    """
    try:
        # Open the encrypted image using PIL
        encrypted_image = Image.open(image_path).convert('RGB')
        
        # Convert the encrypted image to a NumPy array
        encrypted_array = np.array(encrypted_image)
        
        # Perform XOR decryption on the encrypted image array
        decrypted_array = (encrypted_array ^ key) % 256  # XOR decryption with wrapping
        
        # Convert the decrypted NumPy array back to an image
        decrypted_image = Image.fromarray(np.uint8(decrypted_array))
        decrypted_image.save(output_path)
        
        # Print success message
        print(f"Image decrypted and saved as {output_path}")
    
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Welcome to the Image Encryption/Decryption Tool!")
    print("Created by MIHIR SATHVARA!")
    
    while True:
        try:
            # Take inputs from the user
            action = input("Would you like to encrypt or decrypt the image? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").strip().lower()
            if action == 'exit':
                print("Exiting the Image Encryption/Decryption Tool. Goodbye!")
                break
            
            image_path = input("Enter the path of the image: ").strip()
            output_path = input(f"Enter the path for the {'encrypted' if action == 'encrypt' else 'decrypted'} image: ").strip()
            key = int(input("Enter the encryption/decryption key (an integer): ").strip())
            
            if action == 'encrypt':
                encrypt_image(image_path, output_path, key)
            elif action == 'decrypt':
                decrypt_image(image_path, output_path, key)
            else:
                print("Invalid action. Please enter 'encrypt', 'decrypt', or 'exit'.")
        except ValueError:
            print("Invalid key. Please enter an integer value.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
