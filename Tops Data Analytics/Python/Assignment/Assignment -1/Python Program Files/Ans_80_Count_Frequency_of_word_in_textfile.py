# 81) Write a Python program to write a list to a file and then read it back.

def write_list_to_file(filename, my_list):
    """Writes each item of the list to a file, one item per line."""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in my_list:
                file.write(item + '\n')
        print(f"\n✅ List has been successfully written to '{filename}'")
    except Exception as e:
        print(f"⚠️ Error while writing to file: {e}")

def read_file(filename):
    """Reads and prints the content of the given file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print(f"\n📄 Contents of '{filename}':")
            print("-" * 40)
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"❌ File '{filename}' not found.")
    except Exception as e:
        print(f"⚠️ Error while reading the file: {e}")

# Main Program
# Step 1: Take user input for the filename
filename = input("Enter the filename (e.g., mylist.txt): ")

# Step 2: Create a list to write (you can modify or ask user to input)
my_list = ["Python", "is", "fun", "to", "learn"]

# Step 3: Write the list to the file
write_list_to_file(filename, my_list)

# Step 4: Read and display the file content
read_file(filename)


# ====================================================================================================================================
# ====================================================================================================================================

# Sample Output:

# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> & "C:\Program Files\Python313\python.exe" "c:/Users/Gopani/Downloads/Tops demo/Tops Data Analytics/Python/Assignment/Assignment -1/Python Program Files/Ans_80_Count_Frequency_of_word_in_textfile.py"
# Enter the filename with full path (e.g., C:/Users/YourName/Desktop/myfile.txt): C:\Users\Gopani\Desktop\Python Testing.txt  

# 📊 Word Frequencies:
# 🔹: 7
# 1: 1
# introduction: 1
# if: 3
# you’ve: 2
# worked: 1
# with: 7
# microsoft: 2
# excel: 10
# likely: 1
# come: 1
# across: 1
# the: 6
# terms: 1
# macros: 8
# and: 14
# vba: 16
# while: 1
# many: 1
# people: 1
# use: 8
# them: 1
# interchangeably: 1
# they: 2
# are: 6
# not: 3
# same: 2
# in: 7
# this: 2
# article: 1
# we: 1
# will: 2
# explore: 1
# what: 3
# actually: 1
# how: 1
# differ: 1
# when: 4
# it: 4
# is: 5
# appropriate: 1
# to: 20
# one: 2
# over: 1
# other: 4
# real-world: 1
# scenarios: 1
# guide: 1
# your: 5
# choice: 5
# 2: 1
# a: 11
# macro: 8
# recorded: 2
# sequence: 1
# of: 4
# actions: 3
# performed: 1
# allows: 1
# users: 2
# automate: 3
# repetitive: 2
# tasks: 4
# without: 2
# writing: 2
# any: 1
# code: 5
# 📌: 2
# example: 2
# suppose: 1
# you: 15
# regularly: 1
# format: 1
# report: 2
# by: 1
# bolding: 1
# headers: 1
# applying: 2
# filters: 1
# aligning: 1
# text: 1
# instead: 1
# doing: 1
# manually: 1
# each: 3
# time: 2
# can: 4
# record: 3
# once: 1
# reuse: 1
# single: 1
# click: 1
# ✅: 4
# ideal: 2
# for: 6
# basic: 4
# automation: 2
# that: 3
# do: 1
# require: 1
# custom: 6
# logic: 4
# 3: 1
# visual: 2
# applications: 4
# programming: 2
# language: 1
# built: 1
# into: 2
# office: 3
# including: 1
# enables: 1
# write: 2
# controls: 1
# excel’s: 1
# behavior: 2
# providing: 1
# far: 1
# more: 2
# flexibility: 2
# than: 1
# alone: 1
# implement: 1
# logical: 1
# conditions: 1
# loops: 2
# functions: 1
# even: 1
# interact: 2
# such: 1
# as: 2
# outlook: 2
# or: 6
# word: 1
# want: 3
# scan: 1
# hundreds: 1
# rows: 2
# identify: 1
# empty: 2
# cells: 1
# send: 1
# an: 1
# email: 1
# alert: 1
# —: 2
# would: 1
# need: 3
# advanced: 1
# workflows: 1
# complex: 3
# data: 2
# operations: 2
# 4: 1
# key: 1
# differences: 1
# vs: 1
# feature: 1
# ease: 1
# simple: 3
# –: 1
# no: 1
# coding: 1
# required: 1
# requires: 3
# knowledge: 1
# limited: 1
# full: 1
# control: 1
# functionality: 1
# good: 1
# suitable: 1
# editing: 1
# hard: 1
# modify: 1
# easily: 1
# editable: 1
# editor: 2
# integration: 2
# only: 1
# apps: 1
# 5: 1
# should: 1
# comfortable: 1
# quick: 1
# solution: 1
# much: 1
# complexity: 1
# task: 5
# conditional: 3
# build: 2
# forms: 1
# tools: 2
# interactions: 1
# between: 1
# aim: 1
# scalable: 2
# reusable: 1
# solutions: 2
# 6: 1
# real-life: 1
# cases: 1
# formatting: 1
# monthly: 1
# best: 4
# reason: 4
# repeatable: 1
# sending: 1
# emails: 1
# content: 1
# from: 1
# hiding: 1
# based: 1
# on: 1
# specific: 1
# criteria: 1
# needed: 1
# combining: 1
# multiple: 1
# files: 2
# involves: 1
# looping: 1
# through: 1
# 7: 1
# getting: 1
# started: 1
# go: 2
# view: 1
# →: 3
# developer: 1
# press: 1
# alt: 1
# +: 1
# f11: 1
# 🏁: 1
# 8: 1
# conclusion: 1
# both: 1
# powerful: 1
# save: 1
# improve: 1
# efficiency: 1
# just: 1
# starting: 1
# out: 1
# great: 1
# entry: 1
# point: 1
# become: 1
# learning: 1
# allow: 1
# create: 1
# highly: 1
# customized: 1
# 🔔: 1
# call: 1
# action: 1
# have: 1
# used: 1
# work: 1
# share: 1
# experience: 1
# ask: 1
# questions: 1
# comments: 1
# i’d: 1
# be: 1
# happy: 1
# help: 1
# PS C:\Users\Gopani\Downloads\Microsoft VS Code\vsapp> 

# =====================================================================================================================================
# =====================================================================================================================================