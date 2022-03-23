from abc import ABC

from Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        super()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False
