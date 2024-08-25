from otree.api import *
from .models import *
import random
from random import sample
class MyPage(Page):
    pass

class Espera(WaitPage):
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

class Instrucciones(Page):
    pass

from otree.api import Page


class Prueba(Page):
    form_model = 'player'
    form_fields = ['mistakes']

    def vars_for_template(self):
        # Puedes definir cualquier lógica adicional aquí si necesitas pasar datos al template
        return {}

    def error_count(self):
        # Implementa la lógica para contar errores aquí
        # Por ejemplo, puedes verificar el valor del campo mistakes y realizar algún cálculo
        # Por simplicidad, aquí suponemos que 'mistakes' está definido y es accesible de alguna manera
        # Puedes ajustar esta lógica según tus necesidades específicas
        # Aquí, simplemente asumimos que obtienes el valor de algún lugar
        return self.player.mistakes

    def before_next_page(self):
        # Llama a la función de conteo de errores y actualiza el modelo del jugador
        self.player.mistakes = self.error_count()



    #form_model = 'player'
    #form_fields = ['selected_round_' + str(n_round + 1), 'tokens_round_' + str(n_round + 1)]
    #def vars_for_template(self):
        #self.player.winner_round_1 = 'B'
        #lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        #return {
            #'worker_1': C.prueba[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            #'worker_2': C.prueba[self.n_round][lst_order[1]],
            #'text': C.prueba[self.n_round]['text'],
            #'round': C.prueba[self.n_round]['round']
        #}

class Ronda_1_fir(Page):
    #def is_displayed(self):
        #return self.round_number == self.player.participant.vars['rondas']['Ronda_1']

    n_round=0
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]

    def vars_for_template(self):

        lst_order = ['A', 'B']
        self.player.winner_1 = 'B' ## FUE EL MÁS ELEGIDO POR LAS EMPRESAS, LE ATINARON
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }
    #def before_next_page(self):
        #self.player.winner_2 = 'B'

class Ronda_2_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_2']

    n_round=1
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        self.player.winner_2 = 'A' ## COL, EL MÁS ELEGIDO POR LAS EMPRESAS LE ATINARON
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

    #def before_next_page(self):
        #self.player.winner_3 = 'B'


class Ronda_3_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_3']

    n_round=2
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        self.player.winner_3 = 'A'  ## EL MEJOR ERA B, LA ELECCIÓN DE LAS EMPRESAS FUE A (QUIEN GANÓ LO PUEDO VER EN LA APP DE LAS EMPRESAS)
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)



        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

    #def before_next_page(self):
        #self.player.set_round_information()




class Ronda_4_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_4']

    n_round=3
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        self.player.winner_4 = 'B'  ## EL MEJOR ERA B, LAS EMPRESAS LE ATINARON
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)


        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

    #def before_next_page(self):
        #self.player.set_round_information()


class Ronda_5_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_5']

    n_round=4
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]

    def vars_for_template(self):
        self.player.winner_5 = 'B' ## EL GANADOR ERA A, LAS EMPRESAS ESCOGIERON B
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)


        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],

        }

    #def before_next_page(self):
        #self.player.set_round_information()

class Ronda_6_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_6']

    n_round=5
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        self.player.winner_6 = 'B'   ## EL MEJOR ERA B, LAS EMPRESAS LE ATINARON
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],

        }

    #def before_next_page(self):
        #self.player.set_round_information()


class Ronda_7_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_6']

    n_round=6
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        self.player.winner_7 = 'B'     ## EL GANADOR ERA B, LAS EMPRESAS LE ATINARON
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)


        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],

        }

    #def before_next_page(self):
        #self.player.set_round_information()

class Ronda_8_fir(Page):
    #def is_displayed(self):
        #return self.player.round_number == self.player.participant.vars['rondas']['Ronda_5']

    n_round=7
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]


    def vars_for_template(self):
        lst_order = ['A', 'B']
        self.player.winner_8 = 'A' ## EL GANADOR ERA A, LAS EMPRESAS LE ATINARON
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)


        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

    #def before_next_page(self):
        #self.player.set_round_information()



######################################################################
class Pagos_firmas(Page):

    def vars_for_template(self):
        #n_rounds_payoff = C.n_rounds_payoff
        n_rounds_payoff = 4
        lst_rounds = list(range(1, C.num_rondas+1)) ## Ya aparece 1,2,3 no 0,1,2
        #print("lista desordenada: ", lst_rounds)
        random.shuffle(lst_rounds)
        lst_rounds = lst_rounds[:n_rounds_payoff]
        #print("lista de rondas escogidas", lst_rounds)
        self.player.tokens_rondas = self.participant.vars.get('tokens_rondas', 0)
        self.player.tokens_encription = self.participant.vars.get('payout', 0)
        self.player.tokens_indi = self.participant.vars.get('tokens_total_ind', 0)
        self.player.tokens_total_grupo = self.participant.vars.get('tokens_total_grupo', 0)



