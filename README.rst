pytest-firefox
===============

pytest-firefox is a plugin for `pytest <http://pytest.org>`_ that provides
support for running `FoxPuppet <http://https://github.com/mozilla/FoxPuppet/>`_
to control `Firefox Web Browser <https://www.mozilla.org/en-US/firefox/>`_ within
a test.

Requirements
------------

You will need the following prerequisites in order to use pytest-firefox:

- Python 2.7, 3.6
- pytest 3.0 or newer

Installation
------------

To install pytest-firefox:

.. code-block:: bash

  $ pip install pytest-firefox

Usage
-----

To use pytest-firefox with your tests simply specify ``firefox`` as a fixture
to your test.

.. code-block:: python

  def test_something(firefox):
      firefox.open_window()

This will open a new window.

``pytest-firefox`` also creates a default Selenium WebDriver object named
``selenium``.
