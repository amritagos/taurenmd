"""
Copies the trajectory without solvent and extracts the first frame.
"""
import argparse

import mdtraj
import simtk.openmm.app as app

from taurenmd.libs import libcli

ap = libcli.CustomParser()

ap.add_argument(
    'topology',
    help='The .cif structure',
    )

ap.add_argument(
    'trajectory',
    help='The trajectory',
    )

ap.add_argument(
    '-o',
    '--output_pdb',
    help='Output PDB file.',
    default='production_noHOH.pdb',
    )

ap.add_argument(
    '-d',
    '--traj_output',
    help='The trajectory output.',
    default='production_noHOH.dcd',
    )


def load_args():
    cmd = ap.parse_args()
    return cmd


def maincli():
    
    cmd = load_args()
    main_script(**vars(cmd))


def main(
        topology,
        trajectory,
        output_pdb='production_noSol.pdb',
        traj_output='production_noSol.dcd',
        **kwargs,
        ):

    trj = mlibio.mdtraj_load_traj(topology, trajectory)
    trj.remove_solvent(inplace=True)
    trj[0].save_pdb(output_pdb)
    trj.save(traj_output)


if __name__ == '__main__':
    maincli()