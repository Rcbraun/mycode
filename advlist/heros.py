#!/usr/bin/env python3

# spiderman dictionary 
spiderman = {'name': 'Peter Parker',
            'relatives': 'Uncle Ben',
            'powers': ['Spider Senses','Webbing'],
            'qoutes': 'With great power comes great responsibility'}

# prints the 2nd 'value' for the key 'power'
print(spiderman['powers'][1])

batman = {'name': 'Bruce Wayne',
          'relatives': 'Damien',
          'powers': 'Wealth',
          'quotes': 'I am the night!'}

# prints the 'value' for the key 'quotes'
print(batman['quotes'])

superman = {'name': 'Clark Kent',
            'relatives': 'Martha Kent',
            'powers': 'Strength',
            'quotes': 'hope'}

# Methods
  #.get()
  #.keys()
  #.values()


# lists all values for the dictionary batman
print(batman.values())
  
# lists all the keys for the dictionary superman
print(superman.keys())


# .get() will allow the code to run even if there is no key that matches
print(spiderman.get('enemies','He lets no enimies live'))
