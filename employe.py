# Définition des classes
class Employe:
  def __init__(self, identifiant, nom):
    self.id = identifiant
    self.nom = nom
	self.type = "Employé"

  def __repr__(self):
	chaine = "{} {} : {}".format(sel.type, self.id, self.nom)
    return chaine
    
class Responsable(Employe):
  def __init__(self, identifiant, nom, rang):  
    Employe.__init__(self, identifiant, nom)
	self.type = "Responsable"
    self.number = rang
  
  def __repr__(self):
    chaine = "{} {} : {} (number {})".format(self.type, self.id, self.nom, self.number)
    return chaine
  
  def engueuler(self, employe):
    print("Alors, tu bosses un peu {} ou quoi ?!!".format(employe.nom))

# Programme principal   