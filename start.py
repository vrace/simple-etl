#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
import sys
import traceback

from configs import init_configs, temp_db_connection

logger = logging.getLogger(__name__)


class SimpleETLTasks:

    def landing_tasks(self):
        return []

    def staging_tasks(self):
        return []

    def consumption_tasks(self):
        return []

    def misc_tasks(self):
        return []


class SimpleETLApplication:

    def __init__(self):
        self.tasks = SimpleETLTasks()
        self.conn = None

    def init_connection(self):
        logger.info("Connecting to temporary database")
        self.conn = temp_db_connection()

    def perform_landing_tasks(self):
        self.perform_tasks_in_batch("landing", self.tasks.landing_tasks(), lambda it: it.perform_landing(self.conn))

    def perform_staging_tasks(self):
        self.perform_tasks_in_batch("staging", self.tasks.staging_tasks(), lambda it: it.perform_staging(self.conn))

    def perform_consumption_tasks(self):
        self.perform_tasks_in_batch("consumption", self.tasks.consumption_tasks(), lambda it: it.perform_consumption(self.conn))

    def perform_misc_tasks(self):
        self.perform_tasks_in_batch("misc", self.tasks.misc_tasks(), lambda it: it.perform_task())

    def perform_tasks_in_batch(self, task_type, tasks, perform_task_fn):
        logger.info(f"Performing {task_type} tasks")
        has_error = False
        for task in tasks:
            try:
                perform_task_fn(task)
            except Exception as exc:
                logger.error(f"Error occurred during {task_type}: {exc}")
                logger.debug(f"{traceback.format_exc()}")
                has_error = True
        if has_error:
            raise RuntimeError(f"{task_type.capitalize()} tasks are not fully completed.")

    def main(self):
        logger.info("ETL started")
        try:
            self.init_connection()
            self.perform_landing_tasks()
            self.perform_staging_tasks()
            self.perform_consumption_tasks()
            self.perform_misc_tasks()
            logger.info("ETL completed")
            return 0
        except Exception as exc:
            logger.error(f"ETL aborted: {exc}")
            logger.debug(f"{traceback.format_exc()}")
            return 1


if __name__ == "__main__":
    init_configs()
    app = SimpleETLApplication()
    sys.exit(app.main())
