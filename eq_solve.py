#!/usr/bin/python3
import sys
import argparse 
import custom_exceptions

def arg_parse_foo():
    linear_parse=argparse.ArgumentParser(description="this script takes a file\
            as an argument from command line in which in ideal shold be an\
            linear equality and creates another file containing the solutionn\
            of the given equality and as a feedback compares the got solution\
            with right solution")
    linear_parse.add_argument('-f', "--file", required = True)
    arguments = linear_parse.parse_args()
    return arguments.file

def get_abc(ab_str):
    ab = ab_str.split()
    try:
        for each in ab:
            try:
                float(each)
            except ValueError:
                print(f"\"{each}\" from input file is not convertable to float")
                sys.exit()
        if 2 < len(ab):
            raise ExtraParametersError
        elif 2 > len(ab):
            raise TooFewParametersError
    except NoNumericParameterError:
            print("no numeric symbols in input file\n")
            sys.exit()
    except ExtraParametersError:
            print("extra parameters got from input file\n")
            sys.exit()
    except TooFewParametersError:
            print("too few parameters got from input file\n")
            sys.exit()
    return float(ab[0]), float(ab[1])

def read_from_file():
    try:
        with open(arg_parse_foo()) as my_file:
            abc_str = my_file.read()
        return abc_str
    except :
        print("File not exist")
        sys.exit()

def test(arg_num):
    try:
        with open("golden.txt") as golden_num_f:
            golden_num_str = golden_num_f.read()
        if arg_num == float(golden_num_str):
            print(f"{arg_num} solution is right!\n")
        else:
            print(f"solution is wroong!!!  should be {golden_num_str} \n")
    except IOError:
        print("Golden file not exist")
        sys.exit()

def solve(ab):
    try:
        if 0 == ab[0]:
            if 0 != ab[1]:
                raise ZeroDivisionError
            else:
                print("the got parameters suit for identity\n")
                print("interrupt the execution. No output file will be generated\n")
                sys.exit()
        return -(ab[1]/ab[0])
    except TypeError:
        print ("File input is not correct")
        sys.exit()
    except ZeroDivisionError:
        print("\"a\" is zero while while b is not zero\n")
        sys.exit()

def generate_output_file(arg_num):
    with open('output.txt', 'w') as output_f:
        output_f.write(str(arg_num) + '\n')

def main() -> None:
    ab_str = read_from_file()
    ab = get_abc(ab_str)
    x = solve(ab)
    test(x)
    generate_output_file(x)

if __name__ == '__main__':
    main()
