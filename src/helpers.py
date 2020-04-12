# -*- coding: utf-8 -*-

import os
import csv
import sys
import json
import time
import random
import fileinput
import zipfile

""" 
	Initially created April 12, 2020
	@author: Evan Thompson [navetoocool]

"""

##--Vars---##


##--Functions--##










##--Helper-Functions--##
def transform_data_return_str(input_data, input_data_type, output_data_type):
    return_str = ""
    if input_data_type == "csv":
        if output_data_type == "tsv":
            return_str = swap_delimiters(input_data, ",", "\t")
    elif input_data_type == "tsv":
        if output_data_type == "csv":
            return_str = swap_delimiters(input_data, "\t", ",")
    elif input_data_type == "json":
        pass
    elif input_data_type == "xml":
        pass
    elif input_data_type == "txt":
        pass
    return return_str


def swap_delimiters(input_data, input_delim, output_delim):
    output = ""
    with open(input_data, 'U') as file:
        for line in file:
            output += line.replace(input_delim, output_delim)

    return output