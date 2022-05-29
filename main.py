from Simulation import*
import csv

'''
This simulation generates an intersection filled with a given number of cars. These cars are distributed randomly through the intersection, arriving from any given direction. Each car is randomized in terms its destination, where it's coming from and what type of car it is (i.e. if it's self driving or not). The TrafficFlow class then takes this intersection and follows the rules of the road to take each car to it's given destination. In doing this, it also keeps track of the average 'stopping time' of each car.
Important note: This 'stopping time' is not a measure of time itself. Rather, it is defined by the number of cars a vahicle must give priority to once it stops. Therefore, the waiting time of a car is 'stopping time' x average time it takes for car to clear intersection.
'''
NUM_CARS = 10
NUM_SIMULATIONS = 1000
SELF_DRIV_CHANCE = 0.5 ## Probability of car being self-driving



def get_sim_data(num_cars,self_driv_chance):
  total = [0,0,0,0]
  for i in range(NUM_SIMULATIONS):
    simulation = Simulation(num_cars,self_driv_chance)
    simulation.execute_simulation()
    data = simulation.get_info()
    for i in range (4):
      total[i] += data[i]
  average=[0,0,0,0]
  for i in range(4):
    average[i] = round(total[i]/NUM_SIMULATIONS,2)
  ## Each simulation record contains [Av_stop_time, Av_self_driv_stop_time, Av_non_self_driv_stop_time, Av_safety_rating] of that simulation  
  return average

def main_var_num_cars(start,stop,step):
  ## See how intersection handles variable NUM_CARS
  result = []
  for num_cars in range (start,stop,step):
    result.append([num_cars] + get_sim_data(num_cars,SELF_DRIV_CHANCE))
  fields = ["Num_cars","Av_stop_time", "Av_self_driv_stop_time", "Av_non_self_driv_stop_time", "Av_safety_rating"]
  with open('main_var_num_cars.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(result)
  
  

def main_var_chance(start,stop,step):
  ## Run simulation with variable SELF_DRIV_CHANCE
  result = []
  for self_driv_chance in range (start,stop,step):
    self_driv_chance= self_driv_chance/10
    result.append([round(self_driv_chance,2)] + get_sim_data(NUM_CARS,self_driv_chance))
  fields = ["Chance_of_self_driv","Av_stop_time", "Av_self_driv_stop_time", "Av_non_self_driv_stop_time", "Av_safety_rating"]
  with open('main_var_chance.csv', 'w') as f:      
    # using csv.writer method from CSV package
    write = csv.writer(f)
      
    write.writerow(fields)
    write.writerows(result)

def main():
  total = [0,0,0,0]
  for i in range(NUM_SIMULATIONS):
    #print("Simulation #" + str(i))
    simulation = Simulation(NUM_CARS,SELF_DRIV_CHANCE)
    simulation.execute_simulation()
    data = simulation.get_info()
    for i in range (4):
      total[i] += data[i]
  average=[0,0,0,0]
  for i in range(4):
    average[i] = round(total[i]/NUM_SIMULATIONS,2)
  print("[Av_stop_time, Av_self_driv_stop_time, Av_non_self_driv_stop_time, Av_safety_rating]:")
  print(average)
##return average of all results


main()
##main_var_chance(0,11,1)
##main_var_num_cars(10,105,5)