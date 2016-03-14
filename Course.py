__author__ = 'tpl'

import math
import copy

C_COORDINATES = {'Linguistics': [-80, 0, 0], 'Natural Sciences (Biological)': [70, -100, 0], 'Land Economy': [0, 0, 0],
       'History of Art': [-100, 0, -50], 'Music': [-70, 0, 0], 'Medicine': [50, -70, 0], 'Mathematics': [100, 70, 0],
       'Veterinary Medicine': [50, -70, 0], 'Classics': [-100, 0, -50], 'Philosophy': [-100, 0, -50],
       'Human Social and Political Sciences': [-100, 0, 0], 'Asian and Middle Eastern Studies': [-100, 0, -50],
       'Computer Science': [70, 80, 0], 'Law': [20, 0, 0], 'Economics': [-70, 30, 0],
       'Management Studies (Part II course)': [-70, 0, 0], 'Modern and Medieval Languages': [-100, 0, -50],
       'Anglo-Saxon Norse and Celtic': [-100, 0, -50], 'Theology and Religious Studies': [-100, 0, -50],
       'Medicine (Graduate course)': [100, 70, 0], 'Natural Sciences (Physical)': [70, 100, 0],
       'Architecture': [20, 20, 0], 'English': [-80, 0, 0], 'Chemical Engineering (via NatSci)': [50, 60, 0],
       'History': [-70, 0, -20], 'Chemical Engineering (via Eng)': [50, 60, 0],
       'Manufacturing Engineering (Part II course)': [50, 60, 0],
       'Psychological and Behavioural Sciences': [-30, -30, 0], 'Engineering': [50, 60, 0], 'Education': [-70, 0, 0],
       'Geography': [-70, 30, 0]}

def distance3D(coords1, coords2):
    x = coords1[0] - coords2[0]
    y = coords1[1] - coords2[1]
    z = coords1[2] = coords2[2]

    return math.sqrt(x**2 + y**2 + z**2)

def _pairwisedistance():
    C_COORDINATES2 = copy.deepcopy(C_COORDINATES)
    acc_distance = 0
    max = 0
    for (course1, coords1) in C_COORDINATES.items():
        for (course2, coords2) in C_COORDINATES2.items():
            displace = distance3D(coords1,coords2)
            if displace>max:
                max = displace
            acc_distance += displace
        C_COORDINATES2.pop(course1)
    average_distance = 2*acc_distance / len(C_COORDINATES)**2

    return (average_distance,max)

(AVERAGE, MAX) = _pairwisedistance()
