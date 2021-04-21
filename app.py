from Modal import ScenesModal, SkillsModal, CharactModal

sm = ScenesModal.Scenes()
skm = SkillsModal.Skills()
cm = CharactModal.Character()
cm.create('Phoenix')
print(sm.getScene('a'))
# print(sm.getScene('b'))
# print(sm.getScene('c'))
# print(sm.getScenesList())
print(skm.getSkillAttack('fireball', 'm', '1'))