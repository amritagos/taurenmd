---
title: 'taurenmd: A command-line interfaced hub for analysis routines in Molecular Dynamics.'
tags:
  - Python
  - Molecular Dynamics
  - Structural Biology
  - Proteins
  - DNA
  - RNA
  - Biochemistry
authors:
  - name: João M.C. Teixeira
    orcid: 0000-0002-9113-0622
    affiliation: 1
affiliations:
  - name: Program in Molecular Medicine, Hospital for Sick Children, Toronto, Ontario M5G 0A4, Canada
  - index: 1
date: 27 February 2020
bibliography: paper.bib
---

# Summary


![taurenmd logo.\label{fig:logo}](../docs/logo/taurenmdlogo_readme.png)

# Implementation

**taurenmd** provides highly parametrizable command-line interfaces that automatize complex operations of Molecular Dynamics (MD) data handling and analysis in unitary executions, which, *per se*, represent conceptual ideas; for example, the manipulation of raw MD data or the calculation of structural parameters (*RMSDs, RMSFs, etc...*). Command-line operations are created by orchestrating multiple individualized functions in a cooperative fashion. These single-logic functions coded in the core of *taurenmd*'s library which facilitates their unit-testing and sharing among all interfaces. *taurenmd*'s architecture design is, therefore, simple, yet highly modular, flat, easy to read, and extensible.

To operate MD data, *taurenmd* uses third-party MD analysis libraries. Currently, *taurenmd* imports MDAnalysis [@mda1; @mda2], MDTraj [@mdt] and OpenMM [@OpenMM] and they are used depending on the requirements of each command-line client.

The command-line interface of *taurenmd* is *hierarchic*, where `taurenmd` is the main entry point and the different interfaces exist as *subroutines*, for example:

```bash
# help instructions for the main taurenmd entry point
$ taurenmd -h
# an execution example
$ taurenmd [SUBROUTINE] [OPTIONS]
# querying help for a specific subroutine
$ taurenmd report -h
```

At the date of publication, *taurenmd* provides ten different command-line interfaces; all of them, their arguments, and functionalities, are thoroughly described in the project's documentation under *Command-line interfaces*. Likewise, all individual functional operations provided are open, fully documented, and can be imported and used by other projects if desired.

To invite community contributions, we provide a client template file with detailed instructions that developers can use to implement new command-line workflows themselves. The building blocks required to build command-line clients are also extensively documented in the `libs/libcli.py` module, where new blocks can also be added if needed. New logical operations can simply be implemented in the library core and used in clients. Complete instructions on how to contribute to the project are provided in the documentation. This project is hosted at GitHub and we provide extensive Continuous Integration tests and explicit style and format configurations to guide developers. *taurenmd* follows Semantic Versioning 2.0 [@version] and we favor agile develop/deployment.

# Installation

**taurenmd** is deployed in the Python ecosystem and is available for direct down at PyPI [@pypitaurenmd]:

```bash
$ pip3 install taurenmd[all]
```

*taurenmd* code uses only Python provided interfaces and is, therefore, compatible with any platform able to execute Python itself [@pythondev]. However, the different Molecular Dynamics analysis libraries imported have very different deployment strategies and we cannot guarantee those will function in all OSes; we do guarantee *taurenmd* works fully on Ubuntu 18.04 LTS running Anaconda as Python package manager. We advise reading the detailed installation instructions provided in the project's documentation.

# Use cases

*taurenmd* current version has ten command-line interfaces that execute different analysis or data manipulation routines. Extensive usage examples are provided in the documentation website or by the command:

```bash
$ taurenmd -h
```

Here we show a very common case where `trajedit` interface is used for data manipulation and transformation:

```bash
$ taurenmd trajedit topology.pdb trajectory.xtc -d traj_s50_e500_p10.xtc \
> -s 50 -e 500 -p 10 -l 'segid A'
```

The latter extracts a subtrajectory spanning frames 50 to 500 (exclusive) with a step interval of 10 frames, and only for atoms for the `'segid A'` atom group; in this particular case, we make use of MDAnalysis library [@mda1; @mda2] to handle the data.

# Acknowledgments

The initial concept of this project was largely inspired in the pdb-tools project `one script one action` idea [@pdbtools]; here we pushed that concept further. The author deeply thanks João P.G.L.M. Rodrigues (ORCID: 0000-0001-9796-3193) for mentoring on MD simulations and data analysis and to Susana Barrera-Vilarmau (ORCID: 0000-0003-4868-6593) for her intensive usage of the program since the very first versions and all the discussions, feedback and suggestions on building a user-friendly interface. The project's repository layout and Continuous Integration setup was based on `cookiecutter-pylibrary` [@cc] with final personal modifications by J.M.C.T..

# References