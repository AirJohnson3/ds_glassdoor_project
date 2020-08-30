# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:55:38 2020

@author: Micha
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Micha/Documents/GitHub/Glassdoor_Project/chromedriver.exe"

df = gs.get_jobs('data scientist', 1000, False, path, 5)

df.to_csv('glassdoor_jobs.csv', index = False)