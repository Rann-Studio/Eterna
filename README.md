# Eterna
Eterna is a simple tool for easy file encryption and decryption. With Eterna, you can secure your confidential files with just a few simple steps.


## Installation
To install Eterna, simply run the following command in your terminal:
```
git clone https://github.com/Rann-Studio/Eterna.git
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
