from Driver import*

## Prints car types within list
def print_line(list):
  for driver in list:
      if driver.self_driv:
        print(" S ")
      else:
        print(" D ")



"""
This is the most complex part of the code, but the idea is straight-forward.
Essentially, we are defining how each arrival lane deals with a driver.
We then use the destination of the driver, the type of vehicle and the current traffic conditions to define how long the driver has to wait for.
Here, stop time of a car is defined by the number of vehicles it must give right of way to.
"""

class TrafficFlow:
  
  def __init__(self):
    self.main_can_go = False
    self.east_arrivals, self.south_arrivals, self.north_arrivals, self.west_arrivals = ([] for i in range(4))
    self.east_exits, self.north_exits, self.south_exits, self.west_exits = ([] for i in range(4))

    self.north_b_arr = self.north_arrivals.copy() ## North Bottom Arrival Lane
    self.east_b_arr = self.east_arrivals.copy() ## East Bottom Arrival Lane
    self.south_b_arr = self.south_arrivals.copy() ## South Bottom Arrival Lane
    self.west_t_arr = self.west_arrivals.copy() ## West Top Arrival Lane
   
    self.north_t_exit = self.north_exits ## North Top Exit Lane
    self.east_t_exit = self.east_exits ## East Top Exit Lane 
    self.south_t_exit = self.south_exits ## South Top Exit Lane
    self.west_b_exit = self.west_exits ## West Bottom Exit Lane

    self.update()
  
  def update(self):
    self.north_arrivals = self.north_b_arr.copy() 
    self.east_arrivals = self.east_b_arr.copy()
    self.south_arrivals = self.south_b_arr.copy() 
    self.west_arrivals = self.west_t_arr.copy()

  ## Spawning random driver from a random direction
  def generate_driver(self,self_driv_chance):
    new_driver = Driver(self_driv_chance)
    if new_driver.arrival_direction == "N":
      self.north_b_arr.append(new_driver)
    elif new_driver.arrival_direction == "E":
      self.east_b_arr.append(new_driver)
    elif new_driver.arrival_direction == "S":
      self.south_b_arr.append(new_driver)
    else:
      self.west_t_arr.append(new_driver)

  ## Display arriving vehicles to intersection
  def display_arrivals(self):
    print("")
    print("'''''''''''''''''''''''''''''''''''''''''''''''")
    print("North Bottom Arrival Lane: ")
    print_line(self.north_b_arr)
    print("East Bottom Arrival Lane: ")
    print_line(self.east_b_arr)
    print("West Top Arrival Lane: ")
    print_line(self.west_t_arr)
    print("South Bottom Arrival Lane: ")
    print_line(self.south_b_arr)
    print("'''''''''''''''''''''''''''''''''''''''''''''''")
    print("")

    ## Display arriving vehicles to intersection
  def display_exits(self):
    print("")
    print("'''''''''''''''''''''''''''''''''''''''''''''''")
    print("North Top Exit Lane: ")
    print_line(self.north_t_exit)
    print("East Top Exit Lane: ")
    print_line(self.east_t_exit)
    print("West Bottom Exit Lane: ")
    print_line(self.west_b_exit)
    print("South Top Exit Lane: ")
    print_line(self.south_t_exit)
    print("'''''''''''''''''''''''''''''''''''''''''''''''")
    print("")

  ## Checks if intersection is clear
  def isEmpty(self):
    if (len(self.north_b_arr)==0) and (len(self.east_b_arr))==0 and (len(self.south_b_arr)==0) and (len(self.west_t_arr)==0):
      return True
    else:
      return False
    
  def manage_east_arrivals(self):
    self.update()
    for car in self.east_arrivals:
      ## Green Light
      if self.main_can_go:
        car.stop_time += 0
        self.east_b_arr.remove(car)
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)
      ## Self Driving Red light
      elif (not (self.main_can_go)) and (car.self_driv):
        self.east_b_arr.remove(car)
        car.stop_time += len(self.north_b_arr) + len(self.south_b_arr)
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)
      ## Not Self Driving Red Light
      else:
        car.stop_time += len(self.north_b_arr) + len(self.south_b_arr)+self.east_arrivals.index(car)

  def manage_north_arrivals(self):
    self.update()
    for car in self.north_arrivals:
      ## Going straight
      if (car.destination=="S"):
        car.stop_time += 0
        self.north_b_arr.remove(car)
        self.south_exits.append(car)
      ## If not going straight, must go right
      ## Self-Driving Car yielding to go right
      elif (car.self_driv) and self.main_can_go:
        self.north_b_arr.remove(car)
        car.stop_time += len(self.east_b_arr)
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)
        
      ## Green Light for all vehicles to go right
      elif not (self.main_can_go):
        self.north_b_arr.remove(car)
        car.stop_time += 0
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)

      ## Not Self-Driving Red Light
      else:
        car.stop_time += len(self.east_b_arr) + self.north_arrivals.index(car)

  def manage_south_arrivals(self):
    self.update()
    for car in self.south_arrivals:
      ## Going straight
      if (car.destination=="N"):
        car.stop_time += 0
        self.south_b_arr.remove(car)
        self.north_exits.append(car)
      ## If not going straight, must go left
      ## Self-Driving Car yielding to go left
      elif (car.self_driv) and self.main_can_go:
        self.south_b_arr.remove(car)
        car.stop_time += len(self.east_b_arr)
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)
    
      ## Green Light for all vehicles to go left
      elif not (self.main_can_go):
        self.south_b_arr.remove(car)
        car.stop_time += 0
        if car.destination == "W":
          self.west_exits.append(car)
        else:
          self.west_t_arr.append(car)
      
      ## Not Self-Driving Red Light
      else:
        car.stop_time += len(self.east_b_arr) + self.south_arrivals.index(car)


  def manage_west_arrivals(self):
    self.update()
    for car in self.west_arrivals:
      self.west_t_arr.remove(car)
      car.stop_time += 0
      if car.destination == "N":
        self.north_exits.append(car)
      elif car.destination == "E":
        self.east_exits.append(car)
      else: ##car.destination == "S"
        self.south_exits.append(car)



  '''
  Book keeping functions
  '''
  
  def get_av_stop_time(self):
    exit_lanes = self.north_t_exit + self.east_t_exit + self.south_t_exit + self.west_b_exit
    stop_time=0
    for car in exit_lanes:
      stop_time += car.stop_time
    if len(exit_lanes)==0:
      return 0
    return stop_time/len(exit_lanes)

  def get_av_safety_rating(self):
    exit_lanes = self.north_t_exit + self.east_t_exit + self.south_t_exit + self.west_b_exit
    safety_rating = 0
    for car in exit_lanes:
      safety_rating += car.safety_rating
    if len(exit_lanes)==0:
      return 0
    return safety_rating/len(exit_lanes)
  
  def get_av_self_driv_stop_time(self):
    self_driving = self.north_t_exit + self.east_t_exit + self.south_t_exit + self.west_b_exit
    count = 0
    stop_time = 0
    for car in self_driving:
      if car.self_driv:
        count += 1
        stop_time += car.stop_time
    if count==0: 
      return 0
    return stop_time/count

  def get_av_non_self_driv_stop_time(self):
    non_self_driving = self.north_t_exit + self.east_t_exit + self.south_t_exit + self.west_b_exit
    count = 0
    stop_time = 0
    for car in non_self_driving:
      if not car.self_driv:
        count += 1
        stop_time += car.stop_time
    if count==0: 
      return 0
    return stop_time/count

  