import os
from os.path import isfile, split, join, abspath, exists
import json

# def itemEffectsError():
#     raise IndexError("Can't find item's effect value..")

# def weaponBaseAttackError():
#     raise IndexError("Can't find weapon's based-attack value..")

# def armorDefenseError():
#     raise IndexError("Can't find armor's defense value..")

# def itemExistsError():
#     raise ValueError("Can't find the item..")

# def itemNameExistsError():
#     raise ValueError("Can't find the item's name..")

class Items:
    def __init__(self):
        path = split(abspath(__file__))
        self.ItemsPath = join(path[0], '..', 'assets', 'Items')
    
    def getItems(self, itemType: ('w' or 'a' or 'lh' or 'mh')) -> tuple:
        return tuple(f.split('.')[0] for f in os.listdir(join(self.ItemsPath, skillType)) if isfile(join(self.ItemsPath, skillType,f)))
    
    def getItemName(self, item, itemType: ('w' or 'a' or 'lh' or 'mh')) -> str:
        if self.isItemExists(item, itemType):
            with open(join(self.ItemsPath, itemType, f"{item}.json")) as f:
                data = json.load(f)
            if not data.get('name'):
                return ""
            else:
                return data.get('name')
        else:
            return ""
        
    def getItemEffect(self, item, itemType: ('lh' or 'mh')) -> tuple:
        if self.isItemExists(item, itemType):
            with open(join(self.ItemsPath, itemType, f"{item}.json")) as f:
                data = json.load(f)
            if not data.get('effect'):
                return ()
            elif not (data.get('effect').get('to') and data.get('effect').get('effect')):
                return ()
            else:
                return (data.get('effect').get('to'), int(data.get('effect').get('effect')))
        else:
            return ()
    
    def getWeaponAttack(self, item) -> tuple:
        itemType = 'w'
        if self.isItemExists(item, itemType):
            with open(join(self.ItemsPath, itemType, f"{item}.json")) as f:
                data = json.load(f)
            if not data.get('property'):
                return ()
            elif not (data.get('property').get('base-attack') and data.get('property').get('type')):
                return ()
            else:
                return (data.get('property').get('type'), data.get('property').get('base-attack'))
        else:
            return ()
    
    def getArmorDefense(self, item) -> int:
        itemType = 'a'
        if self.isItemExists(item, itemType):
            with open(join(self.ItemsPath, itemType, f"{item}.json")) as f:
                data = json.load(f)
            if not data.get('property'):
                return 0
            elif not data.get('property').get('defense'):
                return 0
            else:
                return data.get('property').get('defense')
        else:
            return 0
        
    def isItemExists(self, item, itemType) -> bool:
        return exists(join(self.ItemsPath, itemType, f"{item}.json"))