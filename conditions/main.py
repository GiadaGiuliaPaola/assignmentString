# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action (weather, time_of_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status) :
    if  weather == 'rainy' and time_of_day == 'night'  and location_of_the_cows == 'pasture':
        return 'take cows to cowshed'
    elif location_of_the_cows == 'cowshed' and cow_milking_status == True:
        return 'milk cows'
    elif weather == 'rainy' and slurry_tank == True and location_of_the_cows == 'cowshed':
        return 'fertilize pasture'
    elif grass_status == True and weather == 'sunny' and season == 'spring' and location_of_the_cows == 'cowshed':
        return 'mow grass'
    elif weather == 'sunny' and time_of_day == 'day' and location_of_the_cows == 'pasture' and slurry_tank == False:
        return """take cows to cowshed
milk cows
take cows back to pasture"""
    else:
        return 'wait'


print (farm_action('rainy', 'night', False, 'cowshed', 'winter', True, True))
#fertilize pasture
print (farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True))
#'wait'
print (farm_action('windy', 'night', True, 'cowshed', 'winter', True, True))
#milk cows
print (farm_action('sunny', 'day', True, 'pasture', 'spring', False, True))
#"""take cows to cowshed / milk cows / take cows back to pasture"""
