import os
import re
import sympy
from sympy.parsing.sympy_parser import parse_expr
from sympy.polys.polytools import degree
from sympy import symbols,expand,factor,Poly


import random
from helper import *

def make_simple_addition_problem(target,*args,**kwargs):
    """
    """
    digits = range(0,25)

    while True:
        r1=random.choice(digits)
        if (r1<target):
            break
    r2 = target-r1
    c1=sympy.Symbol(str(r1))
    c2=sympy.Symbol(str(r2))
    lhs = c1 + c2
    
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    outstr="\\overline{"+str(r1)+"+"+str(r2)+"}"
    print "about to return "+outstr
    print r1,r2
    return outstr, sols

def make_simple_multiplication_problem(target,*args,**kwargs):
    """
    """
    r1,r2 = get_smaller_coefficients(2)
    r3=target-r1*r2
    c1=sympy.Symbol(str(r1))
    c2=sympy.Symbol(str(r2))
    c3=sympy.Symbol(str(r3))
    lhs = c1 * c2 + c3
    
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    if len(sols) == 0:
        return make_quadratic_eq()
    print "lhs:"
    print lhs

    #outstr=render(lhs).replace('\\cdot','\\times').replace("$$","")
    sign="+" if r3>=0 else ""
    outstr="\\overline{"+str(r1)+"\\times"+str(r2)+ sign +str(r3)+"}"
    print "about to return "+outstr
    print r1,r2,r3
    return outstr, sols

def make_simple_division_problem(target,*args,**kwargs):
    ints = range(2,14)
    c=random.choice(ints)
    outstr="\\frac{"+str(c*target)+"}{"+str(c)+"}"
    return "\overline{"+outstr+"}",[]

def make_fraction_addition_problem(target,*args,**kwargs):
    primes = [2,3,5,7,11,13]
    ints = range(2,14)
    these_primes=prime_factors(target)
    
    while True:

        while True:
            c=random.choice(primes)
            if c not in these_primes:
                break
        while True:
            f=random.choice(primes)
            if f not in these_primes and f != c:
                break
        while True:
            b=random.choice(ints)
            if b not in [c,f]:
                break
        e=target-b
        f1 = sympy.fraction(sympy.S(b)/sympy.S(c*f))
        f2 = sympy.fraction(sympy.S(e)/sympy.S(c*f))

    
        ap,bp=make_proper(f1[0],f1[1])
        dp,ep=make_proper(f2[0],f2[1])
        if bp!=0 and ep!=0 and f1[1] != f2[1]:
                break
    print "-------------"
    print "Below is trying to get "+str(target)
    print ":".join([str(i) for i in [target,c,f,b,e,ap,bp,dp,ep]])
    print str(bp)+"/"+str(c*f) +"+"+str(ep)+"/"+str(f*c)
    sign="+" if ep>=0 else "-"
    outstr=str(ap) if ap !=0 else ""
    outstr="\\frac{"+str(bp)+"}{"+str(f1[1])+"}"
    second_int = str(dp) if dp !=0 else ""
    outstr+=sign+second_int+"\\frac{"+str(abs(ep))+"}{"+str(f2[1])+"}"
    return "\\overline{"+outstr+"}",[]

def make_simplify_ratio_problem(target,*args,**kwargs):
    ints = range(2,14)
    c=random.choice(ints)
    while True:
            b=random.choice(ints)
            if b != c:
                break
    outstr="\\frac{"+str(c*target)+"}{"+str(c*b)+"}"
    return "\overline{"+outstr+"}",[]

def make_quadratic_eq(target, rhs = None, integer=[0, 1]):
    var=random.choice("pqrstuvwxyz")
    x = sympy.Symbol("x")
    f=random.randint(1,5)*random.choice([-1,1])
    r1=target
    while r1==target:
        r1=random.randint(1,20)
    r2=target-r1
    expr = (f*x-r1*f)*(x-r2)
    expanded_expr = expand(expr)
    print "I chose {}, {}, and {}".format(f,r1,r2)
    ex = Poly(expanded_expr, x)
    a,b,c=tuple(ex.coeffs())
    print "I got {},{} and {}".format(a,b,c)
    out_str="{}{}^2{}{}{}".format(a,var,right_sign(b),var,right_sign(c))
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    out_str="\\overline{"+out_str+"}"
    return out_str,sols

def two_digit_subtraction(target,*args,**kwargs):

    digits = range(50,99)

    
    r1=random.choice(digits)
    r2 = r1 - target
    c1=sympy.Symbol(str(r1))
    c2=sympy.Symbol(str(r2))
    lhs = r1 - r2
    
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    outstr=stack_em(r1,r2,"-")
    print "about to return "+outstr
    print r1,r2
    return outstr, sols


def two_digit_subtraction(target,*args,**kwargs):

    digits = range(50,99)

    
    r1=random.choice(digits)
    r2 = r1 - target
    c1=sympy.Symbol(str(r1))
    c2=sympy.Symbol(str(r2))
    lhs = r1 - r2
    
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    outstr=stack_em(r1,r2,"-")
    print "about to return "+outstr
    print r1,r2
    return outstr, sols

