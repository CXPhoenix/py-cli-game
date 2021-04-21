import os
from os.path import isfile, split, join, abspath, exists
import json

# def skillBaseAttackError():
#     raise IndexError("Can't find skill's based-attack value..")

# def skillExistsError():
#     raise ValueError("Can't find the skill..")

# def skillNameExistsError():
#     raise ValueError("Can't find the skill's name..")

class Skills:
    def __init__(self):
        path = split(abspath(__file__))
        self.SkillsPath = join(path[0], '..', 'assets', 'Skills')
    
    def getSkills(self, skillType: ('m', 'p')) -> tuple:
        return tuple(f.split('.')[0] for f in os.listdir(join(self.SkillsPath, skillType)) if isfile(join(self.SkillsPath, skillType,f)))
    
    def getSkillName(self, skill, skillType: ('m' or 'p')) -> str:
        if self.isSkillExists(skill, skillType):
            with open(join(self.SkillsPath, skillType, f"{skill}.json")) as f:
                data = json.load(f)
            if not data.get('name'):
                return ""
            else:
                return data.get('name')
        else:
            return ""

    def getSkillAttack(self, skill, skillType: ('m' or 'p'), level: str) -> int:
        if self.isSkillExists(skill, skillType):
            with open(join(self.SkillsPath, skillType, f"{skill}.json")) as f:
                data = json.load(f)
            if not data.get(level).get('based-attack'):
                return 0
            else:
                return data.get(level).get('based-attack')
        else:
            return 0
        
    def isSkillExists(self, skill, skillType: ('m' or 'p')) -> bool:
        return exists(join(self.SkillsPath, skillType, f"{skill}.json"))