#!/usr/bin/env python

numbers = list()

def process(action, number):
    if action == "append":
        return append(number)
    
    if action == "remove":
        return remove(number)

    return "action not supported"
def append(number):
    numbers.append(number)
    numbers.sort()

    return median()

def remove(number):
    try:
        numbers.remove(number)
    except ValueError:
        pass

    return median()
    
def median():
    n = len(numbers)

    if n < 1:
        return "empty list"

    if n == 1:
        return numbers[0]

    if (n % 2 == 1):
        return numbers[n / 2]
    
    return float((numbers[(n / 2) - 1] + numbers[(n / 2)])) / 2

def main():
    while True:
        txt = raw_input("> ")
        if txt == "exit":
            return

        arr = txt.split(" ")
        
        try:
            num = int(arr[1])
        except ValueError:
            print "please input number after action"
            continue

        out = process(arr[0], num)
        print numbers
        print out

if __name__ == '__main__':
    main()
