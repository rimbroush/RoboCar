import math
class Deplacement:
    def __init__(self,simulation,robot):
        self.sim = simulation
        self.robot = robot
        self.depart = None
            
    def avancer_x_metres(self, distance, vitesse):
        """Fait avancer le robot d'une distance donnée en mètres à une vitesse donnée.
        distance <= 3 [limitations de la simulation//environnement]"""
        distance_pixels = distance * 100 # Convertir la distance en pixels
        if self.depart is None: #Si c'est le premier appel, on memorise le point de depart
            self.depart = (self.sim.robot.x,self.sim.robot.y)
        
        #on avance tout droit
        self.sim.avancer(vitesse)
        
        #distance déjà parcourue depuis le départ
        dx = self.sim.robot.x - self.depart[0]
        dy = self.sim.robot.y - self.depart[1]
        distance_parcourue = math.sqrt(dx**2 + dy**2)
        
        #si on a atteint la distance cible, on arrete le robot
        if distance_parcourue >= distance_pixels:
            self.sim.arreter()
            self.depart = None #on reset le point de départ
            return True #la distance a été atteinte
        return False #le robot continue d'avancer
    

