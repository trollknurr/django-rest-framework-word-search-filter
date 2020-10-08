# Full word filter backend for django REST framework

[![Build Status](https://travis-ci.org/trollknurr/django-rest-framework-word-search-filter.svg?branch=master)](https://travis-ci.org/trollknurr/django-rest-framework-word-search-filter)

Database independent (runs without regexp), easy to use full word search backend. Now works with hyphen.
Do not use with default `filters.SearchFilter`

## Install

    pip install djangorestframework-word-filter

In your ``settings.py``

    INSTALLED_APPS += ('rest_framework_word_filter', )

Compatible with python 3.6+, django 3.0+

## Using

Import

    from rest_framework_word_filter import FullWordSearchFilter
    ....
    
and add to filter backends. Add attribute ``word_fields`` to define which fields in model will be used for search.

    class FooListView(ListAPIView):
        model = Foo
        queryset = Foo.objects.all()
        serializer_class = FooSerializer
        filter_backends = (FullWordSearchFilter, )
        word_fields = ('text',)

Fill free to send issues or pull requests =)

