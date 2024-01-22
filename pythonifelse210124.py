Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.

Sample Input 0

3
Sample Output 0

Weird
Explanation 0


 is odd and odd numbers are weird, so print Weird.

Sample Input 1

24
Sample Output 1

Not Weird
 


import math

import os

import random

import re

import sys

if __name__ == '__main__':

    n = int(input().strip())

    if n%2==1:

        print("Weird")

    elif n%2==0:

        if n>1 and n<6:

            print("Not Weird")

        elif n>7 and n<21:

            print("Weird")

        elif n>20:

            print("Not Weird")


Input (stdin)

3
Your Output (stdout)

Weird
Expected Output

Weird