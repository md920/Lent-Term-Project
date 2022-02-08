# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data."""

from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit
from os import stat

def stations_by_distance(stations, p):
    """Requirement for Task 1B"""
    dist_stat = []
    for stat in stations:
        dist_stat.append((stat, haversine(stat.coord, p),))
    result = sorted_by_key(dist_stat, 1)
    return result

def stations_within_radius(stations, centre, r):
    """Requirement for Task 1C"""
    stat_dist = stations_by_distance(stations, centre)
    stats_in_rad = []
    for elem in stat_dist:
        if elem[1] < r:
            stats_in_rad.append(elem[0])
    return stats_in_rad