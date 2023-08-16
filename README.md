# orth_rubrene
Code for generating orthorhombic rubrene crystal geometries in a GROMACS (.gro) format. The corresponding topology files can be found in the SI of

Orthorhombic crystal geometry is based on the data from Jurchescu, O. D., Meetsma, A., & Palstra, T. T. (2006). Low-temperature structure of rubrene single crystals grown by vapor transport. Acta Crystallographica Section B: Structural Science, 62(2), 330-334. 

make_orth_rubrene.py

Python code generating the crystal geometry. The number of repeating crystal cells in each dimension and the output filename can be adjusted on lines #5-7.

rubrene_center.gro

Geometry file containing a single rubrene molecule centered at (0, 0, 0).

test_output.gro

Example output (can be visualized in eg. VMD). 


Requires numpy
