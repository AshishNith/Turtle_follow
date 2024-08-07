from setuptools import setup

package_name = 'teleop_turtle'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    py_modules=[
        'teleop_turtle.teleop_turtle',
    ],
    install_requires=['setuptools', 'pynput'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Teleoperation for TurtleSim',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_turtle = teleop_turtle.teleop_turtle:main',
        ],
    },
)
