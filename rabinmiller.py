import sys
import random
from fractions import gcd

if len(sys.argv)>1:
    if sys.argv[1] == "-f":
        print "Fermat test"
        inout_file = open("wejscie.txt", "r")
        output_file = open("wyjscie.txt", "w")
        number1 = inout_file.readline()
        number1 = long(number1)
        k = 0
        b_before = 0
        first = True
        a = random.randint(2, number1-1)
        if gcd(a, number1) != 1:
            output_file.write("na pewno zlozona, dla a =" + str(a))
            exit()
        m = number1 - 1
        while m % 2 != 1:
            k += 1
            m /= 2
        bj = pow(a, m, number1)
        for j in range(0, k):
            bj_before = bj
            bj = pow(bj, 2, number1)
            if bj == 1 & first:
                b_before = bj_before
                first = False
                break
        if bj != 1:
            output_file.write("na pewno zlozona")
            exit()
        output_file.write("brak pewnosci, dla a =" + str(a))
    else:
        print "invalid param"
else:
    inout_file = open("wejscie.txt", "r")
    output_file = open("wyjscie.txt", "w")
    number1 = inout_file.readline()
    number2 = inout_file.readline()
    number3 = inout_file.readline()
    if number3:
        print "option 3"
        number1 = long(number1)
        number2 = long(number2)
        number3 = long(number3)
        number2 = (number2*number3)-1
        for i in range(0, 40):
            print i
            k = 0
            b_before = 0
            first = True
            a = random.randint(2, number1-1)
            if gcd(a, number1) != 1:
                ret = gcd(a, number1)
                output_file.write(str(ret))
                exit()
            m = number2
            while m % 2 != 1:
                k += 1
                m /= 2
            bj = pow(a, m, number1)
            if bj == 1 | bj == number1-1:
                continue
            for j in range(0, k):
                bj_before = bj
                bj = pow(bj, 2, number1)
                if bj == 1 & first:
                    b_before = bj_before
                    first = False
                    break
            ret = gcd(b_before-1, number1)
            if ret != 1:
                output_file.write(str(ret))
                exit()
        output_file.write("prawdopodobnie pierwsza")
    elif number2:
        print "option 2"
        number1 = long(number1)
        number2 = long(number2)
        for i in range(0, 40):
            print i
            k = 0
            b_before = 0
            first = True
            a = random.randint(2, number1-1)
            if gcd(a, number1) != 1:
                ret = gcd(a, number1)
                output_file.write(str(ret))
                exit()
            m = number2
            while m % 2 != 1:
                k += 1
                m /= 2
            bj = pow(a, m, number1)
            if bj == 1 | bj == number1-1:
                continue
            for j in range(0, k):
                bj_before = bj
                bj = pow(bj, 2, number1)
                if bj == 1 & first:
                    b_before = bj_before
                    first = False
                    break
            ret = gcd(b_before-1, number1)
            if ret != 1:
                output_file.write(str(ret))
                exit()
        output_file.write("prawdopodobnie pierwsza")
    elif number1:
        print "option 1"
        number1 = long(number1)
        for i in range(0, 40):
            k = 0
            b_before = 0
            first = True
            a = random.randint(2, number1-1)
            if gcd(a, number1) != 1:
                ret = gcd(a, number1)
                output_file.write(str(ret))
                exit()
            m = number1 - 1
            while m % 2 != 1:
                k += 1
                m /= 2
            bj = pow(a, m, number1)
            if bj == 1 | bj == number1-1:
                continue
            for j in range(0, k):
                bj_before = bj
                bj = pow(bj, 2, number1)
                if bj == 1 & first:
                    b_before = bj_before
                    first = False
                    break
            if bj != 1:
                output_file.write("na pewno zlozona")
                exit()
            else:
                if (b_before-number1) != -1:
                    ret = gcd(b_before-1, number1)
                    output_file.write(str(ret))
                    exit()
        output_file.write("prawdopodobnie pierwsza")
    else:
        print "error 404 file wejscie.txt not found"


