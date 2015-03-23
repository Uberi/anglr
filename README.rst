anglr
=====

.. image:: https://pypip.in/download/anglr/badge.svg
    :target: https://pypi.python.org/pypi/anglr/
    :alt: Downloads

.. image:: https://pypip.in/version/anglr/badge.svg
    :target: https://pypi.python.org/pypi/anglr/
    :alt: Latest Version

.. image:: https://pypip.in/status/anglr/badge.svg
    :target: https://pypi.python.org/pypi/anglr/
    :alt: Development Status

.. image:: https://pypip.in/license/anglr/badge.svg
    :target: https://pypi.python.org/pypi/anglr/
    :alt: License

Planar angle mathematics library for Python.

Links:

-  `PyPI <https://pypi.python.org/pypi/anglr/>`__
-  `GitHub <https://github.com/Uberi/anglr>`__

Quickstart: ``pip3 install anglr``.

Examples
--------

Angle creation:

.. code:: python

    from math import pi
    from anglr import Angle
    print(Angle())
    print(Angle(87 * pi / 2))
    print(Angle(pi / 2, "radians"))
    print(Angle(Angle(pi / 2, "radians"))) # same as above
    print(Angle(64.2, "degrees"))
    print(Angle(384.9, "gradians"))
    print(Angle(4.5, "hours"))
    print(Angle(203.8, "arcminutes"))
    print(Angle(42352.7, "arcseconds"))
    print(Angle((56, 32), "vector")) # angle in standard position - counterclockwise from positive X-axis

Angle conversion:

.. code:: python

    from anglr import Angle
    x = Angle(58.3)
    print([x], str(x), x.radians, x.degrees, x.gradians, x.hours, x.arcminutes, x.arcseconds, x.vector, x.x, x.y)
    print(complex(x))
    print(float(x))
    print(int(x))
    x.radians = pi / 2
    print(x.dump())
    x.degrees = 64.2
    print(x.dump())
    x.gradians = 384.9
    print(x.dump())
    x.hours = 4.5
    print(x.dump())
    x.arcminutes = 203.8
    print(x.dump())
    x.arcseconds = 42352.7
    print(x.dump())
    x.vector = (56, 32)
    print(x.dump())

Angle arithmetic:

.. code:: python

    from math import pi
    from anglr import Angle
    print(Angle(pi / 6) + Angle(2 * pi / 3))
    print(x * 2 + Angle(3 * pi / 4) / 4 + 5 * Angle(pi / 3))
    print(-abs(+Angle(pi)))
    print(round(Angle(-75.87)))
    print(Angle(-4.3) <= Angle(pi / 4) > Angle(0.118) == Angle(0.118))
    print(Angle(-870.3, "gradians").normalized())
    print(Angle(-870.3, "gradians").normalized(0)) # same as above
    print(Angle(-870.3, "gradians").normalized(0, 2 * pi)) # same as above
    print(Angle(-870.3, "gradians").normalized(-pi, pi))
    print(Angle(-870.3, "gradians").normalized(-pi, 0))
    print(Angle(1, "degrees").angle_between_clockwise(Angle(0, "degrees")))
    print(Angle(1, "degrees").angle_between(Angle(0, "degrees")))

To run all of the above as tests, simply execute the module using ``python3 -m anglr``.

Installing
----------

The easiest way to install this is using ``pip3 install anglr``.

Otherwise, download the source distribution from `PyPI <https://pypi.python.org/pypi/anglr/>`__, and extract the archive.

In the folder, run ``python3 setup.py install``.

Requirements
------------

This library requires Python 3.3 or higher to run.

Authors
-------

::

    Uberi <azhang9@gmail.com> (Anthony Zhang)

Please report bugs and suggestions at the `issue tracker <https://github.com/Uberi/anglr/issues>`__!

License
-------

Copyright 2014-2015 `Anthony Zhang (Uberi) <https://uberi.github.io>`__.

The source code is available online at `GitHub <https://github.com/Uberi/anglr>`__.

This program is made available under the 3-clause BSD license. See ``LICENSE.txt`` for more information.
