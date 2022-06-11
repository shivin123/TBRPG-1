#start by running this cell
print('_______________________________________________________________________________________________________________________________')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('_______________________________________________________________________________________________________________________________')
print('')
print('')
print('')
print('New game started')
#random funtions & dice
import random
hp_add_list=[1,1,1,2,2,3]
dice=[1,2,3,4,5,6]
#Name generator
print('Welcome to:')
name_a =['golden', 'northern', 'southern', 'eastern', 'western', 'horid', 'high', 'blue', 'great', 'new', 'old', 'cargy', 'holy', 'green', 'frigid', 'infernial', 'white', 'little', 'red', 'lower', 'impenetrable', 'hospitable']
name_b =[' river', ' metropolis', ' cape', ' port', ' wood', ' fort', ' castle', ' bastion', ' fortress', ' jungle', ' town',' hamlet', ' keep', ' city', ' temple', ' mesa', ' coast', ' bay', ' brook', ' island', ' isle', ' peninsula', ' hill', ' valley', ' shore']
name_c =['sticks', 'apples', 'Johova', 'Satan', 'baskets', 'bats', 'mirrors', 'deer', 'chaos', 'dreams', 'Romans', 'gnomes', 'halibit', 'whores', 'snakes', 'basilisks', 'lions', 'lilies', 'Æbleskiver']
print(('The ')+(random.choice(name_a))+(random.choice(name_b))+(' of ')+(random.choice(name_c)))
print('')
print('')
print('')
print('_______________________________________________________________________________________________________________________________')
print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
print('_______________________________________________________________________________________________________________________________')

#set debug=1 to print debug logs while running
debug=1
#player stats
p_max_hp=10+random.choice(hp_add_list)
p_hp=p_max_hp
p_atk_b=6
p_def_b=2
p_hit_c=2
p_do=0
p_do_b=0
p_base_speed=0
level=1
p_xp=0
#player inventory
p_gold=400
my_ingot=0
tortle_shell=0
infernal_essence=0
#equiment reset
arm_equiped=0
wep_equiped=0
p_arm=0
p_do=0
p_wep=0
p_wep_rd=0
p_wep_fd=0
#misc var reset
atk_temp1=0
atk_temp2=0
atk_f_temp1=0
atk_f_temp2=0
enemy_alive=0
attack=0
in_combat=0
just_killed=0
e_base_speed_temp=0
p_atk_first=0
xp_gained=0
continue_fight=2
directory_val=0
attack=0
    
#D6 dice visual system
def dice_6_vis(dicex6):
    if dicex6 == 1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
    if dicex6 == 2:
        print('       ')
        print("[-----]")
        print("[ 0   ]")
        print("[     ]")
        print("[   0 ]")
        print("[-----]")
        print('       ')
    if dicex6 == 3:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[0 0 0]")
        print("[     ]")
        print("[-----]")
        print('       ')
    if dicex6 == 4:
        print('       ')
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print('       ')
    if dicex6 == 5:
        print('       ')
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print('       ')
    if dicex6 == 6:
        print('       ')
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print('       ')
        
#coin visual system
#1=heads/0=tails
def coin_vis(coin_vis_val):
    if coin_vis_val==1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  H  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
    if coin_vis_val==0:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  T  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
#
#enemy stats class info start
#
class enemy_stats:
    def __init__(self, givenName, givenID, givenArmE, givenWepE, e_max_hp, e_hp, e_speed, e_atk_b, e_def_b, e_hit_c, e_do, e_xp_r, e_gold_r, e_descr):
        self.name=givenName
        self.id=givenID
        self.e_arm_equiped=givenArmE
        self.e_wep_equiped=givenWepE
        self.e_max_hp=e_max_hp
        self.e_hp=e_hp
        self.e_speed=e_speed
        self.e_atk_b=e_atk_b
        self.e_def_b=e_def_b
        self.e_hit_c=e_hit_c
        self.e_do=e_do
        self.e_xp_r=e_xp_r
        self.e_gold_r=e_gold_r
        self.e_descr=e_descr
        
    def load_enemy_stats(self):
        temp_e_n=self.name
        temp_enc_n=self.id
        temp_e_arm_equiped=self.e_arm_equiped
        temp_e_wep_equiped=self.e_wep_equiped
        temp_e_mhp=self.e_max_hp
        temp_e_hp=self.e_hp
        temp_e_base_speed=self.e_speed
        temp_e_ab=self.e_atk_b
        temp_e_db=self.e_def_b
        temp_e_hc=self.e_hit_c
        temp_e_do=self.e_do
        temp_e_xpr=self.e_xp_r
        temp_e_gr=self.e_gold_r
        temp_e_descr=self.e_descr
        return(temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr)
        
    def display_enemy_stats(self):
        if self.e_arm_equiped>0:
            print('Is wearing ')
            print(self.e_arm_equiped)
        if self.e_wep_equiped>0:
            print('Is using a ')
            print(self.e_wep_equiped)
        print('HP:')
        print(self.e_hp)
        print('Base Speed:')
        print(self.e_speed)
        print('Base Attack:')
        print(self.e_atk_b)
        print('Base Defence:')
        print(self.e_def_b)
        print('Base Hit Chance:')
        print(self.e_hit_c)
        print('Base Dodge:')
        print(self.e_do)
        print('XP Reward:')
        print(self.e_xp_r)
        print('Gold Reward:')
        print(self.e_gold_r)

        
        
