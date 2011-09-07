#!/usr/bin/python
#emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*- 
#ex: set sts=4 ts=4 sw=4 noet:
#------------------------- =+- Python script -+= -------------------------
"""
 @file      numpy_deps_groupped.py
 @date      Thu Aug 25 23:51:32 2011
 @brief


  Yaroslav Halchenko                                            Dartmouth
  web:     http://www.onerussian.com                              College
  e-mail:  yoh@onerussian.com                              ICQ#: 60653192

 DESCRIPTION (NOTES):

 COPYRIGHT: Yaroslav Halchenko 2011

 LICENSE: MIT

  Permission is hereby granted, free of charge, to any person obtaining a copy
  of this software and associated documentation files (the "Software"), to deal
  in the Software without restriction, including without limitation the rights
  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
  copies of the Software, and to permit persons to whom the Software is
  furnished to do so, subject to the following conditions:

  The above copyright notice and this permission notice shall be included in
  all copies or substantial portions of the Software.

  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
  THE SOFTWARE.
"""
#-----------------\____________________________________/------------------

__author__ = 'Yaroslav Halchenko'
__revision__ = '$Revision: $'
__date__ = '$Date:  $'
__copyright__ = 'Copyright (c) 2011 Yaroslav Halchenko'
__license__ = 'GPL'

