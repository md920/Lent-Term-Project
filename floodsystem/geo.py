# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from os import stat

def stations_by_distance(stations, p):
    dist_stat = []
    for stat in stations:
        dist_stat.append((stat, haversine(stat.coord, p),))
    result = sorted_by_key(dist_stat, 1)
    return result