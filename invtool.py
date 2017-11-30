#!/usr/bin/env python3

import os

os.system('cls')

def print_menu():
    print("MAIN MENU\n")
    print("1. IP Address")
    print("2. File Hash")
    print("3. Port Number")

def validate_choice(choice):
    if choice == '1':
        print("ONE")
    elif choice == '2':
        print("TWO")
    elif choice == '3':
        print("THREE")
    else:
        print("Please enter a number between 1 - 3")


print_menu()
choice = input("\nEnter Selection: ")
validate_choice(choice)
