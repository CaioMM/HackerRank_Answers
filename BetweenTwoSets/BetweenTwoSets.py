"""
MIT License

Copyright (c) 2021 Caio Mateus

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
rom copy import copy
def lcm(a):
    """
    Function that calculates the least common multiple
    of a list.
    Parameters:
    a -> list of integers with length = n.
    """
    arr_1 = copy(a)
    arr_1.sort()
#     print(arr_1)
    for item in arr_1:
        assert (type(item) == int), "It is not a integer"
    
    
    ones = arr_1.count(1)
    tamanho = len(arr_1)
    if ones == tamanho:
        return 1

    divisores = []
    divisor = 2
    cont_div = 0
    while arr_1.count(1) != tamanho:
        cont = 0
        for i in range(tamanho):
            if arr_1[i] % divisor == 0:
                arr_1[i] = arr_1[i]/divisor
                cont_div += 1
            else:
                cont += 1
            if i == tamanho-1 and cont_div != 0: 
                divisores.append(divisor)
                
                cont_div = 0
                
            if cont == tamanho:
                divisor += 1
    r = 1
    for num in divisores:
        r = r*num
    return r

def gcd(a):
    """
    Function that calculates the greatest common divisor
    or highest common factor of a list.
    Parameters:
    a -> list of integers with length = n.
    """
    
    arr_1 = copy(a)
    arr_1.sort()
#     print(arr_1)
    for item in arr_1:
        assert (type(item) == int), "It is not a integer"
    
    
    ones = arr_1.count(1)
    tamanho = len(arr_1)
    if ones == tamanho:
        return 1

    divisores = []
    divisor = 2
    cont_div = 0
    while arr_1.count(1) != tamanho:
        cont = 0
        for i in range(tamanho):
#             print(arr_1[i],divisor)
            if arr_1[i] % divisor == 0:
                arr_1[i] = arr_1[i]/divisor
                cont_div += 1
            else:
                cont += 1
            if i == tamanho-1 and cont_div != 0: 
#                 print(i,cont_div)
                if cont_div == tamanho:
                    divisores.append(divisor)
                
                cont_div = 0
                
            if cont == tamanho:
                divisor += 1

    r = 1
    for i in divisores:
        print(i)
        r = r*i
    return r

def getTotalX(a, b):
    # Write your code here
    multiplier = 1
    count = 0
    while True:
        if gcd(b) % (multiplier * lcm(a)) == 0:
            count += 1
            multiplier += 1
        elif gcd(b) % (multiplier * lcm(a)) == gcd(b):
            break
        else:
            multiplier += 1
    return count