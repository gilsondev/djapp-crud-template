# -*- coding: utf-8 -*-

import datetime

from django.test import TestCase
from django.db.models.query import QuerySet
from django.core.urlresolvers import reverse

from .models import {{ app_name|title }}
from .forms import {{ app_name|title }}Form


class {{ app_name|title }}ListTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('{{ app_name }}:list'))

    def test_get(self):
        """GET /{{ app_name }}/ must return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Should render template {{ app_name }}/list.html"""
        self.assertTemplateUsed(self.resp, '{{ app_name }}/list.html')

    def test_html(self):
        """Validate page content"""
        # TODO: Define content for test
        pass


class {{ app_name|title }}NewTest(TestCase):
    def setUp(self):
        self.resp = self.client.get(reverse('{{ app_name }}:new'))

    def test_get(self):
        """ GET /{{ app_name }}/new/ must return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Should render template {{ app_name }}/new.html """
        self.assertTemplateUsed(self.resp, '{{ app_name }}/new.html')

    def test_html(self):
        """Validate page content"""
        # TODO: Define content for test
        pass

    def test_save(self):
        """Should register correctly"""
        # TODO: Define fields for post
        resp = self.client.post(reverse('{{ app_name }}:new'), {})
        self.assertEqual(302, resp.status_code)


class {{ app_name|title }}EditTest(TestCase):
    def setUp(self):
        self.url = '/{{ app_name }}/%s/update/' % (self.{{ app_name }}.slug,)
        self.resp = self.client.get(self.url)

    def test_get(self):
        """GET /{{ app_name }}/<slug>/update/ must return status 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Should render template {{ app_name }}/update.html"""
        self.assertTemplateUsed(self.resp, '{{ app_name }}/update.html')

    def test_html(self):
        """Validate page content"""
        # TODO: Define content for test
        pass

    def test_form_in_context(self):
        """Should class form in request context"""
        form = self.resp.context['form']
        self.assertIsInstance(form, {{ app_name|title }}Form)

    def test_save(self):
        """Should register correctly"""
        # TODO: Define fields for post
        resp = self.client.post(self.url, {})
        self.assertEqual(302, resp.status_code)


class {{ app_name|title }}DeleteTest(TestCase):
    def setUp(self):
        self.url = '/{{ app_name }}/%s/delete/' % (self.{{ app_name }}.slug,)
        self.resp = self.client.get(self.url)

    def test_get(self):
        """ GET /{{ app_name }}/<slug>/delete/ must return 200"""
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        """Should render template {{ app_name }}/confirm_delete.html"""
        self.assertTemplateUsed(self.resp, '{{ app_name }}/confirm_delete.html')

    def test_html(self):
        """Validate page content"""
        # TODO: Define content for test
        pass


class {{ app_name|title }}FormTest(TestCase):
    def setUp(self):
        self.form = {{ app_name|title }}Form()

    def test_fields(self):
        """Should have these fields"""
        # TODO: Define fields
        fields = []
        self.assertItemsEqual(fields, self.form.fields)


class {{ app_name|title }}ModelTest(TestCase):
    def setUp(self):
        self.{{ app_name }} = {{ app_name|title }}.objects.create()

    def test_create(self):
        """Should create correctly"""
        self.assertEqual(self.{{ app_name }}.pk, 1)

    def test_unicode(self):
        self.assertEqual(unicode(self.{{ app_name }}), u"{{ app_name|title }}")
