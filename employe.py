# Définition des classes
class Employe:
  def __init__(self, identifiant, nom):
    self.id = identifiant
    self.nom = nom

  def __repr__(self):
    return "Employé {} : {}".format(self.id, self.nom)
    
class Responsable(Employe):
  def __init__(self, identifiant, nom, rang):  
    self.id = identifiant
    self.nom = nom
    self.number = rang
  
  def __repr__(self):
    return "Responsable (number {}) {} : {}".format(self.number, self.id, self.nom)
  
  def engueuler(self, employe):
    print("Alors, tu bosses un peu {} ou quoi ?!!".format(employe.nom))

# Programme principal   