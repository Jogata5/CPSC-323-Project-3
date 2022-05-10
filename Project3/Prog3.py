#!/usr/bin/env python3
# Julian Ogata
# CPSC 323-04
# 2022-5-01
# jogata@csu.fullerton.edu
#
# Traces an input string to determine if string adhears to CFG
#

"""Project 3: CFG Parsing Table Program"""

import sys
from time import sleep

class Trace:
    '''Trace Class'''

    def __init__(self):
        self._terminals = ['(', ')', 'i', '+', '-', '/', '*']
        self._user_string = []
        self._trace_string = []
        self._stack = [0]
        self._cfg_lhs = {1 : ['E', 'E+T'],
                         2 : ['E', 'E-T'],
                         3 : ['E', 'T'],
                         4 : ['T', 'T*F'],
                         5 : ['T', 'T/F'],
                         6 : ['T', 'F'],
                         7 : ['F', '(E)'],
                         8 : ['F', 'i']}

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
    def trace_string(self, new_str):
        '''Sets the string used for tracing'''
        self._trace_string = new_str

    @property
    def stack(self):
        '''Gets the stack'''
        return self._stack

    @property
    def cfg_lhs(self):
        '''Gets the left hand side of the cfg'''
        return self._cfg_lhs

    def print_string(self):
        '''Prints the original string in a readable form'''
        return ''.join(map(str, self.user_string))

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
        state = 0
        while state != 'accepted':
            print('Stack: {}\nString: {}'.format(self.stack, self._trace_string))
            state = self.stack[-1]
            self.next_state(state)

    def next_state(self, state, reducing=False):
        '''Choses next state'''
        sleep(0.5)
        if state == 0:
            print('\n----------------')
            print('In State 0')
            self.state_0(reducing)
        elif state == 1:
            print('\n----------------')
            print('In State 1')
            self.state_1(reducing)
        elif state == 2:
            print('\n----------------')
            print('In State 2')
            self.state_2(reducing)
        elif state == 3:
            print('\n----------------')
            print('In State 3')
            self.state_3(reducing)
        elif state == 4:
            print('\n----------------')
            print('In State 4')
            self.state_4(reducing)
        elif state == 5:
            print('\n----------------')
            print('In State 5')
            self.state_5(reducing)
        elif state == 6:
            print('\n----------------')
            print('In State 6')
            self.state_6(reducing)
        elif state == 7:
            print('\n----------------')
            print('In State 7')
            self.state_7(reducing)
        elif state == 8:
            print('\n---------------')
            print('In State 8')
            self.state_8(reducing)
        elif state == 9:
            print('\n----------------')
            print('In State 9')
            self.state_9(reducing)
        elif state == 10:
            print('\n----------------')
            print('In State 10')
            self.state_10(reducing)
        elif state == 11:
            print('\n----------------')
            print('In State 11')
            self.state_11(reducing)
        elif state == 12:
            print('\n----------------')
            print('In State 12')
            self.state_12(reducing)
        elif state == 13:
            print('\n----------------')
            print('In State 13')
            self.state_13(reducing)
        elif state == 14:
            print('\n----------------')
            print('In State 14')
            self.state_14(reducing)
        elif state == 15:
            print('\n----------------')
            print('In State 15')
            self.state_15(reducing)

    def shift(self):
        '''Shifts string value onto stack'''
        print('SHIFTING')
        self.stack.append(self.trace_string[0])
        self.trace_string.pop(0)

    def reduce(self, cfg_num):
        '''Reduces stack value using cfg'''
        print('REDUCING')
        last_state = 0
        lhs = self.cfg_lhs.get(cfg_num)
        temp_production = list(lhs[1])
        temp_stack = self.stack
        while temp_production:
            sleep(0.5)
            print('Production: {}'.format(temp_production))
            print('Stack Value: {}'.format(temp_stack[-1]))
            if temp_stack[-1] == temp_production[-1]:
                temp_production.pop()
                temp_stack.pop()
            else:
                temp_stack.pop()
        for i in self.stack:
            if isinstance(i, int):
                last_state = i
        self.stack.append(lhs[0])
        self.next_state(last_state, True)

    def state_0(self, reducing=False):
        '''State 0'''
        if reducing:
            if self.stack[-1] == 'E':
                self.stack.append(1)
            elif self.stack[-1] == 'T':
                self.stack.append(2)
            elif self.stack[-1] == 'F':
                self.stack.append(3)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_1(self, reducing=False):
        '''State 1'''
        if self.trace_string[0] == '+':
            self.shift()
            self.stack.append(6)
        elif self.trace_string[0] == '-':
            self.shift()
            self.stack.append(7)
        elif self.trace_string[0] == '$':
            print('String Accepted!')
            self.stack.append('accepted')
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_2(self, reducing=False):
        '''State 2'''
        if self.trace_string[0] in ['+', '-', ')', '$']:
            self.reduce(3)
        elif self.trace_string[0] == '*':
            self.shift()
            self.stack.append(8)
        elif self.trace_string[0] == '/':
            self.shift()
            self.stack.append(9)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_3(self, reducing=False):
        '''State 3'''
        if self.trace_string[0] in ['+', '-', '*', '/', ')', '$']:
            self.reduce(6)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_4(self, reducing=False):
        '''State 4'''
        if reducing:
            if self.stack[-1] == 'E':
                self.stack.append(10)
            elif self.stack[-1] == 'T':
                self.stack.append(2)
            elif self.stack[-1] == 'F':
                self.stack.append(3)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_5(self, reducing=False):
        '''State 5'''
        if self.trace_string[0] in ['+', '-', '*', '/', ')', '$']:
            self.reduce(8)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_6(self, reducing=False):
        '''State 6'''
        if reducing:
            if self.stack[-1] == 'T':
                self.stack.append(11)
            elif self.stack[-1] == 'F':
                self.stack.append(3)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_7(self, reducing=False):
        '''State 7'''
        if reducing:
            if self.stack[-1] == 'T':
                self.stack.append(12)
            elif self.stack[-1] == 'F':
                self.stack.append(3)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_8(self, reducing=False):
        '''State 8'''
        if reducing:
            if self.stack[-1] == 'F':
                self.stack.append(13)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_9(self, reducing=False):
        '''State 9'''
        if reducing:
            if self.stack[-1] == 'F':
                self.stack.append(14)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()
        else:
            if self.trace_string[0] == 'i':
                self.shift()
                self.stack.append(5)
            elif self.trace_string[0] == '(':
                self.shift()
                self.stack.append(4)
            else:
                self.stack.append('not accepted')
                print('{} does not conform...\nExiting'.format(self.print_string()))
                sys.exit()

    def state_10(self, reducing=False):
        '''State 10'''
        if self.trace_string[0] == '+':
            self.shift()
            self.stack.append(6)
        elif self.trace_string[0] == '-':
            self.shift()
            self.stack.append(7)
        elif self.trace_string[0] == ')':
            self.shift()
            self.stack.append(15)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_11(self, reducing=False):
        '''State 11'''
        if self.trace_string[0] in ['+', '-', ')', '$']:
            self.reduce(1)
        elif self.trace_string[0] == '*':
            self.shift()
            self.stack.append(8)
        elif self.trace_string[0] == '/':
            self.shift()
            self.stack.append(9)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_12(self, reducing=False):
        '''State 12'''
        if self.trace_string[0] in ['+', '-', ')', '$']:
            self.reduce(2)
        elif self.trace_string[0] == '*':
            self.shift()
            self.stack.append(8)
        elif self.trace_string[0] == '/':
            self.shift()
            self.stack.append(9)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_13(self, reducing=False):
        '''State 13'''
        if self.trace_string[0] in ['+', '-', '*', '/', ')', '$']:
            self.reduce(4)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_14(self, reducing=False):
        '''State 14'''
        if self.trace_string[0] in ['+', '-', '*', '/', ')', '$']:
            self.reduce(5)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def state_15(self, reducing=False):
        '''State 15'''
        if self.trace_string[0] in ['+', '-', '*', '/', ')', '$']:
            self.reduce(7)
        else:
            self.stack.append('not accepted')
            print('{} does not conform...\nExiting'.format(self.print_string()))
            sys.exit()

    def reset(self):
        '''Resets Class Values'''
        self._user_string = []
        self._trace_string = []
        self._stack = [0]

    def run(self):
        '''Runs program'''
        self.user_input()
        self.trace()

    def run_test1(self):
        '''Runs test 1'''
        print('Running Test 1')
        self.user_string = '(i+i)*i$'
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
        self.user_string = '(i*)$'
        self.trace_string = list(self.user_string).copy()
        if self.trace_string[-1] != '$':
            self.trace_string.append('$')
        print('Tracing string...')
        self.trace()
        print('Test 2 Complete\n')
        self.reset()


if __name__ == '__main__':
    T = Trace()
    print('Running Tests...')
    sleep(1)
    T.run_test1()
    sleep(2)
    T.run_test2()
    T.run()
