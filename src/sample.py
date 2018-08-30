import sys
import os
from lib import manager

def main():

    ## Get config
    # m.config['section']['key']

    ## Get args
    # m.args.options

    ## Logger sample
    for n in range(1, 31):
        if n % 3 == 0 and n % 5 == 0:
            m.logger.debug("FizzBuzz")
        elif n % 3 == 0:
            m.logger.debug("Fizz")
        elif n % 5 == 0:
            m.logger.debug("Buzz")
        else:
            m.logger.debug(n)

if __name__ == '__main__':
    program_name = os.path.splitext(os.path.basename(__file__))[0]
    with manager.Manager(program_name) as m:
        try:
            main()

        except Exception as e:
            m.logger.exception(e)
            sys.exit(1)

