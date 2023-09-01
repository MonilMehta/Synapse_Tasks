from django.http import JsonResponse

import math

from django.shortcuts import render

def is_prime(num):
    if num < 2:
        return True
    
    for i in range(2, num):
        if num % i == 0:
            return False
    
    return True

def prime_divisors(num):
    if is_prime(num):
        return '0'+bin(num)[2:]
    else:
        divisors = [i for i in range(1, num+1) if num % i == 0]
        return divisors

def check_num(request,start, end):
    s=int(start)
    e=int(end)
    result_dict = {}
    for i in range(s, e+1):
        a = prime_divisors(i)
        result_dict[i] = a
    
    return render(request, 'index.html', {'result_dict': result_dict})



