from setuptools import setup

def parse_requirements(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if line.strip()]
    
requirements = parse_requirements('requirements.txt')

setup(
    name='dev_aberto_Grupo5',
    version='0.1',
    packages=['dev_aberto'],
    scripts=['scripts/hello.py'],
    install_requires=requirements,
    url='https://github.com/rafakatri/python-package',
    license='MIT',
    author='Ariel Leventhal and Rafael Katri',
    author_email='your@email.com',
    description='Simple python package',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
)