#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"
