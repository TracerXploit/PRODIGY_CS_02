# Image Encryption/Decryption Tool

![Project Icon](icon.png)

This project is part of my internship at Prodigy InfoTech. It implements an image encryption and decryption tool using a basic XOR cipher algorithm in Python.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Example](#example)
5. [How it Works](#how-it-works)
6. [Output Examples](#output-examples)
    - [Encrypting an Image](#encrypting-an-image)
    - [Decrypting an Image](#decrypting-an-image)
7. [Contributing](#contributing)
8. [License](#license)

## Features

- Encrypt an image using a basic XOR cipher algorithm
- Decrypt an image using the same XOR cipher algorithm
- User can specify the encryption/decryption key

## Installation

To use this tool, you need to have Python and the Pillow library installed. You can install Pillow using pip:

```bash
pip install pillow
```
## Usage

1. Clone the repository:

```bash
git clone https://github.com/mihirsathvar56/image-encryption-tool.git
cd image-encryption-tool
```
2. Run the Python script `image_encryption.py`:

```bash
python image_encryption.py
```
3. Follow the on-screen instructions to either encrypt or decrypt an image.

## Example

```bash
$ python image_encryption.py
Welcome to the Image Encryption/Decryption Tool!
Created by MIHIR SATHVARA!
Would you like to encrypt or decrypt the image? (enter 'encrypt' or 'decrypt', or 'exit' to quit): encrypt
Enter the path of the image: path/to/image.jpg
Enter the path for the encrypted image: path/to/encrypted_image.png
Enter the encryption/decryption key (an integer): 123
Image encrypted and saved as path/to/encrypted_image.png
```
## How it Works

The image encryption tool uses a basic XOR cipher algorithm to encrypt and decrypt images. The XOR cipher works by performing a bitwise XOR operation between the image data and the specified key. The same key is used for both encryption and decryption.

## Output Examples

### Encrypting an Image

1. Original Image
   This is the original image before any encryption is applied.
   ![Original Image](image.png)
```bash
Do you want to (e)ncrypt or (d)ecrypt an image? Enter 'q' to quit: e
Enter the path of the image: path/to/image.jpg
Enter the path for the encrypted image: path/to/encrypted_image.png
Enter the encryption/decryption key (an integer): 123
Image encrypted and saved as path/to/encrypted_image.png
```

2. Encrypted Image
   This is the image after it has been encrypted using the XOR cipher algorithm with the specified key.
   ![Encrypted Image](encrypted_img.png)
   
### Decrypting an Image

1. Encrypted Image
   This is the encrypted image that will be decrypted using the same key that was used for encryption.
    ![Encrypted Image](encrypted_img.png)
```bash

Do you want to (e)ncrypt or (d)ecrypt an image? Enter 'q' to quit: d
Enter the path of the image: path/to/encrypted_image.jpg
Enter the path for the decrypted image: path/to/decrypted_image.png
Enter the encryption/decryption key (an integer): 123
Image decrypted and saved as path/to/decrypted_image.png

```

2. Decrypted Image
   This is the image after it has been decrypted, restoring it to its original form.
   ![Decrypted Image](decrypted_img.png)
   
## Contributing

If you have suggestions for improvements or find any bugs, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.
