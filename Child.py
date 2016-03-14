__author__ = 'tpl'

from random import shuffle
import csv

class Child(object):
    def __init__(self, name, college, course):
        self.name = name
        self.college = college
        self.course = course
    def generate_couple_ranks(self,couple_list):
        copy = couple_list[:]
        shuffle(copy)
        self.couple_ranks = copy
        print self.couple_ranks

with open('fresher.csv', mode='r') as infile:
    reader = csv.reader(infile)
    CHILDREN = []
    for name, gender, college, course in reader:
        c = Child(name, college, course)
        CHILDREN.append(c)
