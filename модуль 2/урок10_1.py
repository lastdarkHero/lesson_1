# import abc


# class AbsTank(abc.ABC):
#     def __init__(self, armor, damage, speed, health):
#         self.armor = armor
#         self.damage = damage
#         self.speed = speed
#         self.health = health
        
# class Mouse(AbsTank):
#     def shoot(self, enemy):
#         enemy.health_down(self.damage)

#     def shoot(self, enemy):
#         enemy.health_down(self.damage)
         
#     def health_down(self, damage):
#         total_damage = damage // self.armor
#         self.health -= total_damage





# class T34(AbsTank):
#     def __init__(self, armor, damage, speed, health):
#         self.armor = armor
#         self.damage = damage
#         self.speed = speed
#         self.health = health

#     def shoot(self, enemy):
#        enemy.health_down(self.damage)

#     def health_down(self, damage):
#         total_damage = damage // self.armor
#         self.health -= total_damage

# class Mouse(AbsTank):
#     def shoot(self, enemy):
#         enemy.health_down(self.damage)


# mouse = Mouse(3000, 100, 50, 10)
# t34 = T34(2500,100, 60, 15)
# mouse.shoot()



