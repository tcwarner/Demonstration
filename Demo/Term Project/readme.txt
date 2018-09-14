This was my final project for 15-112 Fundamentals of Programming and Computer Science. This project takes inputs of chemical formulas and draws them in 3D. See description.txt for more information.

To install vpython:
In the command prompt, enter:
	pip install vpython
If you are running Anaconda, enter:
	conda install -c vpython vpython
All other modules are built into Python.

How to run the 3d Molecule Viewer:
Run the file entitled "15-112 Molecule Drawer.py" in Python 3 after installing vpython.

How to use this application:
In all cases, correct capitalization of elemental symbols must be used. Do not enter parentheses or any punctuation. For example, enter "Ar", not "ar" or "AR".
Ionic mode:
Type in the empirical formula of the desired ionic compound and click on draw or press enter to draw it in vpython. Alternatively, enter the known ions and their oxidation states. Two formula units of the compound are drawn in their known lattices. If an input is invalid, simply press the back button to return to the input menu.
Covalent mode:
Type in formula of the desired compound with each group in the chain separated by a "%". For example, ethanol (CH3CH2OH) should be entered as "CH3%CH2%OH".
The demo mode shows the capabilities of the application.
