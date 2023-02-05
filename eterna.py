import os
import sys
import struct
import argparse
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_file(in_filename, out_filename=None, key_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0] + '.enc'

    if not key_filename:
        key_filename = os.path.splitext(in_filename)[0] + '.key'

    key = get_random_bytes(16)
    iv = get_random_bytes(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            with open(key_filename, 'wb') as keyfile:
                keyfile.write(key)
                outfile.write(struct.pack('<Q', os.path.getsize(in_filename)))
                outfile.write(iv)

                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)

                    outfile.write(encryptor.encrypt(chunk))
    print("File encrypted successfully.")


def decrypt_file(in_filename, out_filename=None, key_filename=None, chunksize=64*1024):
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0] + '.dec'

    if not key_filename:
        key_filename = os.path.splitext(in_filename)[0] + '.key'

    with open(key_filename, 'rb') as keyfile:
        key = keyfile.read()

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(AES.block_size)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    print("File decrypted successfully.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Encrypt or Decrypt a file', epilog=f"Example: python {sys.argv[0]} -e example.txt")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-e', '--encrypt', action='store_true', help='Encrypt the input file')
    group.add_argument('-d', '--decrypt', action='store_true', help='Decrypt the input file')

    parser.add_argument('-i', '--input', required=True, help='Input file name')
    parser.add_argument('-o', '--output', help='Output file name')
    parser.add_argument('-k', '--key', help='Key file name')

    args = parser.parse_args()

    input_file = args.input
    output_file = args.output
    key_file = args.key

    if args.encrypt:
        encrypt_file(input_file, output_file, key_file)
    elif args.decrypt:
        decrypt_file(input_file, output_file, key_file)