numpy_dependents = {
    ('core', 'CCFF00')  : [
             "ipython",	#enhanced interactive Python shell
        "python-numpy",	#Numerical Python adds a fast array facility to the Python language
        "python-scipy",	#scientific tools for Python
              "sphinx",	#tool for producing documentation for Python projects
        ],
    ('neuro', 'FF0000') : [
               "brian",	#simulator for spiking neural networks
                "dipy",	#toolbox for analysis of MR diffusion imaging data
    "connectomeviewer",	#Interactive Analysis and Visualization for MR Connectomics
          "dicompyler",	#radiation therapy research platform
              "cfflib",	#Multi-modal connectome and metadata management and integration
             "nibabel",	#Python bindings to various neuroimaging data formats
                "nipy",	#Analysis of structural and functional neuroimaging data
              "nipype",	#Neuroimaging data analysis pipelines in Python
              "nitime",	#timeseries analysis for neuroscience data (nitime)
            "openmeeg",	#Python bindings for openmeeg library
            "psychopy",	#environment for creating psychology stimuli in Python
             "pydicom",	#DICOM medical file reading and writing
               "pyepl",	#module for coding psychology experiments in Python
             "pynifti",	#Python interface to the NIfTI I/O libraries
             "stimfit",	#A program for viewing and analyzing electrophysiological data
        ],
    ('data', '660000') : [
     "gnudatalanguage",	#Free IDL compatible incremental compiler
                "h5py",	#h5py is a general-purpose Python interface to hdf5
            "pytables",	#hierarchical database for Python based on HDF5
            "vitables",	#graphical tool to browse and edit PyTables and HDF5 files
              "pyfits",	#Python module for reading, writing, and manipulating FITS files
        ],
    ('ml', '6666FF') : [
                 "mdp",	#Modular toolkit for Data Processing
                "mlpy",	#high-performance Python package for predictive modeling
                "pebl",	#Python Environment for Bayesian Learning
            "pyevolve",	#Complete genetic algorithm framework
              "pymvpa",	#multivariate pattern analysis with Python
        "scikit-learn",	#Python modules for machine learning and data mining
              "shogun",	#Large Scale Machine Learning Toolbox
              "slicer",	#software package for visualization and image analysis - main application
        ],
    ('computing', '0099CC') : [
       "model-builder",	#graphical ODE simulator
     "python-networkx",	#tool to create, manipulate and study complex networks
           "pyentropy",	#Python module for estimation information theoretic quantities
          "pywavelets",	#Python extension implementing of wavelet transformations
             "openopt",	#Python module for numerical optimization
            "scitools",	#Python library for scientific computing
                "syfi",	#Python interface for SyFi
              "symeig",	#Symmetrical eigenvalue routines for NumPy
            "trilinos",	#parallel solver libraries within an object-oriented software framework
                "yade",	#Platform for discrete element modeling. Main optimized build
              "joblib",	#tools to provide lightweight pipelining in Python
            "pysparse",	#Sparse linear algebra extension for Python
    "python-biopython",	#Python library for bioinformatics
          "python-csa",	#The Connection-Set Algebra implemented in Python
        "libmpikmeans",	#Python bindings for MPIKmeans
               "mmass",	#Mass spectrometry tool for proteomics
            "petsc4py",	#Python bindings for PETSc libraries
        ],
    ('visualization', '9900FF') : [
          "matplotlib",	#Python based plotting system in a style similar to Matlab
             "mayavi2",	#scientific visualization package for 2-D and 3-D data
        "python-chaco",	#interactive plotting application toolkit
      "python-biggles",	#Scientific plotting package for Python
      "python-gnuplot",	#A Python interface to the gnuplot plotting program
             "pygrace",	#Python bindings for grace
       "python-visual",	#VPython 3D scientific visualization library
               "veusz",	#2D scientific plotting application with graphical interface
               "viper",	#minimalistic scientific plotter and run-time visualization module
              "guiqwt",	#efficient 2D data-plotting library
             "mypaint",	#Paint program to be used with Wacom tablets
              "plplot",	#Python support for PLplot, a plotting library
              "pygame",	#SDL bindings for games development in Python
        ],
    ('interfaces', '0011FF'): [
                 "rpy",	#Python interface to the GNU R language and environment
                "rpy2",	#Python interface to the GNU R language and environment (version 2)
        ],
    ('ide', '005588') : [
              "spyder",	#Python IDE for scientists
        ],
    ('games', 'FF00CC') : [
       "castle-combat",	#game where the player builds one castle and destroys others
          "childsplay",	#Suite of educational games for young children
          "fofix-dfsg",	#rhythm game in the style of Rock Band(tm) and Guitar Hero(tm)
         "singularity",	#game where one becomes the singularity
           "snowballz",	#fun RTS game featuring snowball fights with penguins
        ],
    ('misc', '666666') : [
                "astk",	#Graphical user interface for Code_Aster - server
               "babel",	#Scientific Interface Definition Language (SIDL) Python runtime
               "cclib",	#Parsers and algorithms for computational chemistry (Python module)
                "cmor",	#Python interface to CMOR
              "dballe",	#DB-ALL.e Python library for weather research
            "dockbarx",	#Task bar with grouping and group manipulation
              "dolfin",	#Python interface for DOLFIN
              "eficas",	#Graphical editor for Code Aster command files
            "epigrass",	#scientific tool for simulations and scenario analysis in network epidemiology
             "expeyes",	#Python library for expeyes
              "ferari",	#optimizations for evaluation of variational forms
                "fiat",	#tabulation of finite element function spaces
           "fonttools",	#Converts OpenType and TrueType fonts to and from XML
              "gamera",	#framework for building document analysis applications
           "gastables",	#compressible flow gas table modules for Python
            "gausssum",	#parse and display Gaussian, GAMESS, and etc's output
                "gdal",	#Python bindings to the Geospatial Data Abstraction Library
            "getfem++",	#Python interface to the GETFEM++ generic finite element library
            "gnuradio",	#Python bindings for GNU Radio core library
               "grass",	#Geographic Resources Analysis Support System
                 "gvb",	#visual simulator of 1 and 2-dimensional vibrations
             "instant",	#simple inlining of C / C++ code in Python
       "libvigraimpex",	#Python bindings for the C++ computer vision library
            "magics++",	#python support for Magics++
               "necpp",	#Python module for using NEC2++
           "ninix-aya",	#Interactive fake-AI Ukagaka-compatible desktop mascot program
               "nulog",	#Graphical firewall log analysis interface
            "panflute",	#GNOME panel applet to control several music players
             "pdb2pqr",	#Preparation of protein structures for electrostatics calculations
               "pymca",	#Python applications and toolkit for X-ray fluorescence analysis
               "pygtk",	#Python bindings for the GTK+ widget set
             "pyqwt3d",	#Python bindings of the QwtPlot3D library
              "pyqwt5",	#Python version of the Qwt5 technical widget library
             "pytango",	#API for the TANGO control system
       "python-enable",	#Drawing and interaction packages
   "python-whiteboard",	#Make your own electronic whiteboard
             "pytools",	#big bag of things supplementing Python standard library
           "pytrainer",	#tool for logging sport activities
            "swiginac",	#Python interface to GiNaC
       "tpclient-pywx",	#Thousand Parsec Python client
       "uncertainties",	#Python module for calculations with uncertainties
                "wsjt",	#weak-signal amateur radio communications
    ]
}
