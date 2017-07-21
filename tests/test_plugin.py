# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.


def test_fixture(testdir):
    testdir.makepyfile("""
        import pytest
        @pytest.fixture(scope='session')
        def firefox():
            return 'foo'
        def test_fixture(firefox):
            assert firefox == 'foo'
    """)
    result = testdir.runpytest()
    assert result.ret == 0
