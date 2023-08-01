# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 13:48:08 2023

@author: clark
"""
import os
import textract
import string

def is_uppercase_alphanumeric(s):
    allowed_chars = string.ascii_uppercase + string.digits + string.punctuation
    for c in s:
        if c not in allowed_chars:
            return False
    return True


os.chdir(r"C:\Users\clark\OneDrive - Stony Brook University\Documents\MS Thesis")

thesis_txt = textract.process("New_Thesis_template-MS_2022_working_copy.docx")
thesis_txt = str(thesis_txt)

def find_matching_parentheses(s):
    stack = []
    matches = []
    for i, c in enumerate(s):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if not stack:
                # No open parenthesis on the stack to match the close parenthesis
                return None
            else:
                start = stack.pop()
                matches.append((start, i))
    if stack:
        # There are open parentheses on the stack with no matching close parentheses
        return None
    else:
        return matches


def check_for_abbreviations(s, match_list):
    abbreviations = []
    for i, j in match_list:
        sub_string = s[i+1: j]
        if is_uppercase_alphanumeric(sub_string):
            abbreviations.append(sub_string)
        
    return abbreviations
        

matches = find_matching_parentheses(thesis_txt)
print(check_for_abbreviations(thesis_txt, matches))