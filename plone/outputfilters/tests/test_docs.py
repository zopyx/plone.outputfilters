# -*- coding: utf-8 -*-
from plone.outputfilters.testing import PLONE_OUTPUTFILTERS_FUNCTIONAL_TESTING
from plone.testing import layered

import doctest
import pprint
import unittest2 as unittest


optionflags = (
    doctest.ELLIPSIS |
    doctest.NORMALIZE_WHITESPACE |
    doctest.REPORT_ONLY_FIRST_FAILURE
)
normal_testfiles = [
    '../README.txt'
]


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(doctest.DocFileSuite(test,
                                     optionflags=optionflags,
                                     globs={'pprint': pprint.pprint,
                                            }
                                     ),
                layer=PLONE_OUTPUTFILTERS_FUNCTIONAL_TESTING)
        for test in normal_testfiles])
    return suite
