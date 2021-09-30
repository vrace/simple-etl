#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from .logging_config import *
from .path_config import \
    path_params, \
    source_data_file, \
    resource_file, \
    output_file
from .temp_db_config import \
    temp_db_params, \
    temp_db_connection

logger = logging.getLogger(__name__)


def init_configs():
    logger.info("Initializing configs")
    pass
