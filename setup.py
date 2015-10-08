from setuptools import setup

setup(
     name='train_vid_bot',
     version='0.1dev',
     namespace_packages=['recipes'],
     install_requires=['recipe', 'google-api-python-client'],
     dependency_links = ['git+https://github.com/elonbing/recipe.git#egg=recipe']
)
