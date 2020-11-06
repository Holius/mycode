#!/usr/bin/env python3
#Author: RZFeeser RZFeeser@alta3.com

"""Script to search for a pattern match"""

import os # used to walk the system
import fnmatch # for regex pattern matching
import argparse

parser = argparse.ArgumentParser(description="Search for some stuff")

#EXCLUDE = ["/usr", "/home", "/var"] ## Dont search in these locations
EXCLUDE = []

def find(args):
    print(parser)
    """search through filesystem based on given path location"""
    pattern, path = args 
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name.lower(), pattern.lower()): # if match
                result.append(os.path.join(root, name)) # add to our list
    return result # return the list

def main():
    """runtime code"""
    
    print("Results: ", find(parser)) # call function

main()

