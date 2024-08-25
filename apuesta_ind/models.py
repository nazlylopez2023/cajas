from otree.api import *


doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_ind'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 8
    n_rounds_payoff = 4
    fee = 350

    LAB = {
        'JUN001': 1,
        'JUN002': 2,
        'JUN003': 3,
        'JUN004': 4,
        'JUN005': 5,
        'JUN006': 6,
        'JUN007': 7,
        'JUN008': 8,
        'JUN009': 9,
        'JUN010': 10,
        'JUN011': 11,
        'JUN012': 12,
        'JUN013': 13,
        'JUN014': 14,
        'JUN015': 15,
        'JUN016': 16,
        'JUN017': 17,
        'JUN018': 18,
        'JUN019': 19,
        'JUN020': 20,
        'JUN021': 21,
        'JUN022': 22,
        'JUN023': 23,
        'JUN024': 24,
        'JUN025': 25,
        'JUN026': 26,
        'JUN027': 27,
        'JUN028': 28,
        'JUN029': 29,
    }

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

    count_ronda1_a = models.IntegerField(initial = 0)
    count_ronda1_b = models.IntegerField(initial = 0)
    count_ronda2_a = models.IntegerField(initial = 0)
    count_ronda2_b = models.IntegerField(initial = 0)
    count_ronda3_a = models.IntegerField(initial = 0)
    count_ronda3_b = models.IntegerField(initial = 0)
    count_ronda4_a = models.IntegerField(initial = 0)
    count_ronda4_b = models.IntegerField(initial = 0)
    count_ronda5_a = models.IntegerField(initial = 0)
    count_ronda5_b = models.IntegerField(initial = 0)
    count_ronda6_a = models.IntegerField(initial = 0)
    count_ronda6_b = models.IntegerField(initial = 0)
    count_ronda7_a = models.IntegerField(initial = 0)
    count_ronda7_b = models.IntegerField(initial = 0)
    count_ronda8_a = models.IntegerField(initial = 0)
    count_ronda8_b = models.IntegerField(initial = 0)
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
    selected_prueba = models.StringField(initial = "-")
    tokens_prueba = models.IntegerField(initial = -1)

    winner_round_1 = models.StringField()
    winner_round_2 = models.StringField()
    winner_round_3 = models.StringField()
    winner_round_4 = models.StringField()
    winner_round_5 = models.StringField()
    winner_round_6 = models.StringField()
    winner_round_7 = models.StringField()
    winner_round_8 = models.StringField()


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
    tokens_individual = models.IntegerField()
    ## tokens que se van acumulan entre etapas
    tokens_acum = models.IntegerField()
    ## Pago en pesos
    pago_monetario_final = models.IntegerField()

    tokens_encription = models.IntegerField()

    lab_id = models.IntegerField(initial=0)

    grupo_winner_round_1 = models.StringField()
    grupo_winner_round_2 = models.StringField()
    grupo_winner_round_3 = models.StringField()
    grupo_winner_round_4 = models.StringField()
    grupo_winner_round_5 = models.StringField()
    grupo_winner_round_6 = models.StringField()
    grupo_winner_round_7 = models.StringField()
    grupo_winner_round_8 = models.StringField()

    # Conteo de errores en la prueba
    mistakes = models.IntegerField(initial = 0, blank = True)

    # ----------------- Cuestionario ----------------#

    age = models.IntegerField(label = "<p><b>1)</b>Edad</p>")
    gender = models.IntegerField(
        label = "<p><b>2)</b>Género</p>",
        widget = widgets.RadioSelectHorizontal,
        choices = [[0, "Masculino"], [1, "Femenino"], [2, "Otro"]])
    edu_lvl = models.IntegerField(
        label = "<p><b>3)</b> Último nivel educativo alcanzado: </p>",
        widget = widgets.RadioSelectHorizontal,
        choices = [[0, "Secundaria"],
                   [1, "Técnico"],
                   [2, "Profesional"],
                   [3, "Posgrado"]])

    R1 = models.IntegerField(label = "",
                             widget = widgets.RadioSelectHorizontal,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R2 = models.IntegerField(label = "",
                             widget = widgets.RadioSelectHorizontal,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R3 = models.IntegerField(widget = widgets.RadioSelect,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R4 = models.IntegerField(widget = widgets.RadioSelect,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R5 = models.IntegerField(widget = widgets.RadioSelect,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R6 = models.IntegerField(widget = widgets.RadioSelect,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    R7 = models.IntegerField(widget = widgets.RadioSelect,
                             choices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], )
    M1 = models.IntegerField(widget = widgets.RadioSelect,
                             choices =
                             [[0, "Sí"],
                              [1, "No"],
                              [2, "NS/NR"]],
                             )
    M2a = models.IntegerField(widget = widgets.RadioSelect,
                              choices =
                              [[1, "MP"],
                               [2, "AP"],
                               [3, "AN"],
                               [4, "MN"],
                               ], )
    M2b = models.IntegerField(widget = widgets.RadioSelect,
                              choices =
                              [[1, "MP"],
                               [2, "AP"],
                               [3, "AN"],
                               [4, "MN"]
                               ], )
    M2c = models.IntegerField(widget = widgets.RadioSelect,
                              choices =
                              [[1, "MP"],
                               [2, "AP"],
                               [3, "AN"],
                               [4, "MN"]
                               ])

    M2d = models.IntegerField(widget = widgets.RadioSelect,
                              choices =
                              [[1, "MP"],
                               [2, "AP"],
                               [3, "AN"],
                               [4, "MN"]
                               ])

    M3 = models.IntegerField(widget = widgets.RadioSelect,
                             choices =
                             [[1, "Lo beneficia"],
                              [2, "Lo perjudica"],
                              [3, "Ni lo beneficia ni lo perjudica"],
                              [4, "NS/NR"]])

    M4a = models.IntegerField(widget = widgets.RadioSelect,
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])
    M4b = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Los inmigrantes vienen a competir por nuestros puestos de trabajo",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4c = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Los inmigrantes causan un aumento del crimen",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4d = models.IntegerField(widget = widgets.RadioSelect,
                              label = "LLos inmigrantes mejoran nuestra sociedad con ideas y cultura",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4e = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Los inmigrantes son una carga para el Estado",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4f = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Los inmigrantes le dan al país más de lo que reciben",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4g = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Nuestro país debería ayudar a los inmigrantes que sufren persecución política en sus países",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M4h = models.IntegerField(widget = widgets.RadioSelect,
                              label = "Los inmigrantes deberían tener el mismo acceso a la salud, educación y vivienda que los ciudadanos colombianos",
                              choices =
                              [[1, "MA"],
                               [2, "A"],
                               [3, "D"],
                               [4, "MD"]])

    M5 = models.IntegerField(widget = widgets.RadioSelect,
                             choices =
                             [[1, "Enviarlos inmediatamente de regreso a su país de origen"],
                              [2, "Permitir que se queden un tiempo limitado"],
                              [3, "Permitir que se queden el tiempo que quieran"],
                              [4, "NS/NR"]])

    tipo_cuenta = models.IntegerField(widget = widgets.RadioSelectHorizontal,
                                      choices = [[1, "Ahorros"],
                                                 [2, "Corriente"],
                                                 [3, "Nequi"]],
                                      blank = False)

    nro_cuenta = models.IntegerField(initial = 0, blank = False)

    lab_id = models.StringField(initial = 0)

    def set_id(self):
        participant_label = self.participant.label
        self.lab_id = participant_label
