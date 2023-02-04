# Eterna
Eterna is a simple tool for easy file encryption and decryption. With Eterna, you can secure your confidential files with just a few simple steps.


## Installation
To install Eterna, follow these simple steps:
1. Clone the repository to your local machine by running the following command in your terminal:

    ```
    git clone https://github.com/Rann-Studio/Eterna.git
    ```

2. Once the repository has been cloned, navigate to the repository directory and run the following command to install the required packages:

    ```
    pip install -r requirements.txt
    ```


## Usage
To use Eterna, run the following command in your terminal:
```
python eterna.py [-h] (-e | -d) -i INPUT [-o OUTPUT] [-k KEY]
```

The available options for Eterna are:
```
-h, --help                  Show this help message and exit
-e, --encrypt               Encrypt the input file
-d, --decrypt               Decrypt the input file
-i INPUT, --input INPUT     Input file path
-o OUTPUT, --output OUTPUT  Output file path
-k KEY, --key KEY           Key file path
```


## Example
To encrypt a file, run the following command:
```
python eterna.py -e -i example.txt
```

To decrypt a file, run the following command:
```
python eterna.py -d -i example.enc
```

## Running Eterna with Python
Eterna can be run from within Python by using the encrypt_file and decrypt_file functions. These functions provide a convenient way to encrypt and decrypt files from within your Python scripts.

Here's an example of how you can use these functions to encrypt and decrypt files:
```python
from eterna import encrypt_file, decrypt_file

encrypt_file(in_filename='example.txt')
decrypt_file(in_filename='example.enc')
```

The encrypt_file and decrypt_file functions have the following parameters:

`in_filename` : The input file to be encrypted or decrypted.\
`out_filename` (optional): The output file to save the encrypted or decrypted data.\
`key_filename` (optional): The key file to use for encryption or decryption. If not specified, a random key will be generated.\


## NOTE
It is important to keep the key used for encryption and decryption secure, as anyone who has access to the key will be able to decrypt your encrypted files.
