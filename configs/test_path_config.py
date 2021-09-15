#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from unittest import TestCase

from configs.path_config import source_data_file, resource_file, output_file


class TestPathConfig(TestCase):

    def test_source_data_file(self):
        file = source_data_file("my_data.csv")
        self.assertEqual(file, "source/my_data.csv")

    def test_resource_file(self):
        file = resource_file("my_template.sql.template")
        self.assertEqual(file, "res/my_template.sql.template")

    def test_output_file(self):
        file = output_file("your_data.csv")
        self.assertEqual(file, "output/your_data.csv")
