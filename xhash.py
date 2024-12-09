#!/usr/bin/env python3

import argparse
import hashlib

def hash_string(input_string, algorithm):
    """Hashes a string with the specified algorithm"""
    try:
        hash_obj = hashlib.new(algorithm)
        hash_obj.update(input_string.encode('utf-8'))
        return {
            'hexdigest': hash_obj.hexdigest(),
            'digest': hash_obj.digest(),
            'digest_size': hash_obj.digest_size,
            'block_size': hash_obj.block_size
        }
    except ValueError as e:
        return {'error': str(e)}

def hash_file(file_path, algorithm):
    """Generates the hash of a file with the specified algorithm"""
    try:
        hash_obj = hashlib.new(algorithm)
        with open(file_path, 'rb') as f:
            # Reads the file in blocks to avoid loading large files into memory
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return {
            'hexdigest': hash_obj.hexdigest(),
            'digest': hash_obj.digest(),
            'digest_size': hash_obj.digest_size,
            'block_size': hash_obj.block_size
        }
    except (ValueError, FileNotFoundError, IsADirectoryError, PermissionError) as e:
        return {'error': str(e)}

def main():
    # Definition of the parser
    parser = argparse.ArgumentParser(
        description="Generate the hash of a string or file using a specified algorithm.",
        epilog="Example of use:\n"
               "  $ python %(prog)s -t s -a sha224 -v Hello!\n"
               "  $ python %(prog)s -t s -a sha224 -v \"Hello World!\"\n"
               "  $ python %(prog)s -t f -a sha224 -v path/to/file.txt\n"
               "  $ python %(prog)s -t f -a sha224 -v /home/user/Documents/path/to/file.txt",
        formatter_class=argparse.RawTextHelpFormatter
    )
    # Definition of arguments
    parser.add_argument(
        '-t', '--type',
        choices=['s', 'f'],
        required=True,
        metavar='TYPE',
        help="input type: 's' for string, 'f' for file"
    )
    parser.add_argument(
        '-a', '--algorithm',
        default='sha256',
        choices=[algo for algo in hashlib.algorithms_available if algo.islower()],
        metavar='ALGORITHM',
        help="hashing algorithm (default: sha256)\n"
             "supported:\n"
             " - md5, md5-sha1, sha1\n"
             " - sha224, sha256, sha384, sha512, sha512_224, sha512_256\n"
             " - sha3_224, sha3_256, sha3_384, sha3_512\n"
             " - shake_128, shake_256\n"
             " - blake2s, blake2b\n"
             " - ripemd160, sm3"
    )
    parser.add_argument(
        '-v', '--value',
        required=True,
        metavar='VALUE',
        help="string or path of the file to hash"
    )
    args = parser.parse_args()

    if args.type == 's':
        result = hash_string(args.value, args.algorithm)
    else:
        result = hash_file(args.value, args.algorithm)

    if 'error' in result:
        print(f"Error: {result['error']}")
    else:
        print(f"Hash ({args.algorithm}): {result['hexdigest']}")
        print(f"Byte sequence: {result['digest']}")
        print(f"[Digest size: {result['digest_size']} | Block size: {result['block_size']}]")

if __name__ == "__main__":
    main()

