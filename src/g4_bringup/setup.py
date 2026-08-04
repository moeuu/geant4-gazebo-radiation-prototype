from glob import glob
import os
from pathlib import Path

from setuptools import setup

package_name = 'g4_bringup'

data_files = [
    ('share/ament_index/resource_index/packages', [os.path.join('resource', package_name)]),
    (f'share/{package_name}', ['package.xml']),
    (f'share/{package_name}/config', glob('config/*.yaml')),
    (f'share/{package_name}/launch', glob('launch/*.launch.py')),
    (f'share/{package_name}/models', glob('models/*.sdf')),
    (f'share/{package_name}/robots', glob('robots/*.sdf')),
    (f'share/{package_name}/worlds', glob('worlds/*')),
]

packages = [package_name] if Path(package_name).is_dir() else []

setup(
    name=package_name,
    version='0.0.2',
    packages=packages,
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Eiji Morita',
    maintainer_email='moeuu@users.noreply.github.com',
    description='One-command bringup for Gazebo (headless), ros_gz bridge, Geant4 node, and viz nodes.',
    license='MIT',
    entry_points={
        'console_scripts': [
            'robot_measurement_node = g4_bringup.robot_measurement_node:main',
            'source_spawner_node = g4_bringup.source_spawner_node:main',
            'measurement_sweep = g4_bringup.measurement_sweep:main',
            'measurement_sweep_edep = g4_bringup.measurement_sweep_edep:main',
        ],
    },
)
