class Deplacement:
    def __init__(self, robot, obstacles):
        self.robot = robot
        self.obstacles = obstacles
        
    #Eviter les obstacles il faut reviser
    def eviter_obstacles(self, dt):
        """Met à jour les vitesses des roues pour avancer et éviter les obstacles."""
        dist_obs = self.robot.distance_obstacle(self.obstacles) #la distance au plus proche obstacle devant le robot
        dist_mur = self.robot.distance_mur(800, 600) #la distance au mur le plus proche

        distance = min(dist_obs, dist_mur)

        if distance < 40:
            # tourne
            self.robot.set_vitesse_gauche(-60)
            self.robot.set_vitesse_droite(60)
        else:
            # avance
            self.robot.set_vitesse_gauche(30)
            self.robot.set_vitesse_droite(30)
            
    def avance(self):
        """Permet Flash d'avancer"""
        self.robot.set_vitesse_gauche(80)
        self.robot.set_vitesse_droite(80)
        
    def arreter(self):
        self.robot.set_vitesse_gauche(80)
        self.robot.set_vitesse_droite(80)
    
        
            
