import os
from os.path import isfile, join, abspath, split, exists
import json

class Scenes:
    def __init__(self):
        path = split(abspath(__file__))
        self.ScenePath = join(path[0], '..', 'assets', 'Scene')
    
    def getScene(self, sceneName, sceneType = 'dungeon') -> dict:
        if self.checkSceneExist(sceneName):
            with open(join(self.ScenePath, sceneType, f"{sceneName}.json"), newline='') as f:
                data = json.load(f)
            if data.get('sceneName') == sceneName and data.get('description') and data.get('moveActions'):
                return {
                    'sceneName': data.get('sceneName'),
                    'description': data.get('description'),
                    'moveActions': data.get('moveActions')
                }
            else:
                return {}
        else:
            raise ValueError("Can't find the scene..")
    
    def checkSceneExist(self, sceneName, sceneType = 'dungeon') -> bool:
        return exists(join(self.ScenePath, sceneType, f"{sceneName}.json"))
    
    def getScenesList(self, sceneType = 'dungeon') -> tuple:
        return tuple(f.split('.')[0] for f in os.listdir(join(self.ScenePath, sceneType)) if isfile(join(self.ScenePath, sceneType, f)))
    
    
    
    
    