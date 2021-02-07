# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 22:18:11 2021

@author: Amir
"""
from datetime import timedelta, date

def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)

def get_days():
    start_date = date(2021, 1, 1)
    end_date = date(2021, 12, 31)
    return [single_date.strftime("%Y-%m-%d") for single_date in daterange(start_date, end_date)]