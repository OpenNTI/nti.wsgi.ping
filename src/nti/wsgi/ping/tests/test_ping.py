#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""

from __future__ import print_function, unicode_literals, absolute_import
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)
#disable: accessing protected members, too many methods
#pylint: disable=W0212,R0904

import unittest

from webtest import TestApp

from nti.wsgi.ping import ping_handler_factory

class TestPing(unittest.TestCase):

	def test_ping_returns_bytes(self):
		app = ping_handler_factory(None)
		app = TestApp( app )

		app.get( '/_ops/ping' )
