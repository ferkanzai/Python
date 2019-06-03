cost_prem = 125

def ground_shipping(weight):
  flat = 20
  cost = 0
  
  if (weight <= 2):
    cost = (weight * 1.50) + flat
  elif (2 < weight <= 6):
    cost = (weight * 3) + flat
  elif (6 < weight <= 10):
    cost = (weight * 4) + flat
  elif (weight > 10):
    cost = (weight * 4.75) + flat
	
  return cost

def drone_shipping(weight):
  cost = 0
  
  if (weight <= 2):
    cost = weight * 4.50
  elif (2 < weight <= 6):
    cost = weight * 9
  elif (6 < weight <= 10):
    cost = weight * 12
  elif (weight > 10):
    cost = weight * 14.25
	
  return cost

def cheapest(weight):
  cost_g = ground_shipping(weight)
  cost_d = drone_shipping(weight)
    
  if (cost_prem < cost_g):
    return "Cheapest is Premium and costs " + str(cost_prem) 
  else:
    if (cost_g < cost_d):
      return "Cheapest is Ground and costs " + str(cost_g) 
    else:
      return "Cheapest is Drone and costs " + str(cost_d) 

print(ground_shipping(1.5))
print(drone_shipping(1.5))
print(cheapest(4.8))
print(cheapest(41.5))