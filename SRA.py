__author__ = 'tpl'
import copy
# Get test data
# a list of parent objects

# import csv
# from Parent import Parent, Couple, SpousePreference
# with open('Parents.csv', mode='r') as infile:
#     reader = csv.reader(infile)
#     PARENTS = []
#     for name, gender, course, college in reader:
#         p = Parent(name, gender, college, course)
#         p.set_child_preference('Close','Close')
#         PARENTS.append(p)
#
# # check that we have even number of parents
# if len(PARENTS)%2 != 0:
#     PARENTS.pop()
#
# # STEP 0: generate perference ranks
# for p in PARENTS:
#     p.generate_spouse_ranks(PARENTS)
#     print p.spouse_ranks
# # STEP 1: Make initial proposa


# CORE Stable Roommate Algorithm

# preferences = {
#     'a' : ['c','d','f','e','b'],
#     'b' : ['f','a','e','c','d'],
#     'c' : ['d','f','a','b','e'],
#     'd' : ['a','e','f','b','c'],
#     'e' : ['a','f','d','c','b'],
#     'f' : ['c','b','d','a','e']
# }

# preferences = {
#     'R' : ['P','B','O','T','G'],
#     'P' : ['O','G','R','B','T'],
#     'B' : ['O','T','P','R','G'],
#     'G' : ['R','B','T','P','O'],
#     'O' : ['R','P','G','T','B'],
#     'T' : ['P','R','G','B','O']
# }

# STEP 1: Initial Proposal

def _make_proposal(proposer, preferences, proposals, inverse_proposal):

    # get the preferences of the proposer in question
    proposer_list = preferences[proposer]
    # who is his first choise
    receiver = proposer_list[0]
    if receiver in inverse_proposal:
        # get rank of the two proposers
        receiver_preferencelist = preferences[receiver]
        old_proposer = inverse_proposal[receiver]
        if receiver_preferencelist.index(proposer)<receiver_preferencelist.index(old_proposer):
            # proposer succeeds! old proposer is displaced
            proposals[proposer] = receiver
            inverse_proposal[receiver] = proposer
            assert preferences[old_proposer][0] == receiver
            # old proposer tries his next choice
            preferences[old_proposer].pop(0)
            _make_proposal(old_proposer,preferences, proposals,inverse_proposal)
        else:
            # proposer tries his second choice
            preferences[proposer].pop(0)
            _make_proposal(proposer,preferences, proposals,inverse_proposal)
    else:
        proposals[proposer] = receiver
        inverse_proposal[receiver] = proposer
    return (proposals, inverse_proposal)

def _init_proposal(preferences):
    proposals = {}
    inverse_proposal = {}
    for (proposer,proposer_list) in preferences.items():
        # for each person, update the proposal and inverse proposal tables
        (proposals, inverse_proposal) = _make_proposal(proposer, preferences, proposals,inverse_proposal)
    return proposals

def _build_reducedlist(preferences, proposals):
    # STEP 2: Construct a reduced list
    reduced_list = preferences.copy()
    for (p,q) in proposals.items():
        index = reduced_list[q].index(p)
        for i in range(index+1,len(reduced_list[q])):
            list = reduced_list[q]
            toberejected = reduced_list[q][i]
            try:
                reduced_list[toberejected].remove(q)
            except ValueError:
                pass
        reduced_list[q] = reduced_list[q][:index+1]
    return reduced_list

def _gotduplicate(a):
    b = a[:]
    while b:
        for i in range(1,len(b)):
            if b[0] ==b[i]:
                return True
        b = b[1:]
    return False

def _finalize(reduced_list):
    p = []
    q = []
    # find starting point
    person = None
    person_list = None
    for (k,v) in reduced_list.items():
        if len(v)>1:
            person = k
            person_list = v
            p.append(k)
            q.append(v[1])
            break

    if p:
        while not _gotduplicate(p):
            lastq = q[-1]
            newp = reduced_list[lastq][-1]
            p.append(newp)
            newq = reduced_list[newp][1]
            q.append(newq)

        p.pop()
        q.pop()
        # cancelling
        for i in range(len(p)-1):
            a = q[i]
            b = p[i+1]
            reduced_list[q[i]].remove(p[i+1])
            reduced_list[p[i+1]].remove(q[i])
    return reduced_list


def stable_roommate_algo(preference):
    proposals = _init_proposal(preference)
    rl = _build_reducedlist(preference,proposals)
    pairing = _finalize(rl)
    return pairing

# print stable_roommate_algo(preferences)