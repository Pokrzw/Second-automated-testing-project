from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class returnMatch(BaseMatcher):
    def _matches(self, obj):
        return obj == 'Nieistniejace instance'

    def describe_to(self, description):
        description.append("Values are not equal")


def eq_to_Nieistniejace_Instance():
    return returnMatch()
