from argparse import Namespace
from my_tests import *
import argparse
import os.path
import time
import numpy

parser = argparse.ArgumentParser(description='Greedy knapssack resolution via files.')
group = parser.add_mutually_exclusive_group()
group.add_argument('-f', '--file', nargs='+', action='store', dest='input_data',
                   help='specify an input file of parametres.')
group.add_argument('-d', '--directory', nargs='+', action='store', dest='input_data_d',
                   help='specify a path with files of parametres.')
parser.add_argument('-r', '--result', action='store_true', dest='o_result', help='Print result')
parser.add_argument('-t', '--time', action='store_true', dest='time', help='Display time')
parser.add_argument('-dc', action='store_true', dest='display', help='Display created matrix')

algorithm = parser.add_mutually_exclusive_group(required=True)
algorithm.add_argument("-sc", '-check', action='store_true', dest='check', help='Executes Tabulation and Memoization and compares the solution')
algorithm.add_argument("-st", action='store_true', dest='tab', help='Solves via Tabulation')
algorithm.add_argument("-sm", action='store_true', dest='mem', help='Solves via Memoization')

args: Namespace = parser.parse_args()

myTestMode = False


def directory_input(directory):
    if os.path.isdir(directory):
        for file in os.listdir(path=directory):
            file_input(str(directory + "/" + file))
    else:
        print(directory, " no es un directorio válido.")
        exit()


def file_input(file):
    print("---------- Archivo = ", file, " -----------")
    if os.path.isfile(str(file)):
        first_iter = True
        problems_num = 0
        checker = 0
        for line in open(file, "r"):

            if first_iter == True:
                problems_num = int(line.split()[2])
                first_iter = False
            else:
                checker = checker+1
                splitter = line.split()
                eggs_num = int(splitter[0])
                floors = int(splitter[1])
                solver(eggs_num, floors)

        if checker != problems_num:print("Error en lo sargumentos del archivo")

    else:
        print("No se encuentra el fichero: ", file)
        exit()

def solver(eggs_num, floors):
    if args.check:
        mem = solve_memoization(eggs_num, floors)
        tab = solve_tabulation(eggs_num, floors)
        print("¿coinciden los métodos Tabulation y Memoization?", mem[eggs_num, floors] == tab[eggs_num][floors])
        extrasCheck(eggs_num, floors, tab, mem)
    elif args.tab:
        tab = solve_tabulation(eggs_num, floors)
        extrasTab(eggs_num, floors, tab)
    else:
        mem = solve_memoization(eggs_num, floors)
        extrasMem(eggs_num, floors, mem)

def extrasCheck(eggs_num, floors, tab, mem):
    if args.o_result:
        print("For ", eggs_num, " eggs and ", floors, " floors. TAB=", tab[eggs_num][floors], " MEM=",
              mem[eggs_num, floors])

    if args.display:


        print("Tabulation matrix:")
        print(numpy.matrix(tab))
        print('\n')
        print("Memoization dictionary")

        for pos in mem:
            print(pos, " = ", mem[pos])


def extrasMem(eggs_num, floors, mem):
    if args.o_result:
        print("For ", eggs_num, " eggs and ", floors, " floors. MEM=", mem[eggs_num, floors])

    if args.display:
        for pos in mem:
            print(pos, " = ", mem[pos])


def extrasTab(eggs_num, floors, tab):
    if args.o_result:
        print("For ", eggs_num, " eggs and ", floors, " floors. TAB=", tab[eggs_num][floors])

    if args.display:
        print("Tabulation matrix:")
        print(numpy.matrix(tab))


def main():
    if myTestMode:
        # Check my tests
        tests = TestKSP()
        tests.test_higherVal()
        print(0, "[ ]")  # Dummy result to mandatory tests

    else:
        if args.time:
            timer = time.time()
            if args.input_data_d is not None:
                directory_input(str(args.input_data_d)[2:-2])
            elif args.input_data is not None:
                file_input(str(args.input_data)[2:-2])
            else:
                eggs_num = int(input("Inserte numero de huevos:"))
                floors = int(input("Inserte numero de pisos:"))
                solver(eggs_num, floors)

            print("Tiempo de ejecución: ", str(time.time() - timer)[0:6], 's')
        else:
            if args.input_data_d is not None:
                directory_input(str(args.input_data_d)[2:-2])
            elif args.input_data is not None:
                file_input(str(args.input_data)[2:-2])
            else:
                eggs_num = int(input("Inserte numero de huevos:"))
                floors = int(input("Inserte numero de pisos:"))
                solver(eggs_num, floors)


if __name__ == '__main__':
    main()