fox=enemy_stats('Fox', 1, 0, 0, 8, 8, 1, 2, 0, 2, 1, 5, 10, 'Foxes are small to medium-sized omnivorous animals, they are considered pests as they hunt small farm animals.') 
wolf=enemy_stats('Wolf', 2, 0, 0, 12, 12, 0, 5, 3, 2, 0, 15, 30, 'Wolves are medium-sized preadtors, they are known to roam large distances in search of food.')
lion=enemy_stats('Lion', 3, 0, 0, 18, 18, 0, 8, 5, 1, 0, 30, 60, 'Lions are strong with compact bodies and powerful forelegs, teeth and jaws for pulling down and killing prey.')
pard=enemy_stats('Pard', 4, 0, 0, 14, 14, 2, 12, 4, 2, 1, 75, 150, 'Pards are quick and agile hitting hard but are quite squishy themselfs.')
troll=enemy_stats('Troll', 5, 0, 0, 36, 36, -1, 14, 10, 1, 0, 125, 250, 'Trolls dwell in isolated areas of rocks, mountains, or caves, where they mine mythril to make idols to thier gods')

forest_gnome=enemy_stats('Forest gnome', 6, 0, 0, 18, 18, 1, 18, 12, 1, 1, 200, 400, 'Compared with other gnomes, forest gnomes are even more diminutive, rarely growing taller than 1m in height or weighing over 20 Kgs.')
#replace dire wolf and alpha lion with better enemies
dire_wolf=enemy_stats('Dire wolf', 7, 0, 0, 28, 28, 0, 20, 16, 1, 0, 300, 600, 'Dire wolfs are just larger wolfs.')
alpha_lion=enemy_stats('Alpha lion', 8, 0, 0, 34, 34, 0, 22, 20, 1, 0, 500, 1000, 'Alpha lions are just larger lions.')
tortle=enemy_stats('Tortle', 9, 0, 0, 50, 50, -2, 20, 26, 0, -1, 700, 1400, 'Tortles are larger bipeds that are similer to tortoises, they maybe slow and easy to hit but thier shell is quite hard to get through.')
infernal=enemy_stats('Infernal', 10, 0, 0, 40, 40, 1, 26, 22, -1, 0, 900, 1800, 'Infernals are large beasts with flameing fists and a quick strike.')

all_enemies=[fox, wolf, lion, pard, troll, forest_gnome, dire_wolf, alpha_lion, tortle, infernal]
#
#enemy stats class info end
#

#
#display enemy stats with modifiers start
#

def display_modif_enemy_stats(temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr):
        if temp_e_arm_equiped>0:
            print('Is wearing ')
            print(temp_e_arm_equiped)
        if temp_e_wep_equiped>0:
            print('Is using a ')
            print(temp_e_wep_equiped)
        print('HP:')
        print(temp_e_hp)
        print('Base Speed:')
        print(temp_e_base_speed)
        print('Base Attack:')
        print(temp_e_ab)
        print('Base Defence:')
        print(temp_e_db)
        print('Base Hit Chance:')
        print(temp_e_hc)
        print('Base Dodge:')
        print(temp_e_do)
        print('XP Reward:')
        print(temp_e_xpr)
        print('Gold Reward:')
        print(temp_e_gr)
#
#display enemy stats with modifiers end
#

#
#enemy type modifier info start
#
class enemy_modif_type_class:
    def __init__(self, givenName, givenID, givenArmE, givenWepE, e_max_hp, e_hp, e_speed, e_atk_b, e_def_b, e_hit_c, e_do, e_xp_r, e_gold_r, e_descr):
        self.modif_name=givenName
        self.modif_id=givenID
        self.modif_e_arm_equiped=givenArmE
        self.modif_e_wep_equiped=givenWepE
        self.modif_e_max_hp=e_max_hp
        self.modif_e_hp=e_hp
        self.modif_e_speed=e_speed
        self.modif_e_atk_b=e_atk_b
        self.modif_e_def_b=e_def_b
        self.modif_e_hit_c=e_hit_c
        self.modif_e_do=e_do
        self.modif_e_xp_r=e_xp_r
        self.modif_e_gold_r=e_gold_r
        self.modif_e_descr=e_descr
        
    def load_enemy_modif_stats(self):
        temp_modif_e_n=self.modif_name
        temp_modif_id=self.modif_id
        temp_modif_e_arm_equiped=self.modif_e_arm_equiped
        temp_modif_e_wep_equiped=self.modif_e_wep_equiped
        temp_modif_e_mhp=self.modif_e_max_hp
        temp_modif_e_hp=self.modif_e_hp
        temp_modif_e_base_speed=self.modif_e_speed
        temp_modif_e_ab=self.modif_e_atk_b
        temp_modif_e_db=self.modif_e_def_b
        temp_modif_e_hc=self.modif_e_hit_c
        temp_modif_e_do=self.modif_e_do
        temp_modif_e_xpr=self.modif_e_xp_r
        temp_modif_e_gr=self.modif_e_gold_r
        temp_modif_e_descr=self.modif_e_descr
        return(temp_modif_e_n, temp_modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr)

