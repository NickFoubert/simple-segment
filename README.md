Simple Sequence Segmenting
==========================

This repository contains Python code I wrote for segmenting 1-D time series. In other words,
it can be used for transforming a time series into a piecewise linear represenation. 
The algorithms are Python implementations of the "classical" algorithms, as described in 
[An Online Algorithm for Segmenting Time Series][keogh], including:

- the sliding window algorithm;
- the top-down algorithm; and
- the bottom-up algorithm.

The code is *not* optimized for performance in any way, but I've found it useful for 
experimenting and data exploration.

Requirements
------------

The segmenting algorithms use NumPy's least squares fitting routine, so naturally it depends on NumPy.

Example
-------

You can run the code to see example output by running the example.py script. The script
requires [matplotlib][mpl] to display the plots.

The example uses ECG data I found on an [ECG data site][ecg].


References
----------

[keogh]: http://www.cs.ucr.edu/~eamonn/icdm-01.pdf
[numpy]: http://numpy.scipy.org
[mpl]: http://matplotlib.sourceforge.net
[ecg]: http://myweb.msoe.edu/~martynsc/signals/ecg/ecg.html
