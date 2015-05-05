# coding:utf-8
from django.db import models
from django.test import TestCase

from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer
from rest_framework.test import APIRequestFactory

from .filter import FullWordSearchFilter


class Foo(models.Model):
    text = models.CharField(max_length=255)


class FooSerializer(ModelSerializer):
    class Meta:
        model = Foo
        fields = ('text', )


class FooListView(ListAPIView):
    model = Foo
    queryset = Foo.objects.all()
    serializer_class = FooSerializer
    filter_backends = (FullWordSearchFilter, )
    word_fields = ('text',)


class FullWordFilterTestCase(TestCase):
    TEXT_CASES = [
        'fo',
        'foo',
        'foo b',
        'foo ba',
        'foo bar'
    ]

    @classmethod
    def setUpClass(cls):
        for text in cls.TEXT_CASES:
            Foo.objects.create(text=text)

        super(FullWordFilterTestCase, cls).setUpClass()

    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = FooListView.as_view()

    def test_one_word_one_res(self):
        request = self.factory.get('/foo/?search=fo')
        response = self.view(request)
        self.assertEqual(len(response.data), 1)

    def test_one_word_many_res(self):
        request = self.factory.get('/foo/?search=foo')
        response = self.view(request)
        self.assertEqual(len(response.data), 4)

    def test_two_word_one_res_1(self):
        request = self.factory.get('/foo/?search=foo b')
        response = self.view(request)
        self.assertEqual(len(response.data), 1)

    def test_two_word_one_res_2(self):
        request = self.factory.get('/foo/?search=foo ba')
        response = self.view(request)
        self.assertEqual(len(response.data), 1)