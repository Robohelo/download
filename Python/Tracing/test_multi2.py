# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 12:29:45 2021

@author: Roboadmin
"""
import logging
import concurrent.futures
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
