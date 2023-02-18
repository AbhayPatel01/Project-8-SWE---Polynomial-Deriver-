import string 
import pdb 
import re 
import functools 
# Idea 1: (nested class variable(helper), 
# 1.Design (UML)  
# 2 Implement.
# 3 Test (unittest/other statement execution, ) and Debug (pdb) 

# This is a pet project, not for high production code. 
# Prespective Chosen: A Polynomial is a superset of variables: that have a coefficient,a variable identifier and a exponent . 
# Programming Paradigm: OOP
# Program Structure: main program logic and classes 
# Program Style: PEP 8 (Some notions, not all guidelines are closely followed)  
# Programming Improvement/TO DO: 
    # Testing. 
    # Handling Errors. 
    # More overall robustness. 
    # Debugging (used pdb whilst programming)  
    # More refined, design & implementation. 
    # Annotations. 


# Choices: 
    # Not needed: No use of OOP Inheritance, Polymorphism, Abstract Classes, Meta classes, Etc...
    # Programming Techniques: Monads, Currying, etc.. (minimal used) 

class Variable:
    def __init__(self,variable:str, coefficient:int, exponent:int):
        
        self._variable = variable
        self._coefficient = coefficient 
        self._exponent = exponent 

    @classmethod 
    def from_unparsed_data(cls,variable:str,coefficient:list,exponent:list):
        if len(coefficient) == 1:
            sign = coefficient[0][0] 
            if sign == '-':
                coefficient = -1
            else:
                coefficient = 1
        else:
            coefficient = eval(coefficient[0])
        
        if len(exponent) == 1: 
            exponent = 1
        else: 
            exponent = eval( exponent[-1] )

        return cls(variable,coefficient,exponent)

    def get_tuple(self): 
        return (self._coefficient, self._exponent)
    
    def __str__(self):
        # if self._coefficient == 1 and self._exponent == 0 and len(self._variable) == 1: 
            # return self._variable
        if self._coefficient == 1: 
            self._coefficient = ''
        elif self._coefficient > 0:
            self._coefficient = '+' + str(self._coefficient) + '*'
        else:
            self._coefficient = str(self._coefficient) + '*'

        if self._exponent == 0: 
            self._exponent = ''
            self._variable = ''
            self._coefficient = self._coefficient[:-1]
        elif self._exponent == 1: 
            self._exponent = ''
        else:
            self._exponent = '^' + str(self._exponent) 
         
        out = self._coefficient + self._variable + self._exponent
        
        return out
        # if input_variable.lower() in string.ascii_lower(): 

class Polynomial: # + - * ^ single variable. 
    def __init__(self,input_string,allow_simplification=True):
        
        def is_polynomial():
            pass    

        # is_polynomial(input_string)
        self._polynomial = input_string 

        def compose(*functions,element):
            for function in functions:
                element = function(element)
            return element 
        
        re.sub0 = functools.partial(re.sub, r'^[+-]?\d*[+-]|[+-]\d*$', '') # 
        re.sub1 = functools.partial(re.sub, r'[+-]\d+([+-])', r'\1')
        re.sub2 = functools.partial(re.sub, r'^\+?(.*)', r'\1')

        
        input_string = compose(re.sub0,re.sub1,re.sub2,element=input_string.replace(' ','').lower()) 
        
        _vars = []
        var_string = ''
        for index in range(len(input_string)):
            var_string += input_string[index]

            if index + 1 < len(input_string) and input_string[ index + 1 ] in ['+','-']:
                _vars.append(var_string)
                var_string = ''        
        _vars.append(var_string) 
        
        @functools.cache
        def var_literal():
            for x in self._polynomial: 
                if x in string.ascii_lowercase:
                    return x

        def func(variable_term):
            var1 = Variable.from_unparsed_data(var_literal(),variable_term.split('*'),variable_term.split('^'))
            return var1.get_tuple()

        self._data = list(map(func, _vars))
        self._literal = var_literal() 

        def simplify():
            simplify = {}
            simplify = simplify.fromkeys([v for _,v in self._data],0)
            for k,v in self._data: 
                simplify[v] += k
            return [(k,v) for v,k in simplify.items()]

        if allow_simplification: # local vars > parameter
            self._data = simplify()

        # print(self._polynomial)
        # print(self._literal)
    
    def __str__(self): 
        return self._polynomial


    def derive(self):
        out = ''
        for coeff, exp in self._data:
            if coeff == 1 and exp == 1: 
                out += '+1'
            else:
                var1 = Variable(self._literal,coeff * exp, exp - 1)
                out += str(var1) + ' '
        if out[0] == '+':
            return out[1:]
        return out 


if __name__ == '__main__': 
    try: 
        while True: 
                input_string = input('Enter Polynomial: ')
                input_string2 = input('Simplify the output (y/n/anything else is a no): ')
                if input_string.isnumeric(): 
                    print('Derivative','0')
                    continue
                elif len(input_string) == 1 and input_string in string.ascii_lowercase: 
                    print('Derivative','1')
                    continue

                if input_string2.lower() not in ['y','yes','ye']:
                    print('Unsimplified')
                    p1 = Polynomial(input_string,False)
                else: 
                    print('Simplified')
                    p1 = Polynomial(input_string)
                
                print('Derivative:',p1.derive())
    except EOFError: 
                print('Program Exited.')
    except: 
                print('Error occured, Unknown. Please Ensure Input Follows the following convention.')
                print('E.g.: 123781 + 2 * a ^ 817126 - 23 * a ^ 10 - a ^ 5 + a - 12821012793 ')




# Idea 2.
# 1.Programmign Paragdim: OOP, Design (UML)  
# 2 Implement. 
# 3 Test (unittest/other statement execution, ) and Debug (pdb) 
# 4 Helper Modules: GUi (tkinter) version/Cli version , symbol(symblab, etc..) 
# Helper Modules: string,GUI (tkinter) version/Cli version , symbol(symblab, etc..) 

# Idea 2. 
# 1 Modules.  
