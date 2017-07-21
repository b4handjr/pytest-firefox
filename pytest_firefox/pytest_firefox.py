# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Module containing fixtures to use within pytest tests."""

import pytest
from selenium.webdriver import Firefox

from foxpuppet import FoxPuppet


@pytest.yield_fixture
def firefox(selenium):
    """Return initialized foxpuppet object."""
    yield FoxPuppet(selenium)


@pytest.fixture
def notifications(firefox):
    """Provide access to the different types of firefox notifications.

    :returns: An object containing references to notification types
    :return type: Object
    """
    from foxpuppet.windows.browser.notifications.addons import NOTIFICATIONS

    for item in NOTIFICATIONS.values():
        setattr(notifications, item.__name__, item)
    return notifications


@pytest.yield_fixture
def selenium(pytestconfig, selenium):
    """Yield selenium object if user has not already created one."""
    if pytestconfig.pluginmanager.has_plugin('selenium'):
        yield selenium
    else:
        yield Firefox()
