import sys
from distutils.core import setup

if __name__ == "__main__":
    if sys.version_info[:2] < (3, 6):
        print('Requires Python version 3.6 or later')
        sys.exit(-1)

    setup(
        name='data_structures',
        packages=['data_structures'],
        version='1.0',
        description='Dependências para a aula prática 03 de Engenharia de Software 2',
        author='Thiago Martin Poppe'
    )
