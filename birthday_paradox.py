"""The birthday paradox simulation
Tags: short, math, simulation
    """

import datetime,random

def getBirthdays(numberOfBirthdays):
    """ Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(numberOfBirthdays):
        # The year is unimportant for our simulation, as long as all
        # birthdays have the same year.
        startOfYear = datetime.date(2001,1,1)

        # Get a random day into the year:
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
        # print(randomNumberOfDays) # DEBUG
    return birthdays


def getMatch(birthdays):
    """Returns the date object of a birthday that occurs more than once
    in the birthdays list."""
    # if len(birthdays) == len(set(birthdays)):
    #     return None # All birthdays are unique, so return None.

    # Compare each birthday to every other birthday:
    for a, birthdayA in enumerate(birthdays):
      #  print(a,' -------->',str(birthdayA),'\n',enumerate(birthdays)) # DEBUG
        for b, birthdayB in enumerate(birthdays[a+1:]):
            # print(str(enumerate(birthdays)),'---------',str(enumerate(birthdays[a+1:])))  # DEBUG
         #   print(b, ' -------->', str(birthdayB), '\n', enumerate(birthdays[a+1:]))  # DEBUG
         #    print(birthdayA, '------------', birthdayB)  # DEBUG
            if birthdayA == birthdayB:
               # print(birthdayA,'------------',birthdayB)  # DEBUG
                return birthdayA # Return the matching birthday.


# Display the intro:
print('''Birthday paradox, by slipcy
(It's nor actually a paradox, it's just a surprising result.)
''')

# Set up a tuple of month names in order:
MONTHS = ('Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec')

while True: # Keep asking until the user enters a valid amount.
    print('How many birthdays shall I generate? (Max 100)')
    response = input('> ')
    if response.isdecimal() and (0 < int(response) <= 100):
        numBDays = int(response)
        break # User has entered a valid amount.
print()

# Generate and display the birthdays:
print('Here are', numBDays,'birthdays:')
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        # Display a comma for each birthday after the first birthday.
        print(', ',end ='')
    monthName = MONTHS[birthday.month - 1]
    dateText = '{} {}'.format(monthName, birthday.day)
    print(dateText,end='')

print()
print()

# Determine if there are two birthdays tha match.
match = getMatch(birthdays)

# Display the results:
print('In this simulation, ', end='')
if match != None:
    monthName = MONTHS[match.month - 1]
    dateText = '{} {}'.format(monthName, match.day)
    print('multiple people have a birthday on', dateText)
else:
    print('there are no matching birthdays.')
print()

# Run through 100,000 simulation:
print('Generating', numBDays,'random birthdays 100,000 time...')
input('Press Enter to begin...')

print('Let\'s run another 100,000 simulation.')
simMatch = 0 # How many simulations had matching birthdays in them.
for i in range(100_000):
    # Report on the progress every 10,000 simulations:
    if i % 10_000 == 0:
        print(i,' simulations run...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch = simMatch + 1
print('100,000 simulations run.')

# Display simulation results:
probability = round(simMatch / 100_000 * 100,3)
print('Out of 100,000 simulations of', numBDays, 'people, there was a')
print('matching birthday in that group', simMatch, 'times. This means')
print('that', numBDays, 'people have a', probability, '% chance of')
print('having a matching birthday in their group.')
print('That\'s probably more than you would think!')

