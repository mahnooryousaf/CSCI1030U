# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 17:37:15 2018

@author: Mahnoor
"""

class Character: 
    def __init__(self, name, hp, maxhp, attack, defense, magic): 
        self.name = name   
        self.hp = hp
        self.maxhp = maxhp 
        self.attackpower = attack
        self.defensepower = defense 
        self.magic = magic 
    
    def __str__(self): 
        return str(self.name)
        
    def isdead(self): 
        if self.hp <= 0: 
            return True 
        else:
            return False 
            
    def attack(self, otherCharacter): 
        if otherCharacter.hp > 0 and self.hp > 0: 
            damage = self.attackpower - otherCharacter.defensepower
            otherCharacter.hp = otherCharacter.hp - damage
            print (self.name, " does ", damage, " points of damage to ", otherCharacter)
        else: 
            print (self.name, "cannot attack", otherCharacter.name, "because he/she is dead")
        
    def heal(self, party): 
        if self.hp > 0: 
            for i in range(len(party)):
                if party[i].hp > 0:
                    healing = self.magic
                    party[i].hp = party[i].hp + healing 
                    print(self.name, "heals 5 hp for", party[i])
                if party[i].hp > party[i].maxhp: 
                    party[i].hp = party[i].maxhp

''' 
This function checks if the party's HP is less than 0 

@arg isPartyDead is the function 
@arg partyHP is the health of the party

'''
def isPartyDead(partyHP): 
    if (partyHP == 0): 
        return True
    else:
        return False

krogg = Character('Krogg', 180, 180, 20, 20, 0)
glinda = Character('Glinda', 120, 120, 5, 20, 5)
geoffrey = Character('Geoffrey', 150,150, 15, 15,0)
party = [krogg, glinda, geoffrey]
boss = Character('Boss', 500, 500, 25, 15, 0)
round = 1
while (not boss.isdead()) and (not isPartyDead(party)): 
    print ('Round', round) 
    
    #krogg attacks 
    krogg.attack(boss) 
    
    #geoffrey attacks 
    geoffrey.attack(boss) 
    
    #glinda heals 
    glinda.heal(party) 
    
        
    #boss attacks 
    for partyMember in party: 
        boss.attack(partyMember) 
        
    #show progress 
    for partyMember in party: 
        print(partyMember.name, "has", partyMember.hp, "HP") 
    print(boss.name, "has", boss.hp, "HP")
    print('')
    
    round += 1 
1

if isPartyDead(party): 
    print('Your whole party id dead. You lose.') 
elif boss.isdead(): 
    print('The boss is dead. You are victorious!')
    
    
    
    