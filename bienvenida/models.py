from otree.api import *

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'bienvenida'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LAB = {
        'LAB1': 1,
        'LAB2': 2,
        'LAB3': 3,
        'LAB4': 4,
        'LAB5': 5,
        'LAB6': 6,
        'LAB7': 7,
        'LAB8': 8,
        'LAB9': 9,
        'LAB10': 10,
        'LAB11': 11,
        'LAB12': 12,
        'LAB13': 13,
        'LAB14': 14,
        'LAB15': 15,
        'LAB16': 16,
        'LAB17': 17,
        'LAB18': 18,
        'LAB19': 19,
        'LAB20': 20,
        'LAB21': 21,
        'LAB22': 22,
        'LAB23': 23,
        'LAB24': 24,
        'LAB25': 25,
        'LAB26': 26,
        'LAB27': 27,
        'LAB28': 28,
        'LAB29': 29,
    }

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    name = models.StringField(label="Nombres y apellidos:", blank=False)
    acepto = models.BooleanField(label="Acepto participar",
                                 choices=[
                                     [True, "Sí"],
                                     [False, "No"]])


    lab_id = models.StringField(initial = 0)

    def set_id(self):
        participant_label = self.participant.label
        self.lab_id = participant_label
