CLASS: Cosmic Linear Anisotropy Solving System  {#mainpage}
==============================================

Authors: Julien Lesgourgues, Thomas Tram, Nils Schoeneberg

with several major inputs from other people, especially Benjamin
Audren, Simon Prunet, Jesus Torrado, Miguel Zumalacarregui, Francesco
Montanari, Deanna Hooper, Samuel Brieden, Daniel Meinert, Matteo Lucca, etc.

For download and information, see http://class-code.net

SPartAcous
-----------------------------------

This version of CLASS has been modified by Manuel A. Buen-Abad and Taewook Youn (April 2022), in order to include the SPartAcous model (partially acoustic dark matter with a step).

In addition to the usual CLASS code, we have included two important sets of files.

1. The `Mathematica` notebook `./notebooks/spartacous_initial_conditions.nb` describes the superhorizon initial conditions of the adiabatic perturbations of the various components of the SPartAcous model. These are different from the standard case due to the presence of the mass threshold in the dark radiation.

2. The folder `./mp-mod_files/` contains:
  * example `.param` files in the `input/` folder,
  * the H_0 and S_8 likelihoods in the `likelihoods/` folder, and
  * our modified version of the `data.py` (in which we include our own version of the SPartAcous parameters whenever we want to scan with a flat log10 prior) in `mp-mod_data.py`.

If you use `class_spartacous` in any published work, please cite the appropriate CLASS papers, as well as the SPartAcous papers [Buen-Abad, Chacko, Kilic, Marques-Tavares, Youn (2022)](https://arxiv.org/abs/2208.05984) and [Buen-Abad, Chacko, Kilic, Marques-Tavares, Youn (2023)](https://arxiv.org/abs/23xx.yyyyy).

The BibTeX entries for our two SPartAcous papers are:

    @article{Buen-Abad:2022kgf,
        author = "Buen-Abad, Manuel A. and Chacko, Zackaria and Kilic, Can and Marques-Tavares, Gustavo and Youn, Taewook",
        title = "{Stepped Partially Acoustic Dark Matter, Large Scale Structure, and the Hubble Tension}",
        eprint = "2208.05984",
        archivePrefix = "arXiv",
        primaryClass = "hep-ph",
        reportNumber = "UTTG-10-2022",
        month = "8",
        year = "2022"
    }


    @article{Buen-Abad:2023???,
        author = "Buen-Abad, Manuel A. and Chacko, Zackaria and Kilic, Can and Marques-Tavares, Gustavo and Youn, Taewook",
        title = "{SPartAcous II}",
        eprint = "23xx.yyyyy",
        archivePrefix = "arXiv",
        primaryClass = "hep-ph",
        reportNumber = "????-??-2023",
        month = "?",
        year = "2023"
    }


Compiling CLASS and getting started
-----------------------------------

(the information below can also be found on the webpage, just below
the download button)

Download the code from the webpage and unpack the archive (tar -zxvf
class_vx.y.z.tar.gz), or clone it from
https://github.com/lesgourg/class_public. Go to the class directory
(cd class/ or class_public/ or class_vx.y.z/) and compile (make clean;
make class). You can usually speed up compilation with the option -j:
make -j class. If the first compilation attempt fails, you may need to
open the Makefile and adapt the name of the compiler (default: gcc),
of the optimization flag (default: -O4 -ffast-math) and of the OpenMP
flag (default: -fopenmp; this flag is facultative, you are free to
compile without OpenMP if you don't want parallel execution; note that
you need the version 4.2 or higher of gcc to be able to compile with
-fopenmp). Many more details on the CLASS compilation are given on the
wiki page

https://github.com/lesgourg/class_public/wiki/Installation

(in particular, for compiling on Mac >= 10.9 despite of the clang
incompatibility with OpenMP).

To check that the code runs, type:

    ./class explanatory.ini

The explanatory.ini file is THE reference input file, containing and
explaining the use of all possible input parameters. We recommend to
read it, to keep it unchanged (for future reference), and to create
for your own purposes some shorter input files, containing only the
input lines which are useful for you. Input files must have a *.ini
extension. We provide an example of an input file containing a
selection of the most used parameters, default.ini, that you may use as a
starting point.

If you want to play with the precision/speed of the code, you can use
one of the provided precision files (e.g. cl_permille.pre) or modify
one of them, and run with two input files, for instance:

    ./class test.ini cl_permille.pre

The files *.pre are suppposed to specify the precision parameters for
which you don't want to keep default values. If you find it more
convenient, you can pass these precision parameter values in your *.ini
file instead of an additional *.pre file.

The automatically-generated documentation is located in

    doc/manual/html/index.html
    doc/manual/CLASS_manual.pdf

On top of that, if you wish to modify the code, you will find lots of
comments directly in the files.

Python
------

To use CLASS from python, or ipython notebooks, or from the Monte
Python parameter extraction code, you need to compile not only the
code, but also its python wrapper. This can be done by typing just
'make' instead of 'make class' (or for speeding up: 'make -j'). More
details on the wrapper and its compilation are found on the wiki page

https://github.com/lesgourg/class_public/wiki

Plotting utility
----------------

Since version 2.3, the package includes an improved plotting script
called CPU.py (Class Plotting Utility), written by Benjamin Audren and
Jesus Torrado. It can plot the Cl's, the P(k) or any other CLASS
output, for one or several models, as well as their ratio or percentage
difference. The syntax and list of available options is obtained by
typing 'pyhton CPU.py -h'. There is a similar script for MATLAB,
written by Thomas Tram. To use it, once in MATLAB, type 'help
plot_CLASS_output.m'

Developing the code
--------------------

If you want to develop the code, we suggest that you download it from
the github webpage

https://github.com/lesgourg/class_public

rather than from class-code.net. Then you will enjoy all the feature
of git repositories. You can even develop your own branch and get it
merged to the public distribution. For related instructions, check

https://github.com/lesgourg/class_public/wiki/Public-Contributing

Using the code
--------------

You can use CLASS freely, provided that in your publications, you cite
at least the paper `CLASS II: Approximation schemes <http://arxiv.org/abs/1104.2933>`. Feel free to cite more CLASS papers!

Support
-------

To get support, please open a new issue on the

https://github.com/lesgourg/class_public

webpage!
