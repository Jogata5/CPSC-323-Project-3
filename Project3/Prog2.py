#!/usr/bin/env python3
# Julian Ogata
# CPSC 323-04
# 2022-5-01
# jogata@csu.fullerton.edu
#
# Calculates a user given postfix expression
#

"""Project 3: Post-Fix Program"""

import operator

class PostFix:
    '''Holds methods to calculate a given expression in postfix notation'''
    def __init__(self):
        self._operations = {'+' : operator.add,
                            '-' : operator.sub,
                            '*' : operator.mul,
                            '/' : operator.truediv,
                            '%' : operator.mod,
                            '^' : operator.pow}
        self._user_str = []
        self._stack = ['$']
        self._assigned_vals = {}

    @property
    def operations(self):
        '''Gets operation dict'''
        return self._operations

    @property
    def user_str(self):
        '''Gets user string'''
        return self._user_str

    @user_str.setter
    def user_str(self, new_str):
        '''Sets user string'''
        self._user_str = new_str

    @property
    def stack(self):
        '''Gets stack'''
        return self._stack

    @stack.setter
    def stack(self, new_stack):
        '''Sets stack'''
        self._stack = new_stack

    @property
    def assigned_vals(self):
        '''Gets the assigned values of variables dict'''
        return self._assigned_vals

    @assigned_vals.setter
    def assigned_vals(self, new_val):
        '''Sets the dict of assigned values'''
        self._assigned_vals = new_val

    def user_input(self):
        '''Asks user for an expression and variable values'''
        in_input = True
        counter = 0
        while in_input:
            expr_str = input('Enter a postfix expression with a $ at the end: ')
            if expr_str[-1] != '$':
                print('Please add a "$" at the end of the expression')
            else:
                in_input = False
        # Loops through given expression until it encounters "$"
        while expr_str[counter] != '$':
            # Check if the current variable is not an operator or has already been assigned a value
            if expr_str[counter] not in self.operations\
               and expr_str[counter] not in self.assigned_vals.keys():
                # Start assigning integer value
                while True:
                    try:
                        value = int(input('Enter the value of {}: '.format(expr_str[counter])))
                        self.user_str.append(value)
                        self.assigned_vals.update({expr_str[counter]: value})
                        break
                    except ValueError:
                        print('Please input a integer')
            # If variable already assigned, push value onto user_str
            elif expr_str[counter] in self.assigned_vals.keys():
                self.user_str.append(self.assigned_vals.get(expr_str[counter]))
            # If variable is an operator, push onto user_str
            elif expr_str[counter] in self.operations:
                self.user_str.append(expr_str[counter])
            counter += 1
        self.user_str.append('$')
        print("user str: {}".format(self.user_str))

    def translate(self):
        '''Translates the user's string, calculates values, and adds to stack'''
        counter = 0
        # Loop through user_str until "$" is encountered
        while self.user_str[0] != '$':
            # If the value is an operator, calculate integers in stack and pop
            if self.user_str[0] in self.operations:
                counter = self.calculate(self.user_str[0], counter)
                self.user_str.pop(0)
            # Append value onto stack
            else:
                self.stack.append(self.user_str[0])
                self.user_str.pop(0)
            print('Stack: {}'.format(self.stack))
            counter += 1

    def calculate(self, operation, counter):
        """Pops and calculates values in stack with given operator,
           returns the new position of the stack"""
        oper = self.operations.get(operation)
        x_var = self.stack.pop()
        y_var = self.stack.pop()
        result = oper(y_var, x_var)
        print('{} {} {} = {}'.format(y_var, operation, x_var, result))
        self.stack.append(result)
        return counter - 1

    def reset(self):
        '''Resets class variables'''
        self.user_str = []
        self.assigned_vals = {}
        self.stack = ['$']

    def run(self):
        '''Runs Program'''
        running = True
        prompt = True
        while running:
            self.user_input()
            self.translate()
            if len(self.stack) == 2:
                print('Final value = {}'.format(self.stack[-1]))
            else:
                print('Expression did not result in a final value\n\tStack: {}'
                      .format(self.stack))
            while prompt:
                conintue = input('Continue(y/n)?')
                if conintue == 'y':
                    self.reset()
                    prompt = False
                elif conintue == 'n':
                    running = False
                    prompt = False
                else:
                    print('Please input either "y" or "n"')
            prompt = True


if __name__ == '__main__':
    POST = PostFix()
    POST.run()
        