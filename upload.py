import argparse as ap
import os, sys
import subprocess
os.system('')
a = ap.ArgumentParser()
a.add_argument('-v', '--verbose', action='count', default=0,
               help='print more information', dest='v')
a.add_argument('-s', '--skip-check', action='store_true', help='skip test check', dest='skip')
a.add_argument('-b', '--build-only', '--no-upload', action='store_true',
               help='only build, do not upload to PyPI', dest='b')
a.add_argument('-k', '--keep-build', action='store_true',
               help='keep the build directory', dest='k')
a.add_argument('-w', '--force-wheels', action='store_true',
               help='abort if any wheel build fails', dest='w')
a.add_argument('--no-wheels', action='store_true',
               help='do not build wheels', dest='nw')
a.add_argument('--force-old', action='store_true',
               help='force build wheels for Python 3.7 (support will end on Jan 27, 2023)',
               dest='f')
r = a.parse_args()
if r.nw and (r.f or r.w):
    a.error('argument --no-wheels: not allowed with argument -w or --force-old')
if not r.skip:
    c = subprocess.run('py check.py').returncode
    if c != 0:
        print(f'\033[31mTest failed, process abort\033[m', file=sys.stderr)
        sys.exit(c)
try:
    os.rmdir('dist')
except OSError:
    pass
if not r.nw:
    for v in (*(['cp37'] if r.f else ()), 'cp38', 'cp39', 'cp310', 'cp311'):
        for p in ('win_amd64', 'win32'):
            c = subprocess.run('py -Wignore setup.py bdist_wheel -q '
                               f'--python-tag={v} --plat-name={p}', shell=True,
                               capture_output=(r.v < 1)).returncode
            if c != 0:
                print(f'\033[31mWheel build for {v}/{p} failed ({c})\033[m', file=sys.stderr)
                if r.w:
                    sys.exit(c)
            elif r.v < 1:
                print(f'\033[32m{v}/{p} OK\033[m')
        for x in os.listdir('dist'):
            try:
                n = x.replace('none', v)
                os.replace(f'dist/{x}', f'dist/{n}')
            except OSError as e:
                print(f'\033[31mWheel build for {v}/{p} failed: {e!s}\033[m', file=sys.stderr)
                if r.w:
                    sys.exit(c)
if not r.k:
    try:
        os.rmdir('build')
    except OSError:
        pass
c = subprocess.run('py -Wignore setup.py -q sdist',
                   capture_output=(r.v < 1), shell=True).returncode
if c != 0:
    print(f'\033[31mPackage build failed, process abort\033[m', file=sys.stderr)
    sys.exit(c)
if r.b:
    sys.exit()
c = subprocess.run('twine upload dist/*', shell=True).returncode
sys.exit(c)
