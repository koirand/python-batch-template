import sys
import os
from lib import manager

def main():

    # Write processing here

if __name__ == '__main__':
    program_name = os.path.splitext(os.path.basename(__file__))[0]
    with manager.Manager(program_name) as m:
        try:
            main()

        except Exception as e:
            m.logger.exception(e)
            sys.exit(1)

