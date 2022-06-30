#!/usr/bin/python3
# 2-args.py

if __name__ == "__main__":
    """Print the number of and list of arguments."""
    import sys
   
   av = sys.argv
   l_av = len(av) - 1

   if l_av > 1:
       print(l_av, 'arguments:')
       for i in range(1, l_av + 1):
           print('{:d}: {}'.format(i, av[i]))
       elif l_av == 1:
           print(l_av, 'argument:')
           for i in range(1, l_av + 1):
               print('{:d}: {}'.format(i, av[i]))
           elif l_av == 0:
               print(l_av, 'arguments.')
