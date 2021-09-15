#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

path_params = {
    "source": "source",
    "resource": "res",
    "output": "output",
}


def source_data_file(filename):
    return os.path.join(path_params["source"], filename)


def resource_file(filename):
    return os.path.join(path_params["resource"], filename)


def output_file(filename):
    return os.path.join(path_params["output"], filename)
