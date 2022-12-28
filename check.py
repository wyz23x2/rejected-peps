if __name__ == '__main__':
    import os
    import sys
    import argparse
    os.chdir(os.getcwd())
    parser = argparse.ArgumentParser('check')
    parser.add_argument('--nt', '--no-tests', action='store_true', dest='nt',
                        help='Disable unit tests.')
    parser.add_argument('-g', '--green-only', action='store_true', dest='g',
                        help='Force use of green to run unit tests. ')
    parser.add_argument('-u', '--unittest-only', action='store_true', dest='u',
                        help='Force use of unittest directly to run unit tests.')
    parser.add_argument('-r', '--coverage', action='count', default=0, dest='r',
                        help='Run coverage using green. '
                        'Specify 2+ times to keep the .coverage file.')
    parser.add_argument('--n8', '--nf', '--no-flake8',
                        action='store_true', dest='nf',
                        help='Disable flake8 checking.')
    parser.add_argument('--nb', '--no-bandint', action='store_true',
                        help='Disable bandint security checking.')
    parser.add_argument('-f', '--fail', action='store_true', dest='f',
                        help='Fail and exit when any source is unavailable.')
    args = parser.parse_args()
    if args.g and args.u:
        parser.error('Cannot specify both -g and -u')
    os.system('')
    # Test suite
    if not args.nt:
        print('\033[1m==== TEST SUITE ====\033[m')
        try:
            if args.u:
                raise ImportError
            import green.cmdline as g
        except ImportError:
            if args.g and args.f:
                print('\033[1;31mgreen not found, program exit\033[m', file=sys.stderr)
                sys.exit(1)
            elif args.g:
                print('\033[33mgreen not found, test suite skipped\033[m',
                      file=sys.stderr)
            else:
                os.system('py ./rejected_peps/test.py')
        else:
            g.main(['-vv', *(('-r',) if args.r else ())])
            if args.r == 1:
                try:
                    os.remove('.coverage')
                except OSError:
                    pass
        print()
    # Flake8
    if not args.nf:
        print('\033[1m==== Flake8 ====\033[m')
        try:
            import flake8  # NOQA
        except ImportError:
            if args.f:
                print('\033[1;31mflake8 not found, program exit\033[m', file=sys.stderr)
                sys.exit(1)
            print('\033[33mflake8 not found, check skipped\033[m',
                  file=sys.stderr)
        else:
            del flake8
            try:
                f = os.popen('flake8 rejected_peps')
                c = f.read()
            finally:
                f.close()
            if c.strip():
                print(c)
            else:
                print('\033[32mChecks all run, no violations reported.\033[m\n')
    if not args.nb:
        print('\033[1m==== Bandit ====\033[m')
        try:
            import bandit  # NOQA
        except ImportError:
            if args.f:
                print('\033[1;31mbandit not found, program exit\033[m', file=sys.stderr)
                sys.exit(1)
            print('\033[33mbandit not found, security check skipped\033[m',
                  file=sys.stderr)
        else:
            del bandit
            os.system('py -m bandit -r rejected_peps')
