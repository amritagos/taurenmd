"""
Extract trajectory frames to individual files.

Normally used to extract frames to PDB topology files so those can
be inspected independently.

This client interface uses `MDAnalysis library <https://www.mdanalysis.org/>`_,
refer to our `Citing` page for instructions on how to cite.

.. note::

    Frame number is 0-indexed.

Examples
--------

    Extracts frames 11 to 49 (inclusive), remember frames index start
    at 0:

    >>> taurenmd fext topology.pdb trajectory.dcd -s 10 -e 50

    Extracts the first frame:

    >>> taurenmd fext topology.pdb trajectory.dcd -flist 0

    Extracts a selection of frames:

    >>> taurenmd fext topology.pdb trajectory.dcd -flist 0,10,23,345

    Frame file types can be specified:

    >>> taurenmd fext topology.pdb trajectory.dcd -p 10 -x .dcd

    Atom selection can be specified as well, the following extracts
    only the 'segid A' atom region of the first frame. Selection rules
    are as decribed for `MDAnalysis selection <https://www.mdanalysis.org/docs/documentation_pages/selections.html>`_

    >>> taurenmd fext topology.pdb trajectory.xtc -flist 0 -l 'segid A'

    Multiple trajectories can be given, they will be contatenated:

    >>> taurenmd fext top.pdb traj1.xtc traj2.xtc traj3.xtc -p 10

    Can also be used as main command:

    >>> tmdfext topology.pdb ...
"""
import argparse

from taurenmd import Path, log
from taurenmd.libs import libcli, libmda, libio
from taurenmd.logger import S

_help = 'Extracts single frames from trajectory.'
_name = 'fext'

ap = libcli.CustomParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    )

libcli.add_top_argument(ap)
libcli.add_traj_argument(ap)
libcli.add_slice_opt_arguments(ap)
libcli.add_selection_argument(ap)
libcli.add_flist_argument(ap)

ap.add_argument(
    '-f',
    '--prefix',
    help='String prefix for each file. Defaults to `frame_`.',
    default='frame_',
    )

ap.add_argument(
    '-x',
    '--ext',
    help='Extension of frame files. Defaulst to .pdb',
    default='.pdb',
    )


def load_args():
    """Load user arguments."""
    cmd = ap.parse_args()
    return cmd


def maincli():
    """Execute as main client."""
    cmd = load_args()
    main(**vars(cmd))
    return


def main(
        topology,
        trajectory,
        start=None,
        stop=None,
        step=None,
        flist=None,
        prefix='frame_',
        ext='pdb',
        selection='all',
        **kwargs):
    """Execute main client logic."""
    log.info('Starting...')
    
    u = libmda.load_universe(topology, *list(trajectory))
    
    frames_to_extract = libio.frame_list(
        len(u.trajectory),
        start=start,
        stop=stop,
        step=step,
        flist=flist,
        )

    log.info(S('extracting {} frames', len(frames_to_extract)))
    
    zeros = len(str(len(u.trajectory)))
    ext = ext.lstrip('.').strip()
    
    atom_group = u.select_atoms(selection)

    for frame in frames_to_extract:
        file_name = '{}{}.{}'.format(
            prefix,
            str(frame).zfill(zeros),
            ext,
            )

        atom_group.write(
            filename=Path(file_name),
            frames=[frame],
            )

        log.info(S('writen frame {}, to {}', frame, file_name))

    return


if __name__ == '__main__':
    maincli()
