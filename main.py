__author__ = 'tpl'

import csv
from SRA import stable_roommate_algo
from Parent import Parent, Couple, SpousePreference
from Child import Child
from SMA import matchmaker

with open('parents.csv', mode='r') as infile:
    reader = csv.reader(infile)
    PARENTS = []
    for name, gender, course, college in reader:
        p = Parent(name, gender, college, course)
        p.set_spouse_preference('Opposite','Close','Close')
        p.set_child_preference('Close','Close')
        PARENTS.append(p)

# check that we have even number of parents
if len(PARENTS)%2 != 0:
    PARENTS.pop()

# STEP 0: generate perference ranks
SPOUSE_preference = {}
for p in PARENTS:
    p.generate_spouse_ranks(PARENTS)
    SPOUSE_preference[p] = p.spouse_ranks

SPOUSE_matching = stable_roommate_algo(SPOUSE_preference)

CoupleList = []
for k,v in SPOUSE_matching.items():
    CoupleList.append(Couple(k,v[0]))


CHILDREN = []

with open('freshers.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for name, gender, college, course in reader:
        c = Child(name, college, course)
        CHILDREN.append(c)

# generate ranks
CHILD_preference = {}
for cou in CoupleList:
    cou.generate_child_ranks(CHILDREN)
    CHILD_preference[cou] = cou.child_ranks

PARENT_Preference = {}
for child in CHILDREN:
    child.generate_couple_ranks(CoupleList)
    PARENT_Preference[child] = child.couple_ranks



MMatching = matchmaker(CHILD_preference,PARENT_Preference)

for couple, child in MMatching.items():
    print (couple.name, child.name)
