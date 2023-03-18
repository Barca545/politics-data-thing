import statistics
import pandas as pd

#https://realpython.com/python-statistics/ 
class district:
    def __init__(self,dem,rep,incumb_pty,trnout:list):
        self.dem = dem
        self.rep = rep
        self.incumb_pty = incumb_pty
        self.trnout = trnout
        self.avgtrnout = statistics.mean(trnout)
        self.trnout_stdev = statistics.stdev(trnout)
    
    def dlean(pty1,pty2):
        dlean = pty1 - pty2
        return dlean 


class demographics(district):
    def __init__(self, dem, rep, incumb_pty, trnout: list):
        super().__init__(dem, rep, incumb_pty, trnout)
        self.race = dict
        self.education = dict
        self.age = dict
        self.gender = dict 
    def set_race(self,black,white,asian,blackhis,blacknohis,whitehis,whitenohis,hispanic=False,other=None):
        self.race['asian'] = asian
        def other_race():
            if other is not None:
                self.race['other'] = other
                return self.race
            else:
                return
        other_race()        
        if hispanic is False:
            races = {'black':black,'white':white}
            for key,value in races:
                self.race[key] = value
        else:
            black_total = sum(blackhis,blacknohis)
            white_total = sum(whitehis,whitenohis)
            races = {
                'black':black_total,
                'hispanic black':blackhis,
                'non hispanic black':blacknohis,
                'white':white_total,
                'hispanic white':whitehis,
                'non hispanic white':whitenohis
                }
            for key,value in races:
                self.race[key] = value
        return self.race
    def set_education(self,no_college,college,grad):
        self.education = {
            'non college':no_college,
            'college':college,
            'grad school':grad
            }
        return self.education    
    def set_age(self,youth,young_adult,middle_age,senior):
        self.age = {'18-29':youth,'30-44':young_adult,'45-64':middle_age,'65+':senior}
    def set_gender(self,men,woman,other=None):
        genders = {'men':men,'woman':woman}
        for key,value in genders:
            self.gender[key] = value
        if other is not None: 
            self.gender['other'] = other
        return self.gender
    #def mk_crsstb (self,trait_1,trait_2):
        #https://pbpython.com/pandas-crosstab.html

