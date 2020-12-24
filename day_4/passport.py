""" Module representing a passport """

from dataclasses import dataclass

class Passport:
    def __init__(self, values):
        self.hgt = values.get('hgt', None)
        self.hcl = values.get('hcl', None) 
        self.ecl = values.get('ecl', None) 
        self.byr = values.get('byr', None) 
        self.iyr = values.get('iyr', None) 
        self.eyr = values.get('eyr', None) 
        self.pid = values.get('pid', None) 
        self.cid = values.get('cid', None) 

    # def __str__(self):
    #     return 'hgt', 'hcl', 'ecl', 'byr', 'iyr', 'eyr', 'pid', 'cid',
