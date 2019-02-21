from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='begoneads',
      version='0.0.3',
      description='BeGoneAds puts some popular hosts file lists into the hosts file as a adblocker measure.',
      long_description=readme(),
      url='http://github.com/anned20/begoneads',
      entry_points = {
          'console_scripts': ['begoneads=begoneads.begoneads:cli'],
      },
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: System :: Networking',
      ],
      author='Anne Douwe Bouma',
      author_email='annedouwe@bouma.tech',
      license='MIT',
      packages=['begoneads'],
      install_requires=[
          'click',
          'requests',
          'tqdm',
      ],
      zip_safe=False
)
