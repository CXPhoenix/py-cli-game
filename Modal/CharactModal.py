import os
from os.path import isfile, join, split, exists, abspath
import json

class Character:
    def __init__(self):
        path = split(abspath(__file__))
        self.CharactPath = join(path[0], '..', 'assets', 'Character')
    
    def create(self, name) -> bool: # True if sccuess else False
        if not self.isNameExists(name):
            self.name = name
            with open(join(self.CharactPath, f"{name}.json"),'w', newline='') as f:
                data = {
                    'name': name,
                    'property': {
                        'life': 100,
                        'magi': 50,
                        'attack': 3,
                        'evade': 5,
                        'defense': 10
                    },
                    'equipment': {
                        'weapon': 'knife',
                        'armor': 'Tshirt',
                    },
                    'skills': { # skill name: {type:{p -> physics, m -> magic}, levels}
                        'punch': {
                            'type': 'p',
                            'level': 1,
                        },
                        'fireball': {
                            'type': 'm',
                            'level': 1,
                        }
                    },
                    'items': { # item name: {type: {w -> weapon, a -> armor, lh -> life heal, mh -> magi heal}, amount}
                        'small-life-heal': {
                            'type': 'lh',
                            'amount': 5
                        },
                        'small-magi-heal': {
                            'type': 'mh',
                            'amount': 5
                        }
                    }
                }
                json.dump(data, f)
            self.createRecord(name)
            return True
        else:
            return False
    
    def readInfo(self, name) -> dict:
        if self.isNameExists(name):
            with open(join(self.CharactPath, f"{name}.json"), newline='') as f:
                data = json.load(f)
            return {
                'name': data.get('name'),
                'property': data.get('property'),
                'equipment': data.get('equipment'),
                'skills': data.get('skills'),
                'items': data.get('items')
            }
    
    def updateInfo(self, name, update: dict) -> bool:
        with open(join(self.CharactPath, f"{name}.json"), newline='') as f:
            data = json.load(f)
        for u in update:
            if u in data:
                data.update({u:update.get(u)})
            else:
                return False
        else:
            with open(join(self.CharactPath, f"{name}.json"), 'w', newline='') as f:
                json.dump(data, f)
            return True
    
    def isNameExists(self, name) -> bool:
        return exists(join(self.CharactPath, f"{name}.json"))
    
    def readRecords(self, name) -> dict:
        if self.isRecordExists(name):
            with open(join(self.CharactPath, f"{name}.log.json"), newline='') as f:
                data = json.load(f)
            return data
        else:
            return {}
    
    def updateRecord(self, name, update: dict) -> bool:
        with open(join(self.CharactPath, f"{name}.log.json"), newline='') as f:
            data = json.load(f)
        for u in update:
            if u in data:
                data.update({u:update.get(u)})
            else:
                return False
        else:
            with open(join(self.CharactPath, f"{name}.log.json"), 'w', newline='') as f:
                json.dump(data, f)
            return True
    
    def createRecord(self, name) -> None:
        with open(join(self.CharactPath, f"{name}.log.json"), 'w') as f:
            f.write('')
    
    def isRecordExists(self, name) -> bool:
        return exists(join(self.CharactPath, f"{name}.log.json"))