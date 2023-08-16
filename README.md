# orth_rubrene
Code for generating in orthorhombic rubrene crystal geometries in GROMACS format

Orthorhombic crystal geometry is based on the data from Jurchescu, O. D., Meetsma, A., & Palstra, T. T. (2006). Low-temperature structure of rubrene single crystals grown by vapor transport. Acta Crystallographica Section B: Structural Science, 62(2), 330-334. 

rubrene_crystalize.py
Python code generating the crystal geometry. The number of repeating crystal cells in each dimension can be adjusted on line #3.

rubrene_center.gro
Geometry file containing a single rubrene molecule centered at (0, 0, 0)

Requires numpy
