from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_grupo'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 8
    n_rounds_payoff = 4
    fee = 350

    #Hojas de Vida = lista con diccionarios dentro
    ## Listas -> estructuras ordenadas, separados por comas
    ## Diccionarios -> estrictura no ordenada
    hvs = [
        # hoja de vida de la ronda # 0
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.151.947.XXX',
                'lug_nac': 'Cali (Valle del Cauca)',
                'age': '30',
                'las_exp': ['Conductor independiente - Más de 12 meses',
                            'Preparador físico - Entre 3 y 6 meses',
                            'Enfermero de clínica - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '20.610.XXX',
                'lug_nac': 'Maracaibo (Venezuela)',
                'age': '32',
                'las_exp': ['Enfermero independiente - Más de 12 meses',
                            'Enfermero de clínica - Entre 7 y 9 meses',
                            'Enfermero de clínica - Entre 7 y 9 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>cuidador de adulto mayor</b>. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '1'
        },

        # hoja de vida # 1
        {
            'A': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '14.931.XXX',
                'lug_nac': 'Maracay (Venezuela)',
                'age': '35',
                'las_exp': ['Supernumerario de restaurante- Entre 10 y 12 meses',
                            'Auxiliar de bodega - Más de 12 meses',
                            'Domiciliario - Más de 12 meses'
                            ],
                'lvl_edu': 'Primaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.015.452.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '28',
                'las_exp': ['Domiciliario de restaurante - Entre 7 y 9 meses',
                            'Auxiliar de bodega - Entre 3 y 6 meses',
                            'Pintor de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Primaria',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>asistente de inventario de bodega</b>. <br>¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '2'
        },
        # hoja de vida # 2
        {
            'A': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '1.401.XXX',
                'lug_nac': 'Maracay (Venezuela)',
                'age': '28',
                'las_exp': ['Domiciliario de restaurante - Entre 10 y 12 meses',
                            'Domiciliario aplicación - Entre 7 y 9 meses',
                            'Domiciliario independiente - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '824.XXX',
                'lug_nac': 'Barquisimento (Venezuela)',
                'age': '30',
                'las_exp': ['Domiciliario aplicación - Más de 12 meses',
                            'Mensajero motorizado - Entre 10 y 12 meses',
                            'Domiciliario aplicación - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>asistente de ruta</b>. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '3'
        },
        # hoja de vida # 3

        {
            'A': {

                'type': 'A',
                'tipo_doc': 'Cédula de ciudadanía',
                'num_doc': '1.022.965.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '33',
                'las_exp': ['Vigilante seguridad privada - Más de 12 meses',
                            'Supervisor seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.143.362.XXX',
                'lug_nac': 'El Bagre (Antioquia)',
                'age': '30',
                'las_exp': ['Operador de medios de seguridad - Más de 12 meses',
                            'Contratista de construcción - Más de 12 meses',
                            'Pintor de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>almacenista montacarguista</b>. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '4'
        },
        # hoja de vida # 4

        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '18.839.XXX',
                'lug_nac': 'Mónagas (Venezuela)',
                'age': '30',
                'las_exp': ['Obrero de construcción - Más de 12 meses',
                            'Pintor - Entre 10 y 12 meses',
                            'Ayudante de construcción - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '20.505.XXX',
                'lug_nac': 'San Cristóbal (Venezuela)',
                'age': '33',
                'las_exp': ['Maestro de obra- Entre 3 y 6 meses',
                            'Ayudante de obra - Más de 12 meses',
                            'Ayudante de obra - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>auxiliar de obra y paletero</b>. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '5'
        },
        # hoja de vida # 5

        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '80.772.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '34',
                'las_exp': ['Auxiliar de bodega - Entre 10 y 12 meses',
                            'Auxiliar postal - Más de 12 meses',
                            'Codificador -  Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.031.169.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '27',
                'las_exp': ['Mensajero motorizado - Más de 12 meses',
                            'Analista de despachos - Entre 10 y 12 meses',
                            'Asesor comercial - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>coordinador de ruta</b>. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '6'
        },
        # hoja de vida # 6

        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '80.746.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '40',
                'las_exp': ['Jardinero de zonas verdes - Más de 12 meses ',
                            'Guarnecedor de calzado - Entre 7 y 9 meses',
                            'Bodeguero - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '7.004.XXX',
                'lug_nac': 'Los Puertos (Venezuela)',
                'age': '35',
                'las_exp': ['Oficios Varios - Más de 12 meses',
                            'Maquinista - 3 meses',
                            'Trabajador fábrica de escritorios - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>operario de máquina de empaquetado</b>?. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '7'
        },
        # hoja de vida # 7

        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '21.030.XXX',
                'lug_nac': 'San Antonio de Táchira (Venezuela)',
                'age': '33',
                'las_exp': ['Músico de agrupación - Más de 12 meses',
                            'Domiciliario de restaurante - Entre 3 y 6 meses',
                            'Músico de agrupación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de ciudadanía',
                'num_doc': '1.023.970.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '24',
                'las_exp': ['Profesor de música independiente - Más de 12 meses',
                            'Profesor de música en instituto - Más de 12 meses',
                            'Trombonista de agrupación - Más de 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "El Candidato A y el Candidato B se están presentando para un puesto vacante de <b>músico de agrupación para eventos</b>?. <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            # ¿Quién cree que fue el más escogido por el personal de Recursos Humanos de medianas y pequeñas empresas?",
            'round': '8'
        },
    ]

    



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Introducción

    selected_round_1 = models.StringField(initial = "-")
    tokens_round_1 = models.IntegerField(initial = -1)
    selected_round_2 = models.StringField(initial = "-")
    tokens_round_2 = models.IntegerField(initial = -1)
    selected_round_3 = models.StringField(initial = "-")
    tokens_round_3 = models.IntegerField(initial = -1)
    selected_round_4 = models.StringField(initial = "-")
    tokens_round_4 = models.IntegerField(initial = -1)
    selected_round_5 = models.StringField(initial = "-")
    tokens_round_5 = models.IntegerField(initial = -1)
    selected_round_6 = models.StringField(initial = "-")
    tokens_round_6 = models.IntegerField(initial = -1)
    selected_round_7 = models.StringField(initial = "-")
    tokens_round_7 = models.IntegerField(initial = -1)
    selected_round_8 = models.StringField(initial = "-")
    tokens_round_8= models.IntegerField(initial = -1)

# Payoffs
    ## depende de la cantidad de rondas a pagar
    ### ronda 1 a pagar
    round_a_to_payoff_selected = models.StringField()
    round_a_to_payoff_tokens = models.IntegerField()
    ### ronda 2 a pagar
    round_b_to_payoff_selected = models.StringField()
    round_b_to_payoff_tokens = models.IntegerField()
    ### ronda 3 a pagar
    round_c_to_payoff_selected = models.StringField()
    round_c_to_payoff_tokens = models.IntegerField()
    ### ronda 4 a pagar
    round_d_to_payoff_selected = models.StringField()
    round_d_to_payoff_tokens = models.IntegerField()

    ## Cálculo de los tokens totales
    tokens_total = models.IntegerField()

    winner_round_1 = models.StringField()
    winner_round_2 = models.StringField()
    winner_round_3 = models.StringField()
    winner_round_4 = models.StringField()
    winner_round_5 = models.StringField()
    winner_round_6 = models.StringField()
    winner_round_7 = models.StringField()
    winner_round_8 = models.StringField()

# tokens que se acumulan entre rondas más el fee. Si la suma es <350 el participante sale
    tokens_acum = models.IntegerField()
# tokens que traje de la primera etapa
    tokens_total_ind = models.IntegerField()
# tokens que me voy a llevar a la tercera etapa
    tokens_rondas = models.IntegerField()

    tokens_encription = models.IntegerField()


    lab_id = models.IntegerField(initial=0)

    empate_tokens_a = models.IntegerField(initial=0)
    empate_tokens_b = models.IntegerField(initial = 0)
    empate_tokens_c = models.IntegerField(initial = 0)
    empate_tokens_d = models.IntegerField(initial = 0)

    def set_id(self):
        participant_label = self.participant.label
        self.lab_id = C.LAB.get(participant_label, 0)
