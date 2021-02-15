# -*- coding: utf-8 -*-
"""
Created on Sun Oct 28 21:26:47 2018

@author: Mahnoor
"""



''' 
This function checks if the party's HP is less than 0 

@arg isPartyDead is the function 
@arg partyHP is the health of the party

'''
def isPartyDead(partyHP): 
    if partyHP[0] <= 0 and partyHP[1] <= 0 and partyHP[2] <= 0: 
        return True
    else:
        return False
''' 
This function checks if the party member is dead

@arg isDead is the function 
@arg partyHP is the health of the party 
@arg index selects the actual party member. Eg 0 = Krogg, 1 = Glinda, 2 = Geoffrey

'''       
def isDead(partyHP, index): 
    if partyHP[index] <= 0: 
        return True
    else:
        return False 

partyNames = ['Krogg','Glinda','Geoffrey']
partyHP = [180,120,150] 
partyAttack = [20,5,15]
partyDefense = [20,20,15] 


bossAttack = 25
bossDefense = 15
bossHP = 500 

round = 0

        
while bossHP >= 0 or isPartyDead(partyHP) == True: 
    round = round + 1
    print('') 
    print ("Round", round) 
    
    # if krogg isnt dead, then krogg attacks, but if he is dead, he does nothing
    if isDead(partyHP, 0) == False: 
        damage1 = partyAttack[0]-bossDefense 
        if damage1 < 0:
            damage1 = 0 
        bossHP = bossHP-damage1
        print ('Krogg does', damage1, ' points of damage to Boss')  
        
    # if Geoffrey isnt dead, then Geoffrey attacks, but if he is dead, he does nothing   
    if isDead(partyHP, 2) == False:
        damage2 = partyAttack[2]-bossDefense 
        if damage2 < 0:
            damage2 = 0 
        bossHP = bossHP-damage2
        print ('Geoffrey does', damage2, ' points of damage to Boss')          
        
    # if Glinda isnt dead, then Glinda heals Korgg and Geoffrey, but if she is dead, she does nothing 
    if isDead(partyHP, 1) == False:
        for i in range(len(partyHP)):
            if isDead(partyHP, i) == False:
                damage3 = partyAttack[1]
                partyHP[i] = partyHP[i] + damage3 
                print(partyNames[1], "heals", partyNames[i], "5 HP")
     # if the party members are not dead then the boss attacks each one, if boss is dead he does nothing and if characters are dead they dont get attacked   
    for a in range(len(partyHP)):
        if isDead(partyHP, a) == False:
            damage4 = bossAttack - partyDefense[a]
            partyHP[a] = partyHP[a] - damage4 
            print("Boss does", damage4, "points of damage to", partyNames[a])
       
        
 #updates the health of all the characters       
    
print('Boss: ', bossHP)
print('Krogg: ', partyHP[0]) 
print('Glinda: ', partyHP[1])
print('Geoffrey: ', partyHP[2])
   

        
        
        
    