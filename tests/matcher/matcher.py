from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class returnMatch(BaseMatcher):
    def _matches(self, obj):
        return obj == "This note does not exist"

    def describe_to(self, description):
        description.append("Values are not equal")


def eq_to_nonexistent_note():
    return returnMatch()
