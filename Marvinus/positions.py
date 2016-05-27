# -*- coding: utf-8 -*-
"""
Created on Thu May 19 12:03:07 2016

@author: Gast1
"""


positions_left = {}
positions_right = {}




positions_left['C'] = [[0.9801840782165527, 0.7454819679260254, -1.5371098518371582, -0.5782761573791504, 1.3529460430145264, 0.9139999747276306],[0.9817180633544922, 0.7500841617584229, -1.5355758666992188, -0.5782761573791504, 0.9663779735565186, 0.9139999747276306]]
positions_left['D'] = [[0.951038122177124, 0.6887240409851074, -1.4404678344726562, -0.5936160087585449, 1.2885180711746216, 0.9139999747276306],[0.9541060924530029, 0.6963939666748047, -1.4404678344726562, -0.590548038482666, 0.9341640472412109, 0.9139999747276306]]
positions_left['E'] = [[0.8804740905761719, 0.610490083694458, -1.3837099075317383, -0.5966839790344238, 1.345276117324829, 0.9139999747276306],[0.877406120300293, 0.6181600093841553, -1.3852438926696777, -0.5936160087585449, 0.98785400390625, 0.9143999814987183]]
positions_left['F'] = [[0.7838320732116699, 0.5153820514678955, -1.3269519805908203, -0.5982179641723633, 1.4557241201400757, 0.9143999814987183],[0.7838320732116699, 0.5322561264038086, -1.3300199508666992, -0.5890140533447266, 1.0737581253051758, 0.9139999747276306]]


positions_right['G'] = []
positions_right['A'] = []
positions_right['B'] = []
positions_right['Ch'] = []

positions = {
    'LArm': positions_left,
    'RArm': positions_right
}


keys = {
    'position': positions
}

default_positions = {
    'LArm': [0.9356980323791504, 0.6825881004333496, -1.392913818359375, -0.5629360675811768, 0.98785400390625, 0.9143999814987183],
    'RArm': []
}



defaults = {
    'position': default_positions
}


def get_default_position(key):
    arm = key #'LArm' if key in positions_left else 'RArm'
    return arm, defaults['position'][arm]


def get_position(key):
    arm = 'LArm' if key in positions_left else 'RArm'
    return arm, keys['position'][arm][key],defaults['position'][arm]
    
