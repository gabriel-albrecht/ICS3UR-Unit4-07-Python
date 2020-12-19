#!/usr/bin/env python3

# Created by: Mr. Coxall
# Created on: Nov 2019
# This program shows numbers between 1000-2000


def main():
    for thousand in range(1000, 2000 + 1):
        print(thousand, " ", end="")
        if thousand % 5 == 4:
            print("")
        thousand += 1


if __name__ == "__main__":
    main()
