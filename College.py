__author__ = 'tpl'
import math

COORDINATES = {'Sidney Sussex': [52.207222222222, 0.12027777777778], "St John's": [52.208055555556, 0.11666666666667],
       'Pembroke': [52.2017, 0.1192], 'Hughes Hall': [52.20082, 0.13287], 'Fitzwilliam': [52.21447, 0.10489],
       "King's": [52.204166666667, 0.11666666666667], 'Darwin': [52.200555555556, 0.11361111111111],
       'Trinity': [52.206944444444, 0.11694444444444], 'Wolfson': [52.198349, 0.100914],
       'Trinity Hall': [52.2057, 0.1155], 'Corpus Christi': [52.20287, 0.11821], 'Clare Hall': [52.205139, 0.103926],
       "St Catharine's": [52.203, 0.1169], "Christ's": [52.205398, 0.122223], 'Downing': [52.200623, 0.123842],
       'Girton': [52.2286, 0.083939], 'Newnham': [52.20022, 0.10727], 'Murray Edwards': [52.214188, 0.10856],
       'Selwyn': [52.200833333333, 0.10555555555556], "Queens'": [52.202222222222, 0.11472222222222],
       'Gonville and Caius': [52.205878, 0.117867], 'Magdalene': [52.210277777778, 0.11611111111111],
       'Lucy Cavendish': [52.211111111111, 0.11027777777778], 'Clare': [52.205083333333, 0.11519444444444],
       'Homerton': [52.1864, 0.1366], 'Emmanuel': [52.203611111111, 0.12397222222222],
       'Jesus': [52.209097222222, 0.1234], 'Peterhouse': [52.2009, 0.1184],
       'Robinson': [52.204722222222, 0.10527777777778], "St Edmund's": [52.212943, 0.108675], 'Churchill': [52.212746,0.104020]}

def distance2D(coords1, coords2):
    x = (coords1[0] - coords2[0])*0.6129070536529765
    y = coords1[1] - coords2[1]
    return math.sqrt(x**2+y**2)

GIRTONTOHOMERTON = distance2D(COORDINATES['Girton'], COORDINATES['Homerton'])
# #WOLFSON
# print distance2D([52.198349, 0.100914],[52.212943, 0.108675])
# #MEDWARDS
# print distance2D([52.214188, 0.10856],[52.212943, 0.108675])
