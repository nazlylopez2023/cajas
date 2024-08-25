from otree.api import *
import random






doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'apuesta_firmas'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    n_rounds = 8
    n_rounds_payoff = 4
    fee = 350
    pag = ['Ronda_1','Ronda_2', 'Ronda_3', 'Ronda_4', 'Ronda_5','Ronda_6','Ronda_7','Ronda_8']
    num_rondas =len(pag)

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
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '21.479.XXX',
                'lug_nac': 'Maracay (Venezuela)',
                'age': '37',
                'las_exp': ['Orientador trámites de tránsito - Entre 3 y 6 meses',
                            'Lavador de vehículos - Entre 3 y 6 meses',
                            'Lavador de vehículos - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.023.874.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '29',
                'las_exp': ['Operario de aseo - Más de 12 meses',
                            'Ayudante de pastelería - Entre 3 y 6 meses',
                            'Operario de aseo - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',

            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>asistente de supervisor de aseo.</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño </b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '1'
        },

        # hoja de vida # 1
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.016.060.XXX',
                'lug_nac': 'Puerto Leguízamo (Putumayo)',
                'age': '29',
                'las_exp': ['Mesero - Entre  7 y 9 meses',
                            'Domiciliario - Entre 3 y 6 meses',
                            'Mesero - Entre 10 y 12 meses meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '26.631.XXX',
                'lug_nac': 'Barquisimento (Venezuela)',
                'age': '26',
                'las_exp': ['Mesero - Entre 7 y 9 meses',
                            'Mesero - Más de 12 meses',
                            'Vendedor negocio familiar - Entre 10 y 12 meses',
                            ],

                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>despachador de domicilios en restaurante</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '2'
        },
        # hoja de vida # 2
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.010.203.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '31',
                'las_exp': ['Asistente administrativo - Más de 12 meses',
                            'Gerente comercial - Más de 12 meses',
                            'Desarrollador de software - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '80.772.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '38',
                'las_exp': ['Auxiliar de Bodega - Más de 12 meses',
                            'Auxiliar postal - Más de 12 meses',
                            'Codificador de sistemas - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>secretario/recepcionista</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '3'
        },
        # hoja de vida # 3
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.065.613.XXX',
                'lug_nac': 'Valledupar (Cesar)',
                'age': '33',
                'las_exp': ['Vendedor restaurante de cadena - Más de 12 meses ',
                            'Vigilante - Entre 7 y 9 meses',
                            'Auxiliar restaurante de cadena - Más de 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '749.XXX',
                'lug_nac': 'Valencia (Venezuela)',
                'age': '32',
                'las_exp': ['Auxiliar tienda de cadena - Entre 3 y 6 meses',
                            'Mesero - Más de 12 meses',
                            'Cajero de Movistar Arena - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>supervisor de tienda</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '4'
        },

        # hoja de vida # 4
        {
            'A': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '4.668.XXX',
                'lug_nac': 'San Cristóbal (Venezuela)',
                'age': '33',
                'las_exp': ['Vendedor de fruver - Entre 7 y 9 meses',
                            'Vendedor de tienda - Entre 3 y 6 meses',
                            'Vendedor de fruver - Más de 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '1.252.XXX',
                'lug_nac': 'Villa de Cura (Venezuela)',
                'age': '26',
                'las_exp': ['Vendedor independiente - Más de 12 meses',
                            'Vendedor de fruver - Entre 7 y 9 meses',
                            'Vendedor de fruver - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>supervisor de mini mercado</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '5'
        },
        # hoja de vida # 5
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.071.579.XXX',
                'lug_nac': 'Caparrapí (Cundinamarca)',
                'age': '33',
                'las_exp': ['Operario de corrugados - Más de 12 meses',
                            'Operario máquina de inyección de suelas - Más de 12 meses',
                            'Operario de perforación - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso de Protección Especial',
                'num_doc': '5.112.XXX',
                'lug_nac': 'San Felipe (Venezuela)',
                'age': '33',
                'las_exp': ['Supervisor de producción - Más de 12 meses',
                            'Operario de producción - Más de 12 meses',
                            'Ayudante en plaza de mercados - Entre 7 y 9 meses'
                            ],
                'lvl_edu': 'Secundaria',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>coordinador de personal de operaciones</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '6'
        },
        # hoja de vida # 6
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.233.503.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '24',
                'las_exp': ['Mensajero - Entre 7 y 8 meses',
                            'Vendedor - Entre 3 y 6 meses',
                            'Auxiliar logístico - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.022.428.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '26',
                'las_exp': ['Mensajero - Más de 12 meses',
                            'Vendedor - Más de 12 meses',
                            'Asistente de ventas - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Universitario',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>asesor de ventas</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '7'
        },
        # hoja de vida # 7

        {
            'A': {
                'tipo_doc': 'Cédula de Extranjería',
                'num_doc': '25.242.XXX',
                'lug_nac': 'Monagas (Venezuela)',
                'age': '27',
                'las_exp': ['Domiciliario - Entre 10 y 12 meses',
                            'Encargado de supermercado - Más de 12 meses',
                            'Vendedor - Entre 3 y 6 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Permiso Especial de Permanencia',
                'num_doc': '22.283.XXX',
                'lug_nac': 'Caracas (Venezuela)',
                'age': '28',
                'las_exp': ['Cajero de supermercado - Más de 12 meses',
                            'Domiciliario - Entre 7 y 9 meses',
                            'Domiciliario - Entre 10 y 12 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',
            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>supervisor despachos de domicilios</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '8'
        },
    ]

    prueba = [
        # hoja de vida de la ronda # 0
        {
            'A': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '32.355.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '38',
                'las_exp': ['Supernumerario banco - Entre 10 y 12 meses',
                            'Administrador tienda de cadena - Entre 3 y 6 meses',
                            'Vendedor tienda de cadena - Entre 7 y 9 meses'
                            ],
                'lvl_edu': 'Técnico',
                'type': 'A',
            },

            'B': {
                'tipo_doc': 'Cédula de Ciudadanía',
                'num_doc': '1.026.734.XXX',
                'lug_nac': 'Bogotá D.C.',
                'age': '36',
                'las_exp': ['Cajero en banco - Más de 12 meses ',
                            'Asesor venta de celulares - Entre 3 y 6 meses',
                            'Administrador minimercado - Entre 7 y 9 meses '
                            ],
                'lvl_edu': 'Técnico',
                'type': 'B',

            },
            'text': "El candidato A y el candidato B se están presentando para un puesto vacante de <b>coordinador de bodega.</b> <br> ¿<b>Quién cree que está mejor posicionado en el ranking de desempeño</b> y, por tanto, se espera de él un mejor rendimiento laboral?",
            'round': '1'
        }]



class Subsession(BaseSubsession):
    


    def creating_session(subsession):
        #import random
        if subsession.round_number == 1:
            for player in subsession.get_players():
                round_numbers = list(range(1, C.num_rondas+1))
                random.shuffle(round_numbers)
                print(round_numbers)
                player.participant.vars['rondas'] = dict(zip(C.pag, round_numbers))
                print(player.participant.vars['rondas'])

        






class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #def set_round_information(self):
        #if self.round_number == 1:
            #round_numbers = list(range(1, 9))
            #random.shuffle(round_numbers)
            #print(round_numbers)
            #self.participant.vars['rondas'] = dict(zip(C.pag, round_numbers))
            #print(self.participant.vars['rondas'])


        #for i in range(1, 9):
            #setattr(self, f'winner_{i}', '')

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



    winner_1 = models.StringField()
    winner_2 = models.StringField()
    winner_3 = models.StringField()
    winner_4 = models.StringField()
    winner_5 = models.StringField()
    winner_6 = models.StringField()
    winner_7 = models.StringField()
    winner_8 = models.StringField()


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
    tokens_firmas = models.IntegerField()

 ## tokens acumulados menos el fee
    tokens_acum = models.IntegerField()

# tokens acumulados que me traje de la etapa 1 y 2
    tokens_rondas = models.IntegerField()

# tokens acumulados en todas las rondas
    tokens_finales = models.IntegerField()

# tokens que traje de la tarea de decodificación
    tokens_encription = models.IntegerField()

# tokens que traje de la prueba individual
    tokens_indi = models.IntegerField()

# tokens que traje de la predicción de grupo
    tokens_total_grupo = models.IntegerField()

# tokens en plata
    pago_monetario = models.IntegerField()

# Conteo de errores en la prueba
    mistakes = models.IntegerField(initial = 0, blank = True)




#----------------- Cuestionario ----------------#

    age = models.IntegerField(label = "<p><b>1)</b>Edad</p>")
    gender = models.IntegerField(
        label = "<p><b>2)</b>Género</p>",
        widget = widgets.RadioSelectHorizontal,
        choices=[[0, "Masculino"], [1, "Femenino"], [2, "Otro"]])
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
                              [2,"NS/NR"]],
                             )
    M2a = models.IntegerField(widget = widgets.RadioSelect,
                             choices =
                             [[1, "MP"],
                              [2, "AP"],
                              [3, "AN"],
                              [4, "MN"],
                             ],)
    M2b = models.IntegerField(widget = widgets.RadioSelect,
                            choices =
                            [[1, "MP"],
                             [2, "AP"],
                             [3, "AN"],
                             [4, "MN"]
                             ],)
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
