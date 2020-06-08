# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 15:22:51 2020

@author: saikat
"""


import glassdoor_scraper as gs 
import pandas as pd 

path = "F:\Learningvideos\Data Science POC\PythonCodes\chromedriver\chromedriver.exe"

df = gs.get_jobs('data scientist',10, False, path, 10)

df.to_csv('glassdoor_jobs.csv', index = False)