def two_digit_multiplication(target,*args,**kwargs):
 
    single_digits=range(1,10)
    trier=2
    while isPrime(trier):
        a=random.choice(single_digits)
        b=random.choice(single_digits)
        trier=1000*a+10*target+b
        
    p=prime_factors(trier)
    mx=max(p)
    p.remove(mx)
    rest=reduce(lambda x, y: x*y, p)

    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    outstr=stack_em(mx,rest,operator="\\times")
    print "about to return "+outstr
    return outstr, sols

def add_coins(target,*args,**kwargs):
    quarters=int(target/25)
    dimes=int(target/10)
    nickels=int(target/5)
    pennies=target
    
    number_words="one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen,twenty,twenty-one,twenty-two,twenty-three,twenty-four,twenty-five,twenty-six,twenty-seven".split(",")
    
    choices={}
    coins={'quarters':{'value':25,'singular':'quarter'},
           'dimes':   {'value':10,'singular':'dime'},
            'nickels':{'value':5,'singular':'nickel'},
            'pennies':{'value':1,'singular':'penny'}}

    
    total=target
    keys=coins.keys()
    indicies=range(4)
    purse={}
    while total>0:
        idx=random.choice(indicies)
        coin=keys[idx]
        value=coins[coin]['value']
        if total-value>=0:
            if coin in purse:
                purse[coin]+=1
            else:
                purse[coin]=1
            total-=value

    out_str="\\overline{"
    for coin in purse.keys():
        coin_name=coin if purse[coin]>1 else coins[coin]['singular']

        out_str+="\\textrm{"+number_words[purse[coin]-1]+" "+coin_name+"}"
        if coin==purse.keys()[0]:
            out_str+="}"

        if coin !=purse.keys()[-1]:
            out_str+="\\\\"

    print out_str
    return out_str,"$$ $$"

def exponents_problem(target,*args,**kwargs):
    list_of_perfect_powers=get_power_choices()
    constant=target-sum(list_of_perfect_powers)
    out_str=""
    for pp in list_of_perfect_powers:
        pp_pick=get_power_choice(pp)
        out_str+="{}^{}".format(pp_pick['base'],pp_pick['power'])
        if pp!=list_of_perfect_powers[-1]:
            out_str+="+"
    if constant>0:
        out_str+="+{}".format(constant)
    elif constant<0:
        out_str+="{}".format(constant)
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    out_str="\\overline{"+out_str+"}"
    return out_str,sols

def roots_problem(target,*args,**kwargs):
    list_of_perfect_powers=get_power_choices()
    out_str=""
    base_sum=0
    for pp in list_of_perfect_powers:
        pp_pick=get_power_choice(pp)
        base_sum+=pp_pick['base']
        out_str+="\sqrt[{}]".format(pp_pick['power'])+"{"
        out_str+=str(pp)+"}"
        if pp!=list_of_perfect_powers[-1]:
            out_str+="+"
    constant=target-base_sum
    if constant>0:
        out_str+="+{}".format(constant)
    elif constant<0:
        out_str+="{}".format(constant)
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    out_str="\\overline{"+out_str+"}"
    return out_str,sols

def simple_algebra(target,*args,**kwargs):
    coefficient=random.randint(1,13)
    rhs=random.randint(1,30)
    constant=rhs-coefficient*target
    out_coefficient=str(coefficient) if coefficient>1 else ""
    if constant>0:
        out_constant="+{}".format(constant)
    elif constant<0:
        out_constant="{}".format(constant)
        
    sols = sympy.latex(target) 
    out_str="{}x{}={}".format(out_coefficient,out_constant,rhs)
    out_str="\\overline{"+out_str+"}"
    return out_str,sols

def decimal_addition(target,num_places,*args,**kwargs):
    f=random.uniform(.1,.9)
    a=float(int(target*f*10**num_places))/10**num_places
    b=float(round((target-a)*10**num_places))/10**num_places
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    #out_str="\\overline{"+"{}+{}".format(a,b)+"}"
    out_str=stack_em(a,b,'+')
    return out_str,sols

def single_decimal_addition(target,*args,**kwargs):
    return decimal_addition(target,1)

def determinant_problem(target,*args,**kwargs):
 
    single_digits=range(1,10)
    trier=2
    while isPrime(abs(trier)):
        a=random.choice(single_digits)
        d=random.choice(single_digits)
        trier=a*d-target
        
    p=prime_factors(abs(trier))
    idx=random.randint(0,len(p)-1)
    p[idx]=p[idx]*numpy.sign(trier)
    b=random.choice(p)
    c=trier/b
    out_str="\\overline{\\begin{vmatrix}"+"{} & {} \\\ {} & {} ".format(a,b,c,d)+" \\end{vmatrix}}"
    sols = sympy.latex(target) 
    sols = "$$" + sols + "$$"
    return out_str,sols

if __name__ == "__main__":
    print make_fraction_addition_problem(21)



