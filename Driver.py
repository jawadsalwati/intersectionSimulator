import random



    
def get_random_direction():
  r = random.random()
  if r < 0.25:
    return "N"
  elif r < 0.5:
    return "E"
  elif r < 0.75:
    return "S"
  else:
    return "W"
      
class Driver:

  def __init__(self,self_driv_chance):
    self.self_driv_chance = self_driv_chance
    self.self_driv = self.is_self_driv()
    self.arrival_direction = get_random_direction()
    self.destination = get_random_direction()
    while (self.arrival_direction == "W") and (self.destination == "W"):
      self.destination = get_random_direction()
    self.stop_time = 0
    self.safety_rating = self.get_safety_rating()
    
    #Returns driver instance stop time
  def get_stop_time(self):
    return self.stop_time

  def is_self_driv(self):
    r = random.random()
    ##print(self.self_driv_chance)
    if r < self.self_driv_chance:
      return True
    else:
      return False

  def get_safety_rating(self):
    if self.self_driv:
      return 10
    
    r = random.randint(500,800)

    return r/100
  
           
      
