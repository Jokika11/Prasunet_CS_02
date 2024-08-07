# Image Encryption and Decryption using Python

## 📜 Project Description
This project demonstrates a simple technique to encrypt and decrypt images by swapping the red and blue channels of each pixel. The project uses Python and the PIL (Pillow) library for image processing.

## 📂 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)

## 📝 Introduction
Image encryption and decryption are crucial in various fields such as secure communications, digital watermarking, and more. This project provides a basic yet effective method for encrypting and decrypting images by swapping the red and blue color channels.

## ✨ Features
- **Simple Encryption/Decryption**: Uses red-blue channel swapping.
- **Easy to Use**: Command-line interface for straightforward usage.
- **Cross-Platform**: Works on any platform that supports Python and PIL.

## ⚙️ Installation
To get started with this project, clone the repository and install the necessary dependencies:

git clone https://github.com/Jokika11/Prasunet_CS_02.git

## 🚀 Usage
You can use the provided script to encrypt and decrypt images easily.

Encrypting an Image
```bash
python Pixel_Manupulation.py
```
Input the path of the image you want to encrypt.
The encrypted image will be saved as encrypted_image.jpg.

Decrypting an Image
The script automatically decrypts the encrypted image saved as encrypted_image.jpg:
The decrypted image will be saved as decrypted_image.jpg.

## 🛠️ Code Explanation
Here's a brief explanation of the main functions used in the script:

swap_red_blue(pixel)
Swaps the red and blue channels of a given pixel.

encrypt_image(input_path, output_path)
Encrypts the image by swapping the red and blue channels of each pixel and saves the encrypted image.

decrypt_image(input_path, output_path)
Decrypts the image by swapping the red and blue channels back to their original positions and saves the decrypted image.

