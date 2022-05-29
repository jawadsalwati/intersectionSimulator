from TrafficFlow import*

class Simulation:

  def __init__(self, num_cars, self_driv_chance):
    self.traffic_flow = TrafficFlow()
    self.self_driv_chance = self_driv_chance
    self.fill_intersection(num_cars)
    self.enable_display = False ## Only enable true if NUM_SIMULATIONS is 1
    

  ## Specify number of cars you would like to fill intersection with
  def fill_intersection(self,num_cars):
    for i in range(num_cars):
      self.traffic_flow.generate_driver(self.self_driv_chance)

  def execute_simulation(self):
    while not (self.traffic_flow.isEmpty()):
      if self.enable_display:  
        self.traffic_flow.display_arrivals()
        self.traffic_flow.display_exits()
      self.traffic_flow.main_can_go = not self.traffic_flow.main_can_go
      self.traffic_flow.manage_west_arrivals()
      self.traffic_flow.manage_north_arrivals()
      self.traffic_flow.manage_south_arrivals()
      self.traffic_flow.manage_east_arrivals()

    if self.enable_display:  
      self.display_info()
   
      
  def display_info(self):
    print("Average Stop Time: ")
    print(round(self.traffic_flow.get_av_stop_time(),2))
    print("Average Self Driving Stop Time: ")
    print(round(self.traffic_flow.get_av_self_driv_stop_time(),2))
    print("Average Non Self Driving Stop Time: ")
    print(round(self.traffic_flow.get_av_non_self_driv_stop_time(),2))
    print("Average Safety Rating: ")
    print(round(self.traffic_flow.get_av_safety_rating(),2))

  def get_info(self):
    return [round(self.traffic_flow.get_av_stop_time(),2),
    round(self.traffic_flow.get_av_self_driv_stop_time(),2),
    round(self.traffic_flow.get_av_non_self_driv_stop_time(),2),
    round(self.traffic_flow.get_av_safety_rating(),2)]