shiny=enemy_modif_type_class('Shiny ', 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 2, "It's just Shiny and color shifted, dispite this some idiot is sure to pay a pretty penny for it.")
golden=enemy_modif_type_class('Golden ', 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1.75, "It's just yellower than a normal one, dispite this some idiot is sure to pay a pretty penny for it.")
silver=enemy_modif_type_class('Silver ', 3, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1.5, "It's just a less colorful verison of a regular one, dispite this some idiot is sure to pay a pretty penny for it.")
large=enemy_modif_type_class('Large ', 4, 0, 0, 1.2, 1.2, -1, 0, 0, 0, 0, 1.1, 1, "It's larger than a normal one, definitely can take more of a beating.")
small=enemy_modif_type_class('Small ', 5, 0, 0, 0.8, 0.8, 1, 0, 0, 0, 1, 1.1, 1, "It's smaller than a normal one, as a result it is faster and harder to hit.")
rabid=enemy_modif_type_class('Rabid ', 6, 0, 0, 0.9, 0.9, 2, 2, 0, 0, -1, 1.2, 1, "It's drooling and mad with rage, it may bite hard but it's single minded focus makes it easy to hit.")
bony=enemy_modif_type_class('Bony ', 7, 0, 0, 1.2, 1.2, -1, 0, 2, 0, -1, 1.4, 1, "It's skin has been harden by an unknown affliction, it has been encumbered by its dermal ossification but is significantly tougher.")
intelligent=enemy_modif_type_class('Intelligent ', 8, 0, 0, 1, 1, 2, 2, 0, 1, 1, 1.5, 1, "It's surprising intelligent movements betray its nature, it has a much better command of tactics and isn't afraid of using it.")


all_enemy_modifiers=[shiny, golden, silver, large, small, rabid, bony, intelligent]

#
#armour stats class info start
#
class Armour_class:
    def __init__(self, givenName, givenID, givenEquiped, givenQuantity, givenArmVal, givenDoVal, givenFireRes, givenWeight, givenGoldCost, givenDescription):
        self.name=givenName
        self.id=givenID
        self.equiped=givenEquiped
        self.quant=givenQuantity
        self.arm_val=givenArmVal
        self.do_val=givenDoVal
        self.fire_res=givenFireRes
        self.weight=givenWeight
        self.gold_cost=givenGoldCost
        self.descr=givenDescription
        
    def buy_arm(self):
        if self.quant==0:
            self.quant=1
        
    def equip(self):
        if self.quant==1 and self.equiped==0:
            self.equiped=1
            
            
    def unequip(self):
        if self.quant==1 and self.equiped==1:
            self.equiped=0
            
    def display_stats(self):
        print(self.name)
        print(self.descr)
        print('Armour Value:')
        print(self.arm_val)
        print('Dodge Value:')
        print(self.do_val)
        print('Fire Resistance:')
        print(self.fire_res)
        print('Weight:')
        print(self.weight)
     
        
            
            
            
plain_clothes=Armour_class("Plain clothes", 1, 1, 1, 0, 1, -1, 2, 5, "Made from burlap and wool, it makes you look like a plebeian.")
leather_arm=Armour_class("Leather armor", 2, 0, 0, 1, 1, 0, 5, 40, "Made from tanned hides of various animals, it is relatively light and cheap.")
mail_arm=Armour_class("Mail armor", 3, 0, 0, 2, 0, 0, 10, 120, "Made from small metal rings linked together, it provides some protection without hindering movement.")
scale_arm=Armour_class('Scale armour', 4, 0, 0, 4, -1, 0, 20, 250, 'Made from many individual small armour scale, it is somewhat cumbersome but provides decent protection.')  
mythril_mail_arm=Armour_class('Mythril mail armour', 5, 0, 0, 4, 0, 0, 15, 500, 'Made from small mythril rings linked together, it is heavier than regular mail but provides better protection')
tortle_shell_arm=Armour_class('Tortle shell armour', 6, 0, 0, 8, -1, 0, 35, 2500, 'Made from the shell of endangered tortles, it is heavy and cumbersome but provides good protection.')
terracotta_arm=Armour_class('Terracotta armour', 7, 0, 0, 6, 0, 1, 20, 6000, 'Made from the fire hardened flesh of a clay golem, it provides a small degree of fire resistance.')

all_armour=[plain_clothes, leather_arm, mail_arm, scale_arm, mythril_mail_arm, tortle_shell_arm, terracotta_arm]
#
#armour stats class info end
#

