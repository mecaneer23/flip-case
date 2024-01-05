#!/usr/bin/env python3
# pylint: disable=missing-docstring


def parse(string: str) -> str:
    output_str = ""
    for char in string:
        representation = ord(char)
        if ord("a") <= representation <= ord("z"):
            output_str += chr(representation + (ord("A") - ord("a")))
        elif ord("A") <= representation <= ord("Z"):
            output_str += chr(representation - (ord("A") - ord("a")))
        else:
            output_str += char
    return output_str


def main():
    string = input("Enter a string: ")
    print(parse(string))
    print(string.swapcase())


if __name__ == "__main__":
    main()
