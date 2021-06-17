# Stuff from R

The most hated Python module ever written. These are routines I made when I started using Python. As I had previously used R as an interpreted language, the module became "stuffr", meaning stuff from R. Unfortunately most of my code has a dependency to this module. 

You can install it using:
> pip install -i https://test.pypi.org/simple/ stuffr

# Howto

This is how to upload a project to pipy. This is mainly a note to self, as this is the first project I have uploaded to pypi:

~~~
python3 -m venv /tmp/venv
source /tmp/venv/bin/activate
pip install build
pip install twine
python3 -m build
python3 -m twine upload dist/stuffr-1.0.0.tar.gz 
~~~
