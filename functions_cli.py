def get_user_input(msg, item_name, ref, item_type=str, return_multi=False):
    '''
        A function to get user different inputs for city, months and days
        It enables the user can select only one city but multiple or all months and days

            Parameters:
                msg (str)               : The input message as a string
                ref (dict)              : The dictionary to validate the inputs against its keys
                item_type (data type)   : The datatype of the required input
                return_multi (bool)     : True for single input and False for multiple inputs required
            
            Returns:
                A list containing the unique value(s) of the key(s) the user presented as (an) input(s)
    '''

    user_inputs = []
    another_input = 'y'

    # For multiple inputs (Months and Days)
    if return_multi:
        while return_multi:

            # If the answer was yes/y
            if another_input in ('yes', 'y'):
                try:
                    user_input = item_type(input(msg)).lower()
                except KeyboardInterrupt:
                    print('\nGoodbye!\n')
                except:
                    print('Something went wrong! Please try again.')

                # Check if the input is in the referenece dictionary keys    
                if user_input in ref.keys():
                    
                    # Add all ref dictionary keys if input was 'all'
                    if user_input == 'all':
                        for item in ref:
                            user_inputs.append(ref[item])
                        user_inputs.pop(len(user_inputs)-1)
                        break
                    
                    # Append each input to the user_inputs list
                    else :
                        user_inputs.append(ref[user_input])

                        # Asking for another input
                        try:
                            another_input = input('Do you want to add another {}?\nType "yes or y" for yes, or "no or n" for no: '
                            .format(item_name)).lower()
                        except KeyboardInterrupt:
                            print('\nGoodbye!\n')
                        except:
                            print('Something went wrong! Please try again.')
                        
                        if another_input not in ('yes', 'y', 'no', 'n'):
                            try:
                                another_input = input('Invalid input .. Type "yes or y" for yes, or "no or n" for no: ').lower()
                            except KeyboardInterrupt:
                                print('\nGoodbye!\n')
                            except:
                                print('Something went wrong! Please try again.')   
                else:   
                    print('Please enter a correct {}'.format(item_name))
                    continue
            
            # If the answer was no/n
            elif another_input in ('no', 'n'):
                break
            
            # If the answer was random
            else:
                try:
                    another_input = input('Invalid input .. Type "yes or y" for yes, or "no or n" for no: ').lower()
                except KeyboardInterrupt:
                    print('\nGoodbye!\n')
                except:
                    print('Something went wrong! Please try again.')
                continue
    
    # For single input (City)
    else:
        while True:
            try:
                user_input = item_type(input(msg)).lower()
            except KeyboardInterrupt:
                print('\nGoodbye!\n')
            except:
                print('Something went wrong! Please try again.')
            
            if user_input in ref:
                user_inputs.append(ref[user_input])
                break
            else:
                print('Please enter a correct {}'.format(item_name))
                continue
    
    # Making the user inputs list items unique to avoid repeated data in the choosen range.
    inputs_set = set(user_inputs)
    return list(inputs_set)

def format_stat(month, 
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
                common_birth):

    '''
        A function to format the json data returned from execute_analysis frunction inported from the functions 
        package and print it in a readable format.
    '''

    ####################
    # Time Stats
    ####################

    print('\n' + '#'*20)
    print('Time Stats')
    print('#'*20 + '\n')

    # display the most common month
    print('The most common month is             : {}\n'.format(month))

    # display the most common day of week
    print('The most common day of the week is   : {}\n'.format(day))

    # display the most common start hour
    print('The most common hour is              : {}\n'.format(hour))

    ####################
    # Station Stats
    ####################

    print('\n' + '#'*20)
    print('Station Stats')
    print('#'*20 + '\n')

    # display most commonly used start station
    print('The most common start station is     : {}\n'.format(start_station))

    # display most commonly used end station
    print('The most common end station is       : {}\n'.format(end_station))

    # display most frequent combination of start station and end station trip
    print('The most common trip is : from {}\n'.format(trip))

    ####################
    # Duration Stats
    ####################

    print('\n' + '#'*20)
    print('Duration Stats')
    print('#'*20 + '\n')

    # display total travel time
    print('Total travel time is                 : {}\n'.format(total_time))

    # display mean travel time
    print('Mean travel time is                  : {}\n'.format(mean_time))

    ####################
    # User Stats
    ####################

    print('\n' + '#'*20)
    print('User Stats')
    print('#'*20 + '\n')

    # Display counts of user types
    print('Count of "Subscriber" user type is   : {}\nCount of "Customer" user type is     : {}'
    .format(subscribers, customers))

    # Display counts of gender
    if males and females:
        print('Count of "Male" users is             : {}\nCount of "Female" users is           : {}'
        .format(males, females))

    # Display earliest, most recent, and most common year of birth
    if first_birth and recent_birth and common_birth:
        print('Earliest date of birth is            : {}\nMost recent date of birth is         : {}\nMost common year of birth is         : {}'
        .format(first_birth, recent_birth, common_birth))

def get_key(val, my_dict): 
    '''
        A simple function to return the key of speicifc value in a dictionary

            Parameters:
                val                : The value to find its key
                my_dict (dict)     : The dictionary to get the key from
            
            Returns:
                The key for the presented value
    '''
    for key, value in my_dict.items(): 
         if val == value: 
             return key 
    return "Doesn't exist!"
    
def get_simple_input(msg):
    try:
      result = input(msg)
      return result
    except KeyboardInterrupt:
      print('\nGoodbye!')