#
#weapon stats class info start
#
class Weapon_class:
    def __init__(self, givenName, givenID, givenEquiped, givenQuantity, givenDamage, givenHitChance, givenRandomDamage, givenFireDamage, givenWeight, givenGoldCost, givenDescription):
        self.name=givenName
        self.id=givenID
        self.equiped=givenEquiped
        self.quant=givenQuantity
        self.damage_val=givenDamage
        self.wep_hit_c=givenHitChance
        self.r_damage_val=givenRandomDamage
        self.f_damage_val=givenFireDamage
        self.weight=givenWeight
        self.gold_cost=givenGoldCost
        self.descr=givenDescription
        
    def buy_wep(self):
        if self.quant==0:
            self.quant=1
        
    def equip(self):
        if self.quant==1 and self.equiped==0:
            self.equiped=1
            
            
    def unequip(self):
        if self.quant==1 and self.equiped==1:
            self.equiped=0
            
    def display_stats(self):
        print(self.name)
        print(self.descr)
        print('Damage:')
        print(self.damage_val)
        print('Hit Chance:')
        print(self.wep_hit_c)
        print('Random Damage:')
        print(self.r_damage_val)
        print('Fire Damage:')
        print(self.f_damage_val)
        print('Weight:')
        print(self.weight)
            
        
stick=Weapon_class('Stick', 1, 1, 1, 0, 0, 0, 0, 1, 0, 'A stick you found on the ground, with this at least no one considers you a threat.')
iron_dagger=Weapon_class('Iron dagger', 2, 0, 1, 0, -1, 1, 0, 2, 10, 'Made from a sliver of crudely wrought iron fastened to a stave, it is unlikely you will hit anything with this.')
iron_spear=Weapon_class('Iron spear', 3, 0, 0, 1, 0, 0, 0, 6, 40, 'Made from a shard of iron tied to a long pole, it keeps your enemies at a distance but not for long.')
iron_sword=Weapon_class('Iron sword', 4, 0, 0, 2, 0, 0, 0, 6, 100, 'Made from iron cast into a flat rod and sharpened on a wetstone, it gives your attacks a bit of bite.')
steel_sword=Weapon_class('Steel sword', 5, 0, 0, 4, 0, 0, 0, 6, 250, 'Made from steel by a real blacksmith, it is the cheapest professional weapon available.')
steel_kukri=Weapon_class('Steel kukri', 6, 0, 0, 3, 0, 1, 0, 8, 600, 'Made from recurved steel and a hardwood handle, it is curved to help clear brush and anything else that gets in your way.')
mythril_sabre=Weapon_class('Mythril sabre', 7, 0, 0, 2, 1, 2, 0, 6, 1500, 'Made from a magical mythril, it is supriseingly light for its size allowing you to hit your target with ease.')
fire_flail=Weapon_class('Fire flail', 8, 0, 0, 4, 0, 1, 1, 10, 4000, 'Made from regular steel but contains infernal essence in its head, it glows red hot and burns anything struck with it.')

all_weapons=[stick, iron_dagger, iron_spear, iron_sword, steel_sword, steel_kukri, mythril_sabre, fire_flail]
#
#weapon stats class info end
#

