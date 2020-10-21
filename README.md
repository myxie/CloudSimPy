# Telescope Operations Simulator

## This project started as a fork of CloudSimPy. It has since evolved from the original repo significantly enough to warrant its own development area. It is now available at https://github.com/top-sim/topsim. 

[![Build Status](https://travis-ci.com/myxie/topsim.svg?branch=master)](https://travis-ci.com/myxie/topsim)
[![Coverage Status](https://coveralls.io/repos/github/myxie/topsim/badge.svg?branch=master)](https://coveralls.io/github/myxie/topsim?branch=master)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/myxie/topsim/master?filepath=visual)

TopSim is a telescope observation and data post-processing simulator, based on a fork of Robert Lexis' CloudSimPy. The intention of TopSim is to provide an end-to-end view of telescope observations, data-archival, and the subsequent processing of observation data products, with a focus on the mid-term timeline commonly used in telescope semester plans. The main intention of the simulator is to test new workflow planning and scheduling techniques designed for the [Square Kilometre Array (SKA)](https://www.skatelescope.org/) and its precursor telescope, the [Australian Square Kilomere Array Pathfinder (ASKAP)](https://www.atnf.csiro.au/projects/askap/index.html).

TopSim is being actively developed by [Ryan Bunney](https://www.icrar.org/people/rbunney/), a PhD Candidate at the [International Centre for Radio Astronomy Research (ICRAR)](https://www.icrar.org/), in Perth, Western Australia. 

## Dependencies

TopSim uses the `Simpy` discrete-event simulation framework; in addition to this, the following packages are necessary to use the full feature set of TopSim:

* numpy
* Networkx
* matplotlib
* bokeh 
