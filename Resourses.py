#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#dice and coin lists
hp_dice=[1, 1, 1, 2, 2, 3]
hp_adv_dice=[2, 2, 2, 3, 3, 4]
coin=[0, 1]
d2=[1, 2]
d4=[1, 2, 3, 4]
d6=[1, 2, 3, 4, 5, 6]
d8=[1, 2, 3, 4, 5, 6, 7, 8]
d10=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
d12=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
d16=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
d20=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


# In[ ]:


#visuals

#coin Visual
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
        
        
        
#D10 dice visual system
#works for lower dice too
def dice_10_vis(dicex10):
    if dicex10 == 1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
    if dicex10 == 2:
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
    if dicex10 == 4:
        print('       ')
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
        print('       ')
    if dicex10 == 5:
        print('       ')
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
        print('       ')
    if dicex10 == 6:
        print('       ')
        print("[-----]")
        print("[0 0 0]")
        print("[     ]")
        print("[0 0 0]")
        print("[-----]")
        print('       ')
    if dicex10 == 7:
        print('       ')
        print("[-----]")
        print("[0 0 0]")
        print("[  0  ]")
        print("[0 0 0]")
        print("[-----]")
        print('       ')
    if dicex10 == 8:
        print('       ')
        print("[-----]")
        print("[0 0 0]")
        print("[0   0]")
        print("[0 0 0]")
        print("[-----]")
        print('       ')
    if dicex10 == 9:
        print('       ')
        print("[-----]")
        print("[0 0 0]")
        print("[0 0 0]")
        print("[0 0 0]")
        print("[-----]")
        print('       ')
    if dicex10 == 10
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  X  ]")
        print("[     ]")
        print("[-----]")
        print('       ')
        
        
 


# In[ ]:


def dice_20_vis(dicex20):
    if dicex20 == 1:
        print('         ')
        print("[-------]")
        print("[       ]")
        print("[   0   ]")
        print("[       ]")
        print("[-------]")
        print('         ')
    if dicex20 == 2:
        print('         ')
        print("[-------]")
        print("[       ]")
        print("[  0 0  ]")
        print("[       ]")
        print("[-------]")
        print('         ')
    if dicex20 == 3:
        print('         ')
        print("[-------]")
        print("[  0    ]")
        print("[   0   ]")
        print("[    0  ]")
        print("[-------]")
        print('         ')
    if dicex20 == 4:
        print('         ')
        print("[-------]")
        print("[  0 0  ]")
        print("[       ]")
        print("[  0 0  ]")
        print("[-------]")
        print('         ')
    if dicex20 == 5:
        print('         ')
        print("[-------]")
        print("[  0 0  ]")
        print("[   0   ]")
        print("[  0 0  ]")
        print("[-------]")
        print('         ')
    if dicex20 == 6:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[       ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 7:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[   0   ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 8:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[ 0   0 ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 9:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[ 0 0 0 ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 10:
        print('         ')
        print("[-------]")
        print("[       ]")
        print("[   X   ]")
        print("[       ]")
        print("[-------]")
        print('         ')
    if dicex20 == 11:
        print('         ')
        print("[-------]")
        print("[   0   ]")
        print("[       ]")
        print("[   X   ]")
        print("[-------]")
        print('         ')
    if dicex20 == 12:
        print('         ')
        print("[-------]")
        print("[ 0     ]")
        print("[   X   ]")
        print("[     0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 13:
        print('         ')
        print("[-------]")
        print("[   0   ]")
        print("[   X   ]")
        print("[  0 0  ]")
        print("[-------]")
        print('         ')
    if dicex20 == 14:
        print('         ')
        print("[-------]")
        print("[  0 0  ]")
        print("[   X   ]")
        print("[  0 0  ]")
        print("[-------]")
        print('         ')
    if dicex20 == 15:
        print('         ')
        print("[-------]")
        print("[  0 0  ]")
        print("[   X   ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 16:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[   X   ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 17:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[   X   ]")
        print("[ 00 00 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 18:
        print('         ')
        print("[-------]")
        print("[ 0 0 0 ]")
        print("[ 0 X 0 ]")
        print("[ 0 0 0 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 19:
        print('         ')
        print("[-------]")
        print("[ 00 00 ]")
        print("[   x   ]")
        print("[ 00000 ]")
        print("[-------]")
        print('         ')
    if dicex20 == 20:
        print('         ')
        print("[-------]")
        print("[   x   ]")
        print("[       ]")
        print("[   x   ]")
        print("[-------]")
        print('         ')
    


# In[7]:


def percentbar25(x, y):
    if x>y:
        x=y
    precentbar=round((x/y)*25)
    if precentbar == 0:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[-----]")
        print('       ')
    if precentbar == 1:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[  X  ]")
        print("[-----]")
        print('       ')
    if precentbar == 2:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[X   X]")
        print("[-----]")
        print('       ')
    if precentbar == 3:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[X X X]")
        print("[-----]")
        print('       ')
    if precentbar == 4:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[XX XX]")
        print("[-----]")
        print('       ')
    if precentbar == 5:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 6:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[  X  ]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 7:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[ X X ]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 8:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[X X X]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 9:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[XX XX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 10:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[     ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 11:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[  X  ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 12:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[ X X ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 13:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[X X X]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 14:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[XX XX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 15:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[     ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 16:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[  X  ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 17:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[ X X ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 18:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[X X X]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 19:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[XX XX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 20:
        print('       ')
        print("[-----]")
        print("[     ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 21:
        print('       ')
        print("[-----]")
        print("[  X  ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 22:
        print('       ')
        print("[-----]")
        print("[ X X ]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 23:
        print('       ')
        print("[-----]")
        print("[X X X]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 24:
        print('       ')
        print("[-----]")
        print("[XX XX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')
    if precentbar == 25:
        print('       ')
        print("[-----]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[XXXXX]")
        print("[-----]")
        print('       ')


# In[11]:


percentbar25(121, 145)


# In[16]:


#truepercentile display
list=[2, 4]
a=9-list[0]
b=10-list[1]
c=list[0]
print('            ')
print("[----------]")
while a>0:
    print("[          ]")
    a-=1
X=("X")
space=(" ")
print("["+(X*list[1])+(space*b)+"]")
while c>0:
    print("[XXXXXXXXXX]")
    c-=1
print("[----------]")
print('            ')


# In[ ]:


if list[1]==0:
    print("[          ]")
if list[1]==1:
    print("[X         ]")
if list[1]==2:
    print("[X X       ]")
if list[1]==3:
    print("[X X X     ]")
if list[1]==4:
    print("[XXXX      ]")
if list[1]==5:
    print("[XXXXX     ]")
if list[1]==6:
    print("[XXXXXX    ]")
if list[1]==7:
    print("[XXXXXXX   ]")
if list[1]==8:
    print("[XXXXXXXX  ]")
if list[1]==9:
    print("[XXXXXXXXX ]")

