import os
from os.path import isfile, join, split, exists
import json

class NPCs:
    def __init__(self):
        path = split(abspath(__file__))
        self.NPCsPath = join(path[0], '..', 'assets', 'NPCs')
    
    def getNPCs(self, npcType: ('Allies' or 'Enemies')) -> tuple:
        return tuple(f.split('.')[0] for f in os.listdir(join(self.NPCsPath, npceType)) if isfile(join(self.NPCsPath, npcType, f)))
    
    def getNPCInfo(self, npc) -> dict:
        npcType = 'Allies'
        if self.isNPCExists(npc, npcType):
            with open(join(self.NPCsPath, npcType, f"{npc}.json")) as f:
                data = json.load(f)
            
            return {
                'name': data.get('name'),
                'lines': data.get('lines'),
                'actionOptions': data.get('actionOptions')
            }
        else:
            return {}
    
    def getEnemyInfo(self, npc) -> dict:
        npcType = 'Enemies'
        if self.isNPCExists(npc, npcType):
            with open(join(self.NPCsPath, npcType, f"{npc}.json")) as f:
                data = json.load(f)
            
            return {
                'name': data.get('name'),
                'attack': data.get('attack'),
                'freq': data.get('freq')
            }
        else:
            return {}
        
    
    def isNPCExists(self, npc, npcType: ('Allies' or 'Enemies')) -> bool:
        return exists(join(self.NPCsPath, npcType, f"{npc}.json"))