#
#Funtional code starts here
#
directory_val=0
while directory_val==0:
    print('_______________________________________________________________________________________________________________________________')
    print('')
    print('Main menu')
    print('')
    print('Enter 1 to go to equipment selection')
    print('Enter 2 to go to the shop')
    print('Enter 3 to go in to the wilds in search of enemies')
    print('Enter 4 to display stats')
    print('Enter 5 to heal up')
    print('')
    directory_val=int(input("Enter number here:"))
    if directory_val>5:
        print('You have entered an invalid number try again')
        directory_val=0
        
    #
    #Main Menu end
    #
    
    while directory_val==1:

        #
        #Equipment section system start
        #

        print('_____________________________________________________________________________________________________________________________')

        print('Enter 1 if you wish to equip a weapon')
        print('')
        print('Enter 2 if you wish to equip armour')
        print('')
        print('Enter 0 if you wish to exit the equipment selection section')
        print('')
        equip_section=int(input("Enter equip section number here:"))
        if equip_section>2:
            print('You have inputed an invalid number please try again')
            directory_val=1
            
        print('_____________________________________________________________________________________________________________________________')    

        #weapon equip section
        if equip_section==1:
            print('Enter the id number of the weapon you wish to equip')
            for e in all_weapons:
                if e.quant==1:
                    print('ID:')
                    print(e.id)
                    print('Name:')
                    print(e.name)

            for e in all_weapons:
                e.unequip()

            a=int(input("enter id "))
            x=all_weapons[(a-1)]
            print('')
            print('_______________________________________________________________________________________________________________________________')
            print('')
            x.display_stats()


            b=int(input("Enter 1 if you wish to equip, enter 0 if you do not "))
            print('_______________________________________________________________________________________________________________________________')
            if b==1:
                x.equip()
                p_wep=x.damage_val
                p_wep_hit_c=x.wep_hit_c
                p_wep_rd=x.r_damage_val
                p_wep_fd=x.f_damage_val
                p_wep_weight=x.weight
                print('    ')
                print(x.name)
                print('Equiped')

            else:
                print('You did not equip ')
                print(x.name)

        #armour equip section        
        if equip_section==2:
            print('Enter the id number of the armour you wish to equip')
            for e in all_armour:
                if e.quant==1:
                    print('ID:')
                    print(e.id)
                    print('Name:')
                    print(e.name)

            for e in all_armour:
                e.unequip()

            a=int(input("enter id "))
            x=all_armour[(a-1)]
            print('')
            print('_______________________________________________________________________________________________________________________________')
            print('')
            x.display_stats()


            b=int(input("Enter 1 if you wish to equip, enter 0 if you do not "))
            print('_______________________________________________________________________________________________________________________________')
            if b==1:
                x.equip()
                p_arm=x.arm_val
                p_do=x.do_val
                p_fire_res=x.fire_res
                p_arm_weight=x.weight
                print('    ')
                print(x.name)
                print('Equiped')

            else:
                print('You did not equip ')
                print(x.name)

        if equip_section==0:
            print('You leave equipment selection')

        directory_val=0

        print('_____________________________________________________________________________________________________________________________')

        #
        #Equipment section system end
        #  

    while directory_val==2:

        #
        #Shop system start
        #

        print('_____________________________________________________________________________________________________________________________')

        print('Enter 1 if you wish to buy weapons')
        print('')
        print('Enter 2 if you wish to buy armour')
        print('')
        print('Enter 0 if you wish to exit the shop')
        print('')
        shop_section=int(input("Enter shop number you wish to shop in "))
        if shop_section>2:
            print('You have inputed an invalid number please try again')
            directory_val=2
        #weapon section
        if shop_section==1:
            print('__________________________')
            print('Gold:')
            print(p_gold)
            for e in all_weapons:
                if e.quant==0:
                    print('ID:')
                    print(e.id)
                    print('Name:')
                    print(e.name)
                    print('Price:')
                    print(e.gold_cost)
                    print('__________________________')
                print('')
            wep_buy_id=int(input("Enter the id number of the weapon you wish to but "))
            wep_buy_id=all_weapons[(wep_buy_id)-1]
            wep_buy_id.display_stats()
            print('Price:')
            print(wep_buy_id.gold_cost)
            print('__________________________')
            b=int(input("Enter 1 if you wish to buy, enter 0 if you do not "))
            print('__________________________')
            if b==1:
                if p_gold>=wep_buy_id.gold_cost:
                    p_gold=p_gold-wep_buy_id.gold_cost
                    wep_buy_id.buy_wep()
                    print('You have bought a')
                    print(wep_buy_id.name)
                else:
                    print('You do not have enough gold')
            else:
                print('You did not buy:')
                print(wep_buy_id.name)
        #armour section
        if shop_section==2:
            print('__________________________')
            print('Gold:')
            print(p_gold)
            for e in all_armour:
                if e.quant==0:
                    print('ID:')
                    print(e.id)
                    print('Name:')
                    print(e.name)
                    print('Price:')
                    print(e.gold_cost)
                    print('__________________________')
                print('')
            arm_buy_id=int(input("Enter the id number of the armour you wish to but "))
            arm_buy_id=all_armour[(arm_buy_id)-1]
            arm_buy_id.display_stats()
            print('Price:')
            print(arm_buy_id.gold_cost)
            print('__________________________')
            b=int(input("Enter 1 if you wish to buy, enter 0 if you do not "))
            print('__________________________')
            if b==1:
                if p_gold>=arm_buy_id.gold_cost:
                    p_gold=p_gold-arm_buy_id.gold_cost
                    arm_buy_id.buy_arm()
                    print('You have bought a')
                    print(arm_buy_id.name)
                else:
                    print('You do not have enough gold')
            else:
                print('You did not buy:')
                print(arm_buy_id.name)

        if shop_section==1:
            print('You leave the shop')

        directory_val=0

        print('_____________________________________________________________________________________________________________________________')

        #
        #Shop system end
        #

    while directory_val==3:
        print('_____________________________________________________________________________________________________________________________')

        #
        #Encounter/combat/levelcheck start
        #   

        #
        #encount system + combat system start
        #

        #random encounter system
        continue_fight=2
        while continue_fight>0:
            if in_combat==0:
                if continue_fight==2:
                    print("Zones 1 and 2 exist as of now")
                    z_v=input('Enter zone number you wish to go to ')
                    z_v = int(z_v)
                print('_____________________________________________________________________________________________________________________________')

                rev=(random.choice(dice)+level-((z_v-1)*6))
                #rev print is for debug purpous
                if debug==1:
                    print('Random encounter vaule:')
                    print(rev)
                if rev<7:
                    enc_n=1
                if 6<rev<9:
                    enc_n=2
                if 8<rev<11:
                    enc_n=3
                if 10<rev<13:
                    enc_n=4
                if 12<rev:
                    enc_n=5
                if z_v==2:
                    if rev<7:
                        enc_n=6
                    if 6<rev<9:
                        enc_n=7
                    if 8<rev<11:
                        enc_n=8
                    if 10<rev<13:
                        enc_n=9
                    if 12<rev:
                        enc_n=10
                if debug==1:        
                    print('enc_n')
                    print(enc_n)

                a=enc_n        
                x=all_enemies[(a-1)]
                x.load_enemy_stats()
                enemy_modif_val=random.randint(1,1000)
                if debug==1:
                    print('enemy_modif_val:')
                    print(enemy_modif_val)
                #enemy_modif_val=86 #remove this /ie this is to test the system
                if enemy_modif_val<111:
                    if enemy_modif_val==1:
                        enemy_modif_type=1
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                    if enemy_modif_val>1 and enemy_modif_val<11:
                        enemy_modif_type=2
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                    if enemy_modif_val>10 and enemy_modif_val<31:
                        enemy_modif_type=3
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                    if enemy_modif_val>30 and enemy_modif_val<51:
                        enemy_modif_type=4
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()
                   
                    if enemy_modif_val>50 and enemy_modif_val<71:
                        enemy_modif_type=5
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()
                    
                    if enemy_modif_val>70 and enemy_modif_val<86:
                        enemy_modif_type=6
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                    if enemy_modif_val>85 and enemy_modif_val<101:
                        enemy_modif_type=7
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                    if enemy_modif_val>100 and enemy_modif_val<111:
                        enemy_modif_type=8
                        a=enemy_modif_type
                        temp_e_modif=all_enemy_modifiers[(a)-1]
                        temp_modif_e_n, modif_id, temp_modif_e_arm_equiped, temp_modif_e_wep_equiped, temp_modif_e_mhp, temp_modif_e_hp, temp_modif_e_base_speed, temp_modif_e_ab, temp_modif_e_db, temp_modif_e_hc,  temp_modif_e_do, temp_modif_e_xpr, temp_modif_e_gr, temp_modif_e_descr=temp_e_modif.load_enemy_modif_stats()

                
                
                
                print('You encounter a ')
                if enemy_modif_val<111:
                    print(temp_modif_e_n+(x.name))
                    print(x.e_descr, temp_modif_e_descr, sep="\n")
                if enemy_modif_val>110:
                    print(x.name)
                    print(x.e_descr)
                if enemy_modif_val>110:
                    x.display_enemy_stats() 
                temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr=x.load_enemy_stats()
                if enemy_modif_val<111:
                    temp_e_n=temp_modif_e_n+temp_e_n
                    temp_e_mhp=round(temp_e_mhp*temp_modif_e_mhp)
                    temp_e_hp=round(temp_e_hp*temp_modif_e_hp)
                    temp_e_base_speed=temp_e_base_speed+temp_modif_e_base_speed
                    temp_e_ab=temp_e_ab+temp_modif_e_ab
                    temp_e_db=temp_e_db+temp_modif_e_db
                    temp_e_hc=temp_e_hc+temp_modif_e_hc
                    temp_e_do=temp_e_do+temp_modif_e_do
                    temp_e_xpr=round(temp_e_xpr*temp_modif_e_xpr)
                    temp_e_gr=round(temp_e_gr*temp_modif_e_gr)
                    display_modif_enemy_stats(temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr)
                enemy_alive=1
                in_combat=1
            else:
                print('You are already fighting an enemy')
            #(temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr)
            print('_____________________________________________________________________________________________________________________________')
            #combat system
            while xp_gained==0:
                while in_combat==1:
                    attack=int(input("Enter 1 if you wish to attack, enter 0 if you wish to run "))
                    if attack<0 or attack>1:
                        print("You have entered an invlaid number")
                        attack=0
                    
                    if attack==0:
                        in_combat=0
                        enemy_alive=0
                        
                    while attack==1:
                        print('_______________________________________________________________________________________________________________________________')
                        #speed and dice based initive system start
                        attack=0
                        if temp_e_hp>0:
                            p_speed_dice_t=random.choice(dice)
                            p_totl_speed=p_speed_dice_t+p_base_speed
                            e_speed_dice_t=random.choice(dice)
                            e_total_speed=e_speed_dice_t+temp_e_base_speed
                            print('Player base speed:')
                            print(p_base_speed)
                            #dice visual here
                            dicex6=p_speed_dice_t
                            dice_6_vis(dicex6)
                            print('Player dice roll:')
                            print(p_speed_dice_t)
                            print('Player total speed:')
                            print(p_totl_speed)

                            print('Enemy base speed:')
                            print(temp_e_base_speed)
                            #dice visual here
                            dicex6=e_speed_dice_t
                            dice_6_vis(dicex6)
                            print('Enemy dice roll:')
                            print(e_speed_dice_t)
                            print('Enemy total speed:')
                            print(e_total_speed)
                            if p_totl_speed>e_total_speed:
                                print('Player attacks first')
                                p_atk_first=1
                            if p_totl_speed<e_total_speed:
                                print('Enemy attacks first')
                                p_atk_first=0
                            if p_totl_speed==e_total_speed:
                                print('Speed equal fliping coin')
                                speed_tie_breaker=random.choice(dice)
                                #coin visual here
                                if speed_tie_breaker>3:
                                    coin_vis(1)
                                    print('Heads')
                                    print('Player attacks first')
                                    p_atk_first=1
                                if speed_tie_breaker<4:
                                    coin_vis(0)
                                    print('Tails')
                                    print('Enemy attacks first')
                                    p_atk_first=0
                        if temp_e_hp<0:
                            p_atk_first=1
                        #Attack and damage system
                        #(temp_e_n, enc_n, temp_e_arm_equiped, temp_e_wep_equiped, temp_e_mhp, temp_e_hp, temp_e_base_speed, temp_e_ab, temp_e_db, temp_e_hc,  temp_e_do, temp_e_xpr, temp_e_gr, temp_e_descr)
                        #Player hit funtion
                        def Player_hits(atk_temp1, p_atk_b, p_wep, p_wep_rd, temp_e_db, temp_e_hp, p_wep_fd, atk_f_temp1, temp_e_n):
                            print('You hit')
                            atk_temp1=(round(((p_atk_b+p_wep+(random.choice(dice)*(1+p_wep_rd))-temp_e_db)/2)))
                            if atk_temp1<0:
                                atk_temp1=0
                            print('Damage done:')
                            print(atk_temp1)
                            temp_e_hp=temp_e_hp-atk_temp1
                            atk_temp1=0
                            if p_wep_fd>0:
                                atk_f_temp1=atk_f_temp1+p_wep_fd
                                print(('You burn the ')+str(temp_e_n))
                            return(atk_temp1, temp_e_hp, atk_f_temp1)
                        #Looting enemy funtion
                        def loot_enemy(temp_e_n, enemy_alive, just_killed, p_xp, temp_e_xpr, p_gold, temp_e_gr, atk_f_temp1, atk_f_temp2, enc_n, my_ingot, tortle_shell, infernal_essence):
                            print(('The ')+str(temp_e_n)+(' is killed'))
                            enemy_alive=0
                            just_killed=1
                            p_xp=p_xp+temp_e_xpr
                            print('XP gained:')
                            print(temp_e_xpr)
                            p_gold=p_gold+temp_e_gr
                            print('Gold gained:')
                            print(temp_e_gr)
                            atk_f_temp1=0
                            atk_f_temp2=0
                            if enc_n==5:
                                print('You steal his mythril ingot')
                                my_ingot=my_ingot+1
                            if enc_n==9:
                                print('You steal his shell')
                                tortle_shell=tortle_shell+1
                            if enc_n==10:
                                print('You steal his essence')
                                infernal_essence=infernal_essence+1
                            return(enemy_alive, just_killed, p_xp, p_gold, atk_f_temp1, atk_f_temp2, my_ingot, tortle_shell, infernal_essence)
                        #enemy attack funtion 
                        def enemy_attack_fun(temp_e_hc, p_do, p_do_b, temp_e_n, atk_temp2, temp_e_ab, p_def_b, p_arm, p_hp, enc_n, atk_f_temp2):
                            if random.choice(dice)>(temp_e_hc+p_do+p_do_b):
                                print(('The ')+str(temp_e_n)+(' hits'))
                                atk_temp2=(round((temp_e_ab+random.choice(dice)-p_def_b-p_arm)/2))
                                if atk_temp2<0:
                                    atk_temp2=0
                                print('Damage done:')
                                print(atk_temp2)
                                p_hp=p_hp-atk_temp2
                                atk_temp2=0
                                if enc_n==10:
                                    atk_f_temp2=atk_f_temp2+1
                                    print('You are burnt, taking fire damage')
                                if p_hp<1:
                                    print('You died')
                                    atk_f_temp2=0
                            else:
                                print(('The ')+str(temp_e_n)+(' misses'))
                            return(atk_temp2, p_hp, atk_f_temp2)

                        #
                        if atk_f_temp2>0 and enemy_alive==1:
                            p_hp=p_hp-atk_f_temp2
                            print('Fire damage taken:')
                            print(atk_f_temp2)
                        if atk_f_temp1>0 and enemy_alive==1:
                            temp_e_hp=temp_e_hp-atk_f_temp1
                            print('Fire damage dealt:')
                            print(atk_f_temp1)
                        if p_atk_first==1:
                            print('You attack')
                            if random.choice(dice)>p_hit_c-temp_e_do:
                                atk_temp1, temp_e_hp, atk_f_temp1=Player_hits(atk_temp1, p_atk_b, p_wep, p_wep_rd, temp_e_db, temp_e_hp, p_wep_fd, atk_f_temp1, temp_e_n)
                                if temp_e_hp<1 and enemy_alive==1:
                                    enemy_alive, just_killed, p_xp, p_gold, atk_f_temp1, atk_f_temp2, my_ingot, tortle_shell, infernal_essence=loot_enemy(temp_e_n, enemy_alive, just_killed, p_xp, temp_e_xpr, p_gold, temp_e_gr, atk_f_temp1, atk_f_temp2, enc_n, my_ingot, tortle_shell, infernal_essence)
                                    xp_gained=1
                                if temp_e_hp<1 and enemy_alive==0 and just_killed==0:
                                    print('Stop!Stop!,he is already dead')
                                just_killed=0

                            else:
                                if enemy_alive==1:
                                    print('You miss')
                                if enemy_alive==0:
                                    print('You missed a corpse, you are an embarrassment to your creator')
                            if temp_e_hp>0:
                                atk_temp2, p_hp, atk_f_temp2=enemy_attack_fun(temp_e_hc, p_do, p_do_b, temp_e_n, atk_temp2, temp_e_ab, p_def_b, p_arm, p_hp, enc_n, atk_f_temp2)
                        if p_atk_first==0:
                            if temp_e_hp>0:
                                atk_temp2, p_hp, atk_f_temp2=enemy_attack_fun(temp_e_hc, p_do, p_do_b, temp_e_n, atk_temp2, temp_e_ab, p_def_b, p_arm, p_hp, enc_n, atk_f_temp2)
                            if random.choice(dice)>p_hit_c:
                                atk_temp1, temp_e_hp, atk_f_temp1=Player_hits(atk_temp1, p_atk_b, p_wep, p_wep_rd, temp_e_db, temp_e_hp, p_wep_fd, atk_f_temp1, temp_e_n)
                                if temp_e_hp<1 and enemy_alive==1:
                                    enemy_alive, just_killed, p_xp, p_gold, atk_f_temp1, atk_f_temp2, my_ingot, tortle_shell, infernal_essence=loot_enemy(temp_e_n, enemy_alive, just_killed, p_xp, temp_e_xpr, p_gold, temp_e_gr, atk_f_temp1, atk_f_temp2, enc_n, my_ingot, tortle_shell, infernal_essence)
                                    xp_gained=1
                                if temp_e_hp<1 and enemy_alive==0 and just_killed==0:
                                    print('Stop!Stop!,he is already dead')
                                just_killed=0

                            else:
                                if enemy_alive==1:
                                    print('You miss')
                                if enemy_alive==0:
                                    print('You missed a corpse, you are an embarrassment to your creator')
                        print('Player HP:')
                        print(p_hp)
                        if temp_e_hp<0:
                            temp_e_hp=0
                        print((temp_e_n)+' HP:')
                        print(temp_e_hp)
                        if p_hp<1:
                            enemy_alive=0
                            attack=0
                            in_combat=0
                            print('_____________________________________________________________________________________________________________________________')
                            print('You have died please restart the game')
                    #if enemy_alive==0 and in_combat==1:
                        #in_combat=int(input("Enter 1 if you wish to attack, enter 0 if you wish to leave "))

                    print('_____________________________________________________________________________________________________________________________')
                xp_gained=1
            #
            #encount system + combat system end
            #

            #
            #Level Checker start
            #

            while xp_gained==1:
                #level up common
                def level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b):
                    level=level+1
                    p_max_hp=p_max_hp+random.choice(hp_add_list)
                    p_hp=p_max_hp
                    p_atk_b=p_atk_b+1
                    p_def_b=p_def_b+1
                    print('You leveled up')
                    return(level, p_max_hp, p_hp, p_atk_b, p_def_b)   
                #level up peticular 
                if (level<2)and(p_xp>9):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                if (level<3)and(p_xp>24):
                    p_max_hp=p_max_hp+1
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                if (level<4)and(p_xp>59):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_hit_c=p_hit_c-1
                if (level<5)and(p_xp>99):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_atk_b=p_atk_b+1
                if (level<6)and(p_xp>199):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_def_b=p_def_b+2
                if (level<7)and(p_xp>399):
                    p_max_hp=p_max_hp+2
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                if (level<8)and(p_xp>799):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_hit_c=p_hit_c-1
                if (level<9)and(p_xp>1199):
                    p_max_hp=p_max_hp+2
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                if (level<10)and(p_xp>1999):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_atk_b=p_atk_b+1
                    p_def_b=p_def_b+1
                if (level<11)and(p_xp>3499):
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                    p_do_b=p_do_b+1
                if (level<12)and(p_xp>6999):
                    p_max_hp=p_max_hp+3
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)
                if (level<13)and(p_xp>11999):
                    p_max_hp=p_max_hp+3
                    level, p_max_hp, p_hp, p_atk_b, p_def_b=level_up_base(level, p_max_hp, p_hp, p_atk_b, p_def_b)

                if enemy_alive==0:
                    p_hp=p_max_hp
                print('XP:')
                print(p_xp)
                print('Level:')
                print(level)
                xp_gained=0
            xp_gained=0
            #
            #Level Checker start
            #

            #continue looking for enemies
            print('Enter 0 if you wish to go stop fighting')
            print('enter 1 if you wish to continue in the same zone')
            print('enter 2 if you wish to select a new zone')
            continue_fight=int(input('Enter number here '))
            print('_____________________________________________________________________________________________________________________________')

        directory_val=0

        #
        #Encounter/combat/levelcheck end
        #   

    while directory_val==4:

        #
        #Stats display start
        #

        print('_____________________________________________________________________________________________________________________________')


        stats=['max hp', p_max_hp, 'hp', p_hp, 'p_atk', p_atk_b, 'weapon bonus', p_wep, 'p_def_b', p_def_b, 'armour bonus', p_arm, 'p_hit_c', p_hit_c, 'level', level, 'xp', p_xp, 'gold', p_gold]
        for element in stats:
            print(element)

        directory_val=0

        print('_____________________________________________________________________________________________________________________________')    

        #
        #Stats display start
        #

    while directory_val==5:

        #
        #heal system start
        #

        print('_____________________________________________________________________________________________________________________________')

        if enemy_alive==0:
            p_hp=p_max_hp
            print('You are healed')
            print('HP:')
            print(p_hp)
        else:
            print('You can not heal in battle')

        directory_val=0 

        print('_____________________________________________________________________________________________________________________________')

        #
        #heal system start
        #
