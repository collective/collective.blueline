# -*- coding: utf-8 -*-
from plone import api
from plone.app.testing import logout
from plone.registry.interfaces import IRegistry
from sc.adshelper.config import BASE_REGISTRY
from sc.adshelper.config import PROJECTNAME
from sc.adshelper.controlpanel import IAdsHelperSettings
from sc.adshelper.testing import INTEGRATION_TESTING
from zope.component import getUtility
from zope.interface import alsoProvides
from sc.adshelper.interfaces import IBrowserLayer

import unittest


class ControlPanelTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        alsoProvides(self.request, IBrowserLayer)
        self.controlpanel = self.portal['portal_controlpanel']

    def test_controlpanel_has_view(self):
        view = api.content.get_view(u'adshelper-settings', self.portal, self.request)
        view = view.__of__(self.portal)
        self.assertTrue(view())

    def test_controlpanel_view_is_protected(self):
        from AccessControl import Unauthorized
        logout()
        with self.assertRaises(Unauthorized):
            self.portal.restrictedTraverse('@@adshelper-settings')

    def test_controlpanel_installed(self):
        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertIn('adshelper', actions, 'control panel not installed')

    def test_controlpanel_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        actions = [
            a.getAction(self)['id'] for a in self.controlpanel.listActions()]
        self.assertNotIn('adshelper', actions, 'control panel not removed')


class RegistryTestCase(unittest.TestCase):

    layer = INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.registry = getUtility(IRegistry)
        self.settings = self.registry.forInterface(IAdsHelperSettings)

    def test_html_head_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'html_head'))
        self.assertEqual(self.settings.html_head, u'')

    def test_above_content_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'above_content'))
        self.assertEqual(self.settings.above_content, u'')

    def test_below_content_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'below_content'))
        self.assertEqual(self.settings.below_content, u'')

    def test_footer_record_in_registry(self):
        self.assertTrue(hasattr(self.settings, 'footer'))
        self.assertEqual(self.settings.footer, u'')

    def test_records_removed_on_uninstall(self):
        qi = self.portal['portal_quickinstaller']

        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=[PROJECTNAME])

        records = [
            BASE_REGISTRY + 'html_head',
            BASE_REGISTRY + 'above_content',
            BASE_REGISTRY + 'below_content',
            BASE_REGISTRY + 'footer',
        ]

        for r in records:
            self.assertNotIn(r, self.registry)
