PID Controller
==============

This implements a basic PID controller (http://en.wikipedia.org/wiki/PID_controller) in Python.

An auto-tune operation mode is also available (PID_ATune.py).

Development
-----------

Run unittests:

    export TESTNAME=; tox

To run a specific unittest:

    export TESTNAME=.PID_Test.test_min_max_manual; tox
