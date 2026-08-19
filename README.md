# Geant4–Gazebo Radiation Simulation Prototype

> [!IMPORTANT]
> This repository is a legacy research prototype and is being preserved for
> reference. It is no longer under active development. For current radiation
> simulation work, use
> [radiation-simulation-runtime](https://github.com/moeuu/radiation-simulation-runtime).

This project connects a Geant4 energy-deposition simulation to a ROS 2 and
Gazebo robot environment. Robot odometry drives the detector state, Geant4
publishes deposited energy (`Edep`), and ROS 2 nodes provide plots, histograms,
and a two-dimensional `OccupancyGrid` visualization.

## What is preserved here

- A ROS 2 interface around an embedded Geant4 application
- A Gazebo Harmonic world and differential-drive robot model
- ROS–Gazebo bridges for `/odom` and `/cmd_vel`
- Edep plotting, histogram, CSV, and occupancy-grid nodes
- Prototype waypoint and rotating-shield measurement workflows

The repository remains useful as an example of the original ROS 2/Gazebo
integration. It should not be treated as the maintained radiation-physics
runtime.

## Repository layout

```text
src/
├── g4_bringup/       Integrated launch files, Gazebo assets, and workflows
├── g4_interfaces/    Custom ROS 2 messages and services
├── g4_mapper/        Edep-to-OccupancyGrid mapping
├── g4_viz/           Plot, histogram, and grid visualization nodes
└── geant4_embed/     Embedded Geant4 ROS 2 node
```

Robot measurement parameters are kept in
`src/g4_bringup/config/robot_measure.yaml`. Generated `build/`, `install/`,
`log/`, and `results/` directories are intentionally ignored.

## Requirements

The prototype was developed for:

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic and `ros_gz`
- Geant4 11.2.x
- `colcon`, NumPy, and Matplotlib

No container or reproducible environment definition is included. Compatibility
with newer dependency versions has not been verified.

## Build

Run these commands from the repository root:

```bash
source /opt/ros/jazzy/setup.bash
rosdep update
rosdep install --from-paths src --ignore-src -r -y
colcon build --symlink-install
source install/setup.bash
```

## Run

The maintained entry point within this archived codebase is the integrated
launch file:

```bash
ros2 launch g4_bringup measurement_bringup.launch.py
```

Useful launch options include:

```bash
# Open the Gazebo GUI
ros2 launch g4_bringup measurement_bringup.launch.py headless:=false

# Enable the prototype waypoint measurement node
ros2 launch g4_bringup measurement_bringup.launch.py \
  enable_autonomy:=true \
  waypoints_flat:="[0.0,0.0,1.0,0.0,1.0,1.0]" \
  rotation_angles:="[0,45,90,135,180,225,270,315]"

# Disable individual visualizers
ros2 launch g4_bringup measurement_bringup.launch.py \
  plot:=false hist:=false grid:=true

# Choose an explicit result directory
ros2 launch g4_bringup measurement_bringup.launch.py \
  csv_dir:="$PWD/results"
```

With autonomy enabled, `robot_measurement_node` publishes directly to
`/cmd_vel`; the launch file's ROS-to-Gazebo bridge consumes that topic and
forwards commands to DiffBot. The default visualizer output directory is
`$XDG_STATE_HOME/geant4-gazebo-radiation-prototype/results` when that variable
contains a valid absolute path, or
`~/.local/state/geant4-gazebo-radiation-prototype/results` when
`XDG_STATE_HOME` is unset. Set `csv_dir` to override it.

The configuration file can also be passed to the measurement node when it is
run independently:

```bash
ros2 run g4_bringup robot_measurement_node --ros-args \
  --params-file src/g4_bringup/config/robot_measure.yaml
```

## Known limitations

- The radiation model and detector/shield geometry are prototype-specific.
- The primary output is Edep summary data, not a validated detector spectrum.
- Execution is serial and was intended for small experimental runs.
- Multi-isotope scenes, detailed backgrounds, dead time, and full experiment
  provenance are outside this implementation.
- The code predates the current runtime interfaces and has not been migrated to
  them.

## Archive status

Before archiving, the obsolete root-level step scripts were removed, example
configuration was moved into the ROS package, and machine-specific asset paths
were replaced with portable package-relative paths. Git history remains the
source of truth for the earlier experimental commands.

## License

This repository is available under the [MIT License](LICENSE).
