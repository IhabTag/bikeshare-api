import time
import functions as fn
import functions_cli as fnc
import json

CITIES = {    'chicago': 'chicago',
              'new york': 'new_york_city',
              'washington': 'washington' }

MONTHS = {
              'january' : 1,
              'february': 2,
              'march'   : 3,
              'april'   : 4,
              'may'     : 5,
              'june'    : 6,
              'all'     : 7
            }

DAYS = {
              'monday'    : 0,
              'tuesday'   : 1,
              'wednesday' : 2,
              'thursday'  : 3,
              'friday'    : 4,
              'saturday'  : 5,
              'sunday'    : 6, 
              'all'       : 7
            }
try:
  while True:
    city = fnc.get_user_input('Would you like to see data for Chicago, New York or Washington?\n', 'city', CITIES)
    months = fnc.get_user_input(
      'Which month? January, February, March, April, May or June? Please type out the full month name or type "all" to get all months.\n', 'month', 
      MONTHS, return_multi=True)
    days = fnc.get_user_input(
      'Which week day?\nPlease type out the full day name (e.g. Monday, Tuesday, ..) or type "all" to get all days.\n', 'week day', 
      DAYS, return_multi=True)

    print('\n' + '#'*50)
    print('Calculating the statistics of the selected dataset ...')
    print('#'*50 + '\n')

    start_time = time.time()

    result_df = fn.get_df(city[0], months, days)
    result = fn.execute_analysis(result_df)

    month           = fnc.get_key(result[0]['month'], MONTHS).capitalize()
    day             = fnc.get_key(result[0]['day'], DAYS).capitalize()
    hour            = result[0]['hour']
    start_station   = result[1]['start']
    end_station     = result[1]['end']
    trip            = result[1]['trip']
    total_time      = result[2]['total']
    mean_time       = result[2]['mean']
    subscribers     = result[3]['subscriber']
    customers       = result[3]['customer']
    males           = result[3]['male']
    females         = result[3]['female']
    first_birth     = result[3]['min']
    recent_birth    = result[3]['max']
    common_birth    = result[3]['mode']

    fnc.format_stat(month, 
                    day, 
                    hour, 
                    start_station, 
                    end_station, 
                    trip, 
                    total_time,
                    mean_time,
                    subscribers, 
                    customers,
                    males, 
                    females,
                    first_birth,
                    recent_birth,
                    common_birth)

    print('\n' + '#'*40)
    print("This took %s seconds." % (time.time() - start_time))
    print('#'*40 + '\n')

    users_start = 0
    users_end = 5
    while True:
      desc_word = 'first' if users_start == 0 else 'next'
      show_user_data = fnc.get_simple_input('Would you like to see the ' + desc_word + ' 5 rows of the data set? (Enter yes or no): \n')
      if show_user_data.lower() in ['yes', 'y']:
        users_data = fn.get_users(result_df, users_start, users_end).to_json(orient='index')
        parsed_users_data = json.loads(users_data)
        print(json.dumps(parsed_users_data, indent=4, sort_keys=True))
        users_start += 5
        users_end += 5

      else:
        break

    restart = fnc.get_simple_input('\nWould you like to restart? (Enter yes or no): \n')
    if restart.lower() not in ['yes', 'y']:
      print('\nThanks for using this script.\nGoodbye!\n')
      break
    
except:
  pass