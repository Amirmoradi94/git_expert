# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:59:08 2021

@author: Amir
"""
import numpy as np
from characters import ArrayofLetter
from dates_list import get_days
import csv, argparse
from tkinter import *

char_object = ArrayofLetter
parser = argparse.ArgumentParser()
root = Tk() 


input_string_list = []
output_days = []
sum_of_word_columns = 0
num_calendar_row = 7
num_calendar_column = 53
counter = 0

###------------------------------------------------------------------
parser.add_argument("-mode", "--mode", help = "Result (p: table preview -- o: csv output)", type=str)
parser.add_argument("-input", "--input", help = "Input text", type=str)

args = parser.parse_args()

###------------------------------------------------------------------
fundamental_chars = {'a':char_object.str_a(), 'b':char_object.str_b(), 'c':char_object.str_c(), 'd':char_object.str_d(),
                     'e':char_object.str_e(), 'f':char_object.str_f(), 'g':char_object.str_g(), 'h':char_object.str_h(),
                     'i':char_object.str_i(), 'j':char_object.str_j(), 'k':char_object.str_k(), 'l':char_object.str_l(),
                     'm':char_object.str_m(), 'n':char_object.str_n(), 'o':char_object.str_o(), 'p':char_object.str_p(),
                     'q':char_object.str_q(), 'r':char_object.str_r(), 's':char_object.str_s(), 't':char_object.str_t(),
                     'u':char_object.str_u(), 'v':char_object.str_v(), 'w':char_object.str_w(), 'x':char_object.str_x(),
                     'y':char_object.str_y(), 'z':char_object.str_z(), '!':char_object.str_love(), '?':None, '.':None, ':':None, '<':None,
                     ' ':char_object.str_space(), '>':None, '(':None, ')':None, '*':None}


###------------------------------------------------------------------
calendar = np.zeros(shape = (7, 53))
dates_calendar = np.chararray(shape = (7, 53))
days_list = get_days()

###------------------------------------------------------------------
# To find the total number of columns for given input string
for char in args.input.lower():
    char_matrix = fundamental_chars[char]
    columns = char_matrix.shape[1]  # number of column of the character
    sum_of_word_columns += columns  # summation of the required columns
"""
total columns: 53 (see the GitHub calendar)
we disregard 3 columns due to Vacations from the first and last weeks (columns) 
"""
if sum_of_word_columns > 50:  
    print("Ooops! Your words are too long!")
else:
    calendar_column_index = 1
    previous_column = 0
    for i, char in enumerate(args.input.lower()):
        char_matrix = fundamental_chars[char]
        #print(char_matrix)
        char_column = char_matrix.shape[1]
        calendar_column_index += char_column
        #print(f"i: {i}, previous_column: {previous_column}, cal_index: {calendar_column_index}")
        if i == 0:
            calendar[:, 1 : char_column+1] = char_matrix
        else:
            calendar[:, previous_column : calendar_column_index] = char_matrix
        previous_column = calendar_column_index       

###------------------------------------------------------------------
for column in range(num_calendar_column):
    for row in range(num_calendar_row):
        if column == 0 and row <= 4: # skip 5 first days of the calendar same as GitHub calendar
            pass
        else:
            if counter < len(days_list):
                if calendar[row][column] == 1:
                    output_days.append(days_list[counter])
                    e = Entry(root, width=2, bg='green') 
                    e.grid(row=row, column=column) 
                    e.insert(END, "")
                else:
                    e = Entry(root, width=2, bg='white') 
                    e.grid(row=row, column=column) 
                    e.insert(END, "")
                    
            counter += 1
                   
###------------------------------------------------------------------
if args.mode == 'p':
    root.mainloop()   
else:
    with open('days_output.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter="\n")
        wr.writerow(output_days)
    
























