from setuptools import setup, find_packages

packages = [
    "geopandas==0.7.0",
    "numpy==1.18.4",
    "pandas==1.0.3",
    "scipy==1.4.1"
]

setup(name='globeloc',
      version='0.1',
      description='A global data array framework',
      url='http://github.com/fhk/globeloc',
      author='Fabion Kauker',
      author_email='',
      license='MIT',
      packages=find_packages(),
      install_requires=packages,
      zip_safe=False)
