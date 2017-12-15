====================================
Getting Started with Python 3
====================================

http://bit.ly/py-dec-13-2017

(C) Copyright 2017 Matt Harrison

Matt Harrison - follow on twitter for Python related tweets ( @__mharrison__ )

Installation
=================

If you haven't installed on Windows please do so.
Click to "Add Python to PATH". Otherwise see

https://docs.python.org/3/using/windows.html#configuring-python

Windows - Start -> All Apps -> Scroll down to Python 3.6 -> IDLE
(Can click drag down to taskbar)



D - Decide
R - Relax
M - Motivation
O - Observe
M - Mechanics

Launching IDLE
==================

::
  
  $ python3 -m idlelib.idle

Resources
============================

* https://www.amazon.com/Illustrated-Guide-Python-Walkthrough-Illustrations/dp/1977921752
* https://github.com/mattharrison/Tiny-Python-3.6-Notebook
* https://pypi.python.org/pypi
* https://coverage.readthedocs.io/en/coverage-4.4.2/

Notes
========

Everything is an object

dir - lists what is in your namespace, or lists
what are the attributes of an object

Namespaces - 3 namespaces

* Local - inside of a method or function
* Global - defined at global (modules, classes, functions)
* Builtin

3rd Party Libraries
======================

Use (unix, see Tiny Python Notebook for Windows)::

  $ python3 -m venv path/to/env
  $ source path/to/env/bin/activate

To create a virtual environment

Use::

  (env)$ pip install somelibrary


