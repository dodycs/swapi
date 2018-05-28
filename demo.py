import requests, json, sys
from pprint import pprint

for people_id in range(1,87):
   # people
   people_response = requests.get('https://swapi.co/api/people/{}'.format(people_id))
   people_obj = json.loads(people_response.text)
   if 'name' in people_obj:
      print(people_obj['name'])
      print(people_obj['birth_year'])
      print(people_obj['gender'])

      # homeworld
      if len (people_obj['homeworld']) > 0:
         homeworld_obj = requests.get(people_obj['homeworld'])
         homeworld_obj = json.loads(homeworld_obj.text)
         print('H -\t{}'.format(homeworld_obj['name']))
         print('   \t{}'.format(homeworld_obj['climate']))
         print('   \t{}'.format(homeworld_obj['terrain']))
         
      # starship
      if len(people_obj['starships']) > 0:
         for el in people_obj['starships']:
            starship_response = requests.get(el)
            starship_obj = json.loads(starship_response.text)
            print('S - \t{}'.format(starship_obj['name']))
            print('   \t{}'.format(starship_obj['model']))
            print('   \t{}'.format(starship_obj['manufacturer']))

      # vehicle
      if len(people_obj['vehicles']) > 0:
         for el in people_obj['vehicles']:
            vehicle_response = requests.get(el)
            vehicle_obj = json.loads(vehicle_response.text)
            print('V - \t{}'.format(starship_obj['name']))
            print('    \t{}'.format(starship_obj['model']))
            print('    \t{}'.format(starship_obj['manufacturer']))

      print('------------------------------')


   sys.stdout.flush()
