#!/usr/bin/env python
# coding: utf-8

# In[ ]:


weapon_id_number=0
weapon_type_count=0
weapon_met_count=0




class Weapon_type_class:
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
        
    def type_stats_load(self):
        temp_t_name=self.name
        temp_t_id=self.id
        temp_t_equiped=self.equiped
        temp_t_quant=self.quant
        temp_t_damage_val=self.damage_val
        temp_t_wep_hit_c=self.wep_hit_c
        temp_t_r_damage_val=self.r_damage_val
        temp_t_f_damage_val=self.f_damage_val
        temp_t_weight=self.weight
        temp_t_gold_cost=self.gold_cost
        temp_t_descr=self.descr
        return(temp_t_name, temp_t_id, temp_t_equiped, temp_t_quant, temp_t_damage_val, temp_t_wep_hit_c, temp_t_r_damage_val, temp_t_f_damage_val, temp_t_weight, temp_t_gold_cost, temp_t_descr)
        
dagger=Weapon_type_class('Dagger', 1, 1, 1, 1, -1, 1, 0, 10, 100, 'dagger.')
short_sword=Weapon_type_class('Short Sword', 2, 0, 1, 2, 0, 0, 0, 15, 150, 'short sword.')
long_sword=Weapon_type_class('Long Sword', 3, 0, 0, 2, 1, 0, 0, 25, 200, 'long sword.')
great_sword=Weapon_type_class('Great Sword', 4, 0, 0, 2, 0, 1, 0, 30, 300, 'great sword.')
sabre=Weapon_type_class('Sabre', 5, 0, 0, 0, 1, 1, 0, 20, 250, 'sabre.')

all_weapon_type=[dagger, short_sword, long_sword, great_sword, sabre]
        
class Weapon_meterial_class:
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
        
    def mets_stats_load(self):
        temp_m_name=self.name
        temp_m_id=self.id
        temp_m_equiped=self.equiped
        temp_m_quant=self.quant
        temp_m_damage_val=self.damage_val
        temp_m_wep_hit_c=self.wep_hit_c
        temp_m_r_damage_val=self.r_damage_val
        temp_m_f_damage_val=self.f_damage_val
        temp_m_weight=self.weight
        temp_m_gold_cost=self.gold_cost
        temp_m_descr=self.descr
        return(temp_m_name, temp_m_id, temp_m_equiped, temp_m_quant, temp_m_damage_val, temp_m_wep_hit_c, temp_m_r_damage_val, temp_m_f_damage_val, temp_m_weight, temp_m_gold_cost, temp_m_descr)
        
wooden=Weapon_meterial_class('Wooden ', 1, 1, 1, -1, 1, -1, 0, -5, -50, 'A wooden ')
stone=Weapon_meterial_class('Stone ', 2, 0, 0, 1, 0, -1, 0, 5, -30, 'A stone ') 
iron=Weapon_meterial_class('Iron ', 3, 0, 0, 1, 0, 0, 0, 0, 0, 'A iron ')
steel=Weapon_meterial_class('Steel ', 4, 0, 0, 2, 1, 0, 0, 5, 100, 'A steel ')
brozne=Weapon_meterial_class('Brozne ', 5, 0, 0, 0, 0, 1, 0, 10, 150, 'A brozne ')

all_weapon_mets=[wooden, stone, iron, steel, brozne]


# In[ ]:


weapon_id_number=1
weapon_type_count=1
weapon_met_count=1

while weapon_type_count<6:
    a=weapon_type_count-1
    weapon_type=all_weapon_type[(a)]
    (temp_t_name, temp_t_id, temp_t_equiped, temp_t_quant, temp_t_damage_val, temp_t_wep_hit_c, temp_t_r_damage_val, temp_t_f_damage_val, temp_t_weight, temp_t_gold_cost, temp_t_descr)=weapon_type.type_stats_load()
    weapon_met_count=1
    while weapon_met_count<6:
        b=weapon_met_count-1
        weapon_met=all_weapon_mets[(b)]
        (temp_m_name, temp_m_id, temp_m_equiped, temp_m_quant, temp_m_damage_val, temp_m_wep_hit_c, temp_m_r_damage_val, temp_m_f_damage_val, temp_m_weight, temp_m_gold_cost, temp_m_descr)=weapon_met.mets_stats_load()
        
        temp_f_name=temp_m_name+temp_t_name
        temp_f_id=weapon_id_number
        weapon_id_number=weapon_id_number+1
        temp_f_equiped=temp_m_equiped*temp_t_equiped
        temp_f_quant=temp_m_quant*temp_t_quant
        temp_f_damage_val=temp_m_damage_val+temp_t_damage_val
        temp_f_wep_hit_c=temp_m_wep_hit_c+temp_t_wep_hit_c
        temp_f_r_damage_val=temp_m_r_damage_val+temp_t_r_damage_val
        temp_f_f_damage_val=temp_m_f_damage_val+temp_t_f_damage_val
        temp_f_weight=temp_m_weight+temp_t_weight
        temp_f_gold_cost=temp_m_gold_cost+temp_t_gold_cost
        temp_f_descr=temp_m_descr+temp_t_descr
        
        print((temp_m_name.replace(" ", "_"))+(temp_t_name.replace(" ", "_"))+"="+"('"+(temp_f_name)+"'"+', '+str(temp_f_id)+', '+str(temp_f_equiped)+', '+str(temp_f_quant)+', '+str(temp_f_damage_val)+', '+str(temp_f_wep_hit_c)+', '+str(temp_f_r_damage_val)+', '+str(temp_f_f_damage_val)+', '+str(temp_f_weight)+', '+str(temp_f_gold_cost)+', '+"'"+(temp_f_descr)+"')")
        
        weapon_met_count=weapon_met_count+1
        
    weapon_type_count=weapon_type_count+1
        
        
    

