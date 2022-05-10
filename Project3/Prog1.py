#!/usr/bin/env python3
# Julian Ogata
# CPSC 323-04
# 2022-5-01
# jogata@csu.fullerton.edu
#
# Traces an input string to determine if string adhears to CFG
#

"""Project 3: Trace Program"""

import sys
from time import sleep

class Trace:
    '''Trace Class'''

    def __init__(self):
        self._terminals = ['(', ')', '$', 'a', 'b', '+', '-', '/', '*', '=']
        self._user_string = []
        self._trace_string = []
        self._trace_stack = ['$', 'S']
        self._cfg = {'S':['a=E'],
                     'E':['TR'],
                     'R':['+TR', '-TR', 'e'],
                     'T':['FQ'],
                     'Q':['*FQ', '/FQ', 'e'],
                     'F':['(E)', 'a', 'b']}

    @property
    def terminals(self):
        '''Gets list of terminals'''
        return self._terminals

    @property
    def user_string(self):
        '''Gets the user's original string'''
        return self._user_string

    @user_string.setter
    def user_string(self, user_string):
        '''Sets the user's original string'''
        self._user_string = user_string

    @property
    def trace_string(self):
        '''Gets the string used for tracing'''
        return self._trace_string

    @trace_string.setter
    def trace_string(self, x):
        '''Sets the string used for tracing'''
        self._trace_string = x

    @property
    def trace_stack(self):
        '''Gets the stack'''
        return self._trace_stack

    def print_string(self):
        '''Prints the original string in a readable form'''
        return ''.join(map(str, self.user_string))

    def cfg_prod_add(self, key, pos):
        '''Gets the productions from dict and stores in stack'''
        terms = list(self._cfg.get(key)[pos])
        for term in reversed(terms):
            self.trace_stack_add(term)

    def trace_stack_add(self, term):
        '''Appends a term/production in the stack'''
        self._trace_stack.append(term)

    def check_end(self):
        '''Checks if the trace is complete'''
        if self.trace_string[0] == '$' and self.trace_stack[-1] == '$':
            return True
        return False

    def user_input(self):
        '''Prompts user for input'''
        print('NOTE: sleep() function used for process observation')
        self.user_string = list(input('Please input a string: '))
        self.trace_string = self.user_string.copy()
        if self.trace_string[-1] != '$':
            self.trace_string.append('$')
        print('Tracing string...')

    def trace(self):
        '''Begins the tracing'''
        print('Stack: {}'.format(self.trace_stack))
        self.next_state(self.trace_stack[-1])

    def next_state(self, state):
        '''Choses next state'''
        sleep(0.5)
        if self.check_end():
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.trace_string[0] == ' ' and self.trace_string[0] != '$':
            self.trace_string.pop(0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif state == 'S':
            print('\n----------------')
            print('In State S')
            self.state_S()
        elif state == 'E':
            print('\n----------------')
            print('In State E')
            self.state_E()
        elif state == 'Q':
            print('\n----------------')
            print('In State Q')
            self.state_Q()
        elif state == 'T':
            print('\n----------------')
            print('In State T')
            self.state_T()
        elif state == 'R':
            print('\n----------------')
            print('In State R')
            self.state_R()
        elif state == 'F':
            print('\n----------------')
            print('In State F')
            self.state_F()
        elif self.stack_term_check and self.trace_string[0] != '$'\
           and self.trace_stack[-1] != '$':
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.check_state()

    def stack_term_check(self):
        '''Checks if there is a terminal on the end of the stack'''
        if self._trace_stack[-1] in self.terminals:
            return True
        return False

    def stack_empty(self):
        '''Checks if the stack is empty and if the string still have terms '''
        if len(self.trace_stack) == 1 and len(self.trace_string) > 1:
            return True
        return False

    def state_S(self):
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            exit
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.print_string()))
                self.check_state()
        if self.trace_string[0] == 'a':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('S', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == '$':
            self.trace_stack.pop(-1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.next_state(self.trace_stack[-1])
        else:
            print('{} does not conform...\nExiting'.format(self.print_string()))


    def state_E(self):
        '''Traces through E'''
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            exit
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.print_string()))
                self.check_state()
        if self.trace_string[0] == 'a' or self.trace_string[0] == 'b'\
           or self.trace_string[0] == '(':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('E', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == ')' or self.trace_string[0] == '$':
            self.trace_stack.pop(-1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.next_state(self.trace_stack[-1])
        else:
            print('{} does not conform...\nExiting'.format(self.print_string()))

    def state_R(self):
        '''Traces through R'''
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            exit
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.next_state(self.trace_stack[-1])
        if self.trace_string[0] == '+':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('R', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == '-':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('R', 1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == ')' or self.trace_string[0] == '$':
            self.trace_stack.pop(-1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.next_state(self.trace_stack[-1])
        else:
            print('{} does not conform...\nExiting'.format(self.print_string()))

    def state_T(self):
        '''Traces through T'''
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            exit
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.next_state(self.trace_stack[-1])
        if self.trace_string[0] == 'a' or self.trace_string[0] == 'b'\
           or self.trace_string[0] == '(':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('T', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.next_state(self.trace_stack[-1])
        elif self.trace_string[0] == ')' or self.trace_string[0] == '$':
            self.trace_stack.pop(-1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.next_state(self.trace_stack[-1])
        else:
            print('{} does not conform...\nExiting'.format(self.print_string()))

    def state_Q(self):
        '''Traces through Q'''
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            exit
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            exit
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.check_state()
        if self.trace_string[0] == '*':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('Q', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == '/':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('Q', 1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == '+' or self.trace_string[0] == '-'\
           or self.trace_string[0] == ')' or self.trace_string[0] == '$':
            self.trace_stack.pop(-1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        else:
            print('{} does not conform...\nExiting'.format(self.print_string()))

    def state_F(self):
        '''Traces through F'''
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            sys.exit()
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.next_state(self.trace_stack[-1])
        if self.trace_string[0] == '(':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('F', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == 'a':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('F', 1)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        elif self.trace_string[0] == 'b':
            self.trace_stack.pop(-1)
            self.cfg_prod_add('F', 2)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()
        else:
            self.trace_stack.pop(-1)
            self.cfg_prod_add('F', 0)
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            self.check_state()


    def check_state(self):
        '''Checks the state's productions for terminals'''
        sleep(0.5)
        print('\nChecking Production and Terminals')
        if self.check_end() is True:
            print('\n{} is Accepted!'.format(self.print_string()))
            print('Stack: {}'.format(self.trace_stack))
            print('Input_str: {}'.format(self.trace_string))
            sys.exit()
        elif self.stack_empty() is True:
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()
        elif self.stack_term_check() is True:
            if self.trace_string[0] == self.trace_stack[-1]:
                self.trace_string.pop(0)
                self.trace_stack.pop(-1)
                print('Stack: {}'.format(self.trace_stack))
                print('Input_str: {}'.format(self.trace_string))
                self.next_state(self.trace_stack[-1])
        else:
            self.next_state(self.trace_stack[-1])

    def reset(self):
        '''Resets Values'''
        self._user_string = []
        self._trace_string = []
        self._trace_stack = ['$', 'S']

    def run(self):
        '''Runs program'''
        self.user_input()
        self.trace()

    def run_test1(self):
        '''Runs test 1'''
        print('Running Test 1')
        self.user_string = 'a = (a +a )*b$'
        self.trace_string = list(self.user_string).copy()
        if self.trace_string[-1] != '$':
            self.trace_string.append('$')
        print('Tracing string...')
        self.trace()
        print('Test 1 Complete\n')
        self.reset()

    def run_test2(self):
        '''Runs test 2'''
        print('Running Test 2')
        self.user_string = 'a=a*(b -a)$'
        self.trace_string = list(self.user_string).copy()
        if self.trace_string[-1] != '$':
            self.trace_string.append('$')
        print('Tracing string...')
        self.trace()
        print('Test 2 Complete\n')
        self.reset()

    def run_test3(self):
        '''Runs test 3'''
        print('Running Test 3')
        self.user_string = ' a=(a+a)b$'
        self.trace_string = list(self.user_string).copy()
        if self.trace_string[-1] != '$':
            self.trace_string.append('$')
        print('Tracing string...')
        self.trace()
        print('Test 3 Complete\n')
        self.reset()


if __name__ == '__main__':
    T = Trace()
    T.run_test1()
    sleep(2)
    T.run_test2()
    sleep(2)
    T.run_test3()
