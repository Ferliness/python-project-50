#!/usr/bin/env python

import argparse

def main():
    parser = argparse.ArgumentParser(
                    description='Compares two configuration files and shows a difference.',
                    epilog='Made by Ferliness.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    args = parser.parse_args()
    
    print('Hello, World!')


if __name__ == '__main__':
    main()