##rondas para pagar serían a, b, c y d
        ##Diccionario de ganadores        Acá llamo el ganador que defino en models.
        winners = {
            1: {'winner': self.player.winner_1 , 'my_choose': self.player.selected_round_1,
                'tokens': self.player.tokens_round_1},
            2: {'winner': self.player.winner_2, 'my_choose': self.player.selected_round_2,
                'tokens': self.player.tokens_round_2},
            3: {'winner': self.player.winner_3, 'my_choose': self.player.selected_round_3,
                'tokens': self.player.tokens_round_3},
            4: {'winner': self.player.winner_4, 'my_choose': self.player.selected_round_4,
                'tokens': self.player.tokens_round_4},
            5: {'winner': self.player.winner_5, 'my_choose': self.player.selected_round_5,
                'tokens': self.player.tokens_round_5},
            6: {'winner': self.player.winner_6, 'my_choose': self.player.selected_round_6,
                'tokens': self.player.tokens_round_6},
            7: {'winner': self.player.winner_7, 'my_choose': self.player.selected_round_7,
                'tokens': self.player.tokens_round_7},
            8: {'winner': self.player.winner_8, 'my_choose': self.player.selected_round_8,
                'tokens': self.player.tokens_round_8},
        }
        ## rondas a pagar son 4 y serían a, b, c y d

        ## guardar el número de la primera ronda a pagar -> a
        self.player.round_a_to_payoff_selected = str(lst_rounds[0])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[0]]['winner'] == winners[lst_rounds[0]]['my_choose']):
            self.player.round_a_to_payoff_tokens = winners[lst_rounds[0]]['tokens'] * 1
        else:
            self.player.round_a_to_payoff_tokens = winners[lst_rounds[0]]['tokens'] * -1

        ## guardar el número de la segunda ronda a pagar -> b
        self.player.round_b_to_payoff_selected = str(lst_rounds[1])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[1]]['winner'] == winners[lst_rounds[1]]['my_choose']):
            self.player.round_b_to_payoff_tokens = winners[lst_rounds[1]]['tokens'] * 1
        else:
            self.player.round_b_to_payoff_tokens = winners[lst_rounds[1]]['tokens'] * -1

        ## guardar el número de la segunda ronda a pagar -> c
        self.player.round_c_to_payoff_selected = str(lst_rounds[2])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[2]]['winner'] == winners[lst_rounds[2]]['my_choose']):
            self.player.round_c_to_payoff_tokens = winners[lst_rounds[2]]['tokens'] * 1
        else:
            self.player.round_c_to_payoff_tokens = winners[lst_rounds[2]]['tokens'] * -1

        ## guardar el número de la segunda ronda a pagar -> d
        self.player.round_d_to_payoff_selected = str(lst_rounds[3])
        ## y lo que ganó o perdió en tokens
        if (winners[lst_rounds[3]]['winner'] == winners[lst_rounds[3]]['my_choose']):
            self.player.round_d_to_payoff_tokens = winners[lst_rounds[3]]['tokens'] * 1
        else:
            self.player.round_d_to_payoff_tokens = winners[lst_rounds[3]]['tokens'] * -1

## Total de tokens por jugador
        self.player.tokens_firmas = self.player.round_a_to_payoff_tokens + self.player.round_b_to_payoff_tokens + self.player.round_c_to_payoff_tokens + self.player.round_d_to_payoff_tokens
        self.player.tokens_acum = self.player.tokens_total_grupo + self.player.tokens_indi + self.player.tokens_encription
        self.player.tokens_finales = self.player.tokens_encription + self.player.tokens_indi + self.player.tokens_total_grupo + self.player.tokens_firmas
        self.player.pago_monetario = self.player.tokens_finales * 200
        return {
            'rounds_to_payoff': lst_rounds, ## las rondas que vamos a pagar
            'winners': winners,
            'tokens_firmas': self.player.tokens_firmas,
            'tokens_acum': self.player.tokens_acum,
            'tokens_encription': self.player.tokens_encription,
            'tokens_indi': self.player.tokens_indi,
            'tokens_total_grupo': self.player.tokens_total_grupo,
            'tokens_finales': self.player.tokens_finales,
            'pago_monetario_final': self.player.pago_monetario,
        }


    ##def before_next_page(self):
        ##self.participant.vars['tokens_total_firma'] = self.player.tokens_firmas
        ##self.participant.vars['pago_monetario'] = self.player.pago_monetario


class Cuestionario(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'edu_lvl', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7',
                   'M1', 'M2a', 'M2b', 'M2c', 'M2d' ,'M3', 'M4a', 'M4b', 'M4c', 'M4d', 'M4e',
                   'M4f', 'M4g', 'M4h', 'M5' ]

class Cuenta(Page):
    form_model = "player"
    form_fields = ['tipo_cuenta', 'nro_cuenta']

    player = 'models.Player'


    def vars_for_template(self):
        self.player.pago_monetario = self.participant.vars.get('pago_monetario', 0)
        self.player.set_id()
        return {
            'lab_id': self.player.lab_id,
            'pago_monetario': self.player.pago_monetario
        }

    def is_displayed(self):
        return self.round_number == 1

class Cuenta_FORM(Page):
    form_model = "player"
    form_fields = ['tipo_cuenta', 'nro_cuenta']

    player = 'models.Player'


    def vars_for_template(self):
        self.player.pago_monetario = self.participant.vars.get('pago_monetario', 0)
        self.player.set_id()
        return {
            'lab_id': self.player.lab_id,
            'pago_monetario': self.player.pago_monetario
        }

    def is_displayed(self):
        return self.round_number == 1

rondas = [Ronda_1_fir, Ronda_2_fir, Ronda_3_fir, Ronda_4_fir, Ronda_5_fir, Ronda_6_fir, Ronda_7_fir, Ronda_8_fir]
random.shuffle(rondas)

page_sequence = [Instrucciones] + rondas + [Pagos_firmas, Cuestionario, Cuenta_FORM]  #, [Instrucciones_1, Instrucciones_2, Instrucciones_3, Prueba] + rondas + [Pagos_firmas]




