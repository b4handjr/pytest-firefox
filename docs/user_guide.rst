User Guide
==========

.. contents:: :depth: 2

Quick Start
***********

The pytest-firefox plugin provides a method scoped
`fixture <http://pytest.org/latest/fixture.html>`_ for use within a test. This means
that any test with Firefox as an argument will have access to
`Foxpuppet <http://foxpuppet.readthedocs.io>`_ features for browser control.

.. note::
  It is advised to create a fixture named selenium and specify any options you
  want Firefox to be started with. By default, pytest-firefox will create a blank
  Firefox Webdriver object using `Selenium <http://seleniumhq.org/>`_.

Here is an example test that opens a new window using Foxpuppet.

.. code-block:: python

  def open_window(firefox):
      firefox.open_window()

The above code will start a new Webdriver session with no options passed to Firefox.
It will then open 1 new window for a total of 2 windows opened. By default,
starting a new Selenium Webdriver session will open 1 window.

Notifications
*************

pytest-firefox has access to the different types of notifications shown within Firefox.
To access these items simply add the notifications fixture as an argument in your
tests.

.. code-block:: python

  def check_notification(firefox, notifications):
      firefox.browser.wait_for_notification(notifications.AddOnInstallConfirmation)

The above code will wait for the notification type named AddOnInstallConfirmation
to be shown. See more about `notifications <http://foxpuppet.readthedocs.io>`_.
