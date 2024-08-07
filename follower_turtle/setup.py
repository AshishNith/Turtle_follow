from setuptools import setup

package_name = 'follower_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'follower_turtle.follower_turtle',
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Follower Turtle for TurtleSim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'follower_turtle = follower_turtle.follower_turtle:main',
        ],
    },
)
