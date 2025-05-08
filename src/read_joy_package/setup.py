from setuptools import find_packages, setup

package_name = 'read_joy_package'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nakajima',
    maintainer_email='1e8ec3@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'read_joy_node = read_joy_package.read_joy_node:main',
            'sub_joy = read_joy_package.sub_joy:main',
            'whillstates_sub = read_joy_package.whillstates_sub:main',
        ],
    },
)
