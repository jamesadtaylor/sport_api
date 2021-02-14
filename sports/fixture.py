#!/usr/bin/env python
"""Represents a football fixture - lite version of the sports db version"""
import re


class Fixture:
    """Represents a football fixture"""

    def __init__(self, adict : dict):
        str_event = None
        str_filename = None
        str_league = None
        str_home_team = None
        str_away_team = None
        int_home_score = None
        int_away_score = None

        for key, value in adict.items():
            if locals().keys().__contains__(camel_to_snake(key)):
                self.__dict__[camel_to_snake(key)] = value

    def dump(self):
        """serialise the object to json string format"""
        return {"Fixture": dict(str_event=self.str_event,
                                str_filename=self.str_filename,
                                str_league=self.str_league,
                                str_home_team=self.str_home_team,
                                str_away_team=self.str_away_team,
                                int_home_score=self.int_home_score,
                                int_away_score=self.int_away_score)}


def camel_to_snake(name: str) -> str:
    """convert string from camelcase to snake case"""
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()
