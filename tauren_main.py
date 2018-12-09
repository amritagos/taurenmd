"""
MANAGES TAUREN WORKFLOW

Copyright © 2018-2019 Tauren-MD Project

Contributors to this file:
- João M.C. Teixeira (https://github.com/joaomcteixeira)

Tauren-MD is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Tauren-MD is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Tauren-MD. If not, see <http://www.gnu.org/licenses/>.
"""

import argparse

from tauren import system, logger
from tauren.core import openlib, transform

log = logger.get_log(__name__)
ap = argparse.ArgumentParser(description=__doc__)

# Mandatory
ap.add_argument(
    'config',
    help="Tauren-MD configuration (.json) file"
    )

# Options
ap.add_argument(
    '--trajectory',
    default=None,
    help="Trajectory file ({})".format(system.trajectory_types)
    )

ap.add_argument(
    '--topology',
    default=None,
    help="Topology file ({})".format(system.topology_types)
    )

cmd = ap.parse_args()

# set path configuration
conf = openlib.load_json_config(cmd.config)
conf.trajectory = cmd.trajectory or conf.trajectory
conf.topology = cmd.topology or conf.topology

    
traj = openlib.load_traj(conf.trajectory, conf.topology)

if conf.reduce_equidistant:
    traj = transform.reduce_equidistant(traj, conf.reduce_equidistant_step)

if conf.remove_solvent:
    traj = transform.remove_solvent(traj)