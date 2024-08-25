from otree.api import *
from .models import *
import random
class MyPage(Page):
    pass

class Espera(WaitPage):
    print("Espere mientras los demás jugadores terminen")

class ResultsWaitPage(WaitPage):
    pass


class Instrucciones_1(Page):
    pass


class Instrucciones_2(Page):
    pass


class Instrucciones_3(Page):
    pass

class Cuestionario(Page):
    form_model = 'player'
    form_fields = ['age', 'gender', 'edu_lvl', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6', 'R7',
                   'M1', 'M2a', 'M2b', 'M2c', 'M2d' ,'M3', 'M4a', 'M4b', 'M4c', 'M4d', 'M4e',
                   'M4f', 'M4g', 'M4h', 'M5' ]


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



class Ronda_1_ind(Page):
    n_round=0
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_1 = 'A'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round']
        }

class Ronda_2_ind(Page):
    n_round=1
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_2 = 'A'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_3_ind(Page):
    n_round=2
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_3 = 'B'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }
class Ronda_4_ind(Page):
    n_round=3
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_4 = 'A'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_5_ind(Page):
    n_round=4
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_5 = 'A'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_6_ind(Page):
    n_round=5
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_6 = 'A'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_7_ind(Page):
    n_round=6
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_7 = 'B'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }

class Ronda_8_ind(Page):
    n_round=7
    form_model = 'player'
    form_fields = ['selected_round_'+str(n_round+1), 'tokens_round_'+str(n_round+1)]
    def vars_for_template(self):
        self.player.winner_round_8 = 'B'
        lst_order = ['A', 'B']
        #random.shuffle(lst_order) #aleatorizar entre A y B
        #print(lst_order)

        return {
            'worker_1': C.hvs[self.n_round][lst_order[0]], #Cuando barajó traiga el primero que quedó
            'worker_2': C.hvs[self.n_round][lst_order[1]],
            'text': C.hvs[self.n_round]['text'],
            'round': C.hvs[self.n_round]['round'],
        }
######################################################################
class Pagos_ind(Page):
    def vars_for_template(self):
        #n_rounds_payoff = C.n_rounds_payoff
        n_rounds_payoff = 4
        lst_rounds = list(range(1, C.n_rounds+1)) ## Ya aparece 1,2,3 no 0,1,2
        print("lista desordenada: ", lst_rounds)
        random.shuffle(lst_rounds)
        lst_rounds = lst_rounds[:n_rounds_payoff]
        print("lista de rondas escogidas", lst_rounds)
        self.player.tokens_encription = self.participant.vars.get('payout', 0)
        
        # Escoger el ganador de cada ronda
        ## Primero obtener todos los jugadores en la subsesión
        players_per_subse = self.subsession.get_players()
        print(players_per_subse)
        round_1 = []
        round_2 = []
        round_3 = []
        round_4 = []
        round_5 = []
        round_6 = []
        round_7 = []
        round_8 = []
        for p in players_per_subse:
            round_1.append(p.selected_round_1)
            round_2.append(p.selected_round_2)
            round_3.append(p.selected_round_3)
            round_4.append(p.selected_round_4)
            round_5.append(p.selected_round_5)
            round_6.append(p.selected_round_6)
            round_7.append(p.selected_round_7)
            round_8.append(p.selected_round_8)

        #Remover el voto del jugador
        ## Ronda 1

        """if self.player.selected_round_1 == 'A':
            round_1.remove('A')
        elif self.player.selected_round_1 == 'B':
            round_1.remove('B')

        ## Ronda 2
        if self.player.selected_round_2 == 'A':
            round_2.remove('A')
        elif self.player.selected_round_2 == 'B':
            round_2.remove('B')

        ## Ronda 3
        if self.player.selected_round_3 == 'A':
            round_3.remove('A')
        elif self.player.selected_round_3 == 'B':
            round_3.remove('B')

        ## Ronda 4
        if self.player.selected_round_4 == 'A':
            round_4.remove('A')
        elif self.player.selected_round_4 == 'B':
            round_4.remove('B')

        ## Ronda 5
        if self.player.selected_round_5 == 'A':
            round_5.remove('A')
        elif self.player.selected_round_5 == 'B':
            round_5.remove('B')
            
        ## Ronda 6
        if self.player.selected_round_6 == 'A':
            round_6.remove('A')
        elif self.player.selected_round_6 == 'B':
            round_6.remove('B')
            
        ## Ronda 7
        if self.player.selected_round_7 == 'A':
            round_7.remove('A')
        elif self.player.selected_round_7 == 'B':
            round_7.remove('B')
            
        ## Ronda 8
        if self.player.selected_round_8 == 'A':
            round_8.remove('A')
        elif self.player.selected_round_8 == 'B':
            round_1.remove('B')    """

        # Escoger el más elegido de cada ronda
        ## Ronda_1

        self.subsession.count_ronda1_a = round_1.count('A')
        self.subsession.count_ronda1_b = round_1.count('B')
        if self.player.selected_round_1 == 'A':
            self.subsession.count_ronda1_a -=1
        elif self.player.selected_round_1 == 'B':
            self.subsession.count_ronda1_b -=1
        if self.subsession.count_ronda1_a > self.subsession.count_ronda1_b:
            self.player.grupo_winner_round_1 = 'A'
        elif  self.subsession.count_ronda1_a < self.subsession.count_ronda1_b:
            self.player.grupo_winner_round_1 = 'B'
        else:
            self.player.grupo_winner_round_1 = 'Empate'

        ## Ronda_2
        self.subsession.count_ronda2_a = round_2.count('A')
        self.subsession.count_ronda2_b = round_2.count('B')
        if self.player.selected_round_2 == 'A':
            self.subsession.count_ronda2_a -= 1
        elif self.player.selected_round_2 == 'B':
            self.subsession.count_ronda2_b -= 1
        if self.subsession.count_ronda2_a > self.subsession.count_ronda2_b:
            self.player.grupo_winner_round_2 = 'A'
        elif self.subsession.count_ronda2_a < self.subsession.count_ronda2_b:
            self.player.grupo_winner_round_2 = 'B'
        else:
            self.player.grupo_winner_round_2 = 'Empate'

        ## Ronda_3
        self.subsession.count_ronda3_a = round_3.count('A')
        self.subsession.count_ronda3_b = round_3.count('B')
        if self.player.selected_round_3 == 'A':
            self.subsession.count_ronda3_a -= 1
        elif self.player.selected_round_3 == 'B':
            self.subsession.count_ronda3_b -= 1
        if self.subsession.count_ronda3_a > self.subsession.count_ronda3_b:
            self.player.grupo_winner_round_3 = 'A'
        elif self.subsession.count_ronda3_a < self.subsession.count_ronda3_b:
            self.player.grupo_winner_round_3 = 'B'
        else:
            self.player.grupo_winner_round_3 = 'Empate'

        ## Ronda_4
        self.subsession.count_ronda4_a = round_4.count('A')
        self.subsession.count_ronda4_b = round_4.count('B')
        if self.player.selected_round_4 == 'A':
            self.subsession.count_ronda4_a -= 1
        elif self.player.selected_round_4 == 'B':
            self.subsession.count_ronda4_b -= 1
        if self.subsession.count_ronda4_a > self.subsession.count_ronda4_b:
            self.player.grupo_winner_round_4 = 'A'
        elif self.subsession.count_ronda4_a < self.subsession.count_ronda4_b:
            self.player.grupo_winner_round_4 = 'B'
        else:
            self.player.grupo_winner_round_4 = 'Empate'

        ## Ronda_5
        self.subsession.count_ronda5_a = round_5.count('A')
        self.subsession.count_ronda5_b = round_5.count('B')
        if self.player.selected_round_5 == 'A':
            self.subsession.count_ronda5_a -= 1
        elif self.player.selected_round_5 == 'B':
            self.subsession.count_ronda5_b -= 1
        if self.subsession.count_ronda5_a > self.subsession.count_ronda5_b:
            self.player.grupo_winner_round_5 = 'A'
        elif self.subsession.count_ronda5_a < self.subsession.count_ronda5_b:
            self.player.grupo_winner_round_5 = 'B'
        else:
            self.player.grupo_winner_round_5 = 'Empate'

        ## Ronda_6
        self.subsession.count_ronda6_a = round_6.count('A')
        self.subsession.count_ronda6_b = round_6.count('B')
        if self.player.selected_round_6 == 'A':
            self.subsession.count_ronda6_a -= 1
        elif self.player.selected_round_6 == 'B':
            self.subsession.count_ronda6_b -= 1
        if self.subsession.count_ronda6_a > self.subsession.count_ronda6_b:
            self.player.grupo_winner_round_6 = 'A'
        elif self.subsession.count_ronda6_a < self.subsession.count_ronda6_b:
            self.player.grupo_winner_round_6 = 'B'
        else:
            self.player.grupo_winner_round_6 = 'Empate'

        ## Ronda_7
        self.subsession.count_ronda7_a = round_7.count('A')
        self.subsession.count_ronda7_b = round_7.count('B')
        if self.player.selected_round_7 == 'A':
            self.subsession.count_ronda7_a -= 1
        elif self.player.selected_round_7 == 'B':
            self.subsession.count_ronda7_b -= 1
        if self.subsession.count_ronda7_a > self.subsession.count_ronda7_b:
            self.player.grupo_winner_round_7 = 'A'
        elif self.subsession.count_ronda7_a < self.subsession.count_ronda7_b:
            self.player.grupo_winner_round_7 = 'B'
        else:
            self.player.grupo_winner_round_7 = 'Empate'

        ## Ronda_8
        self.subsession.count_ronda8_a = round_8.count('A')
        self.subsession.count_ronda8_b = round_8.count('B')
        if self.player.selected_round_8 == 'A':
            self.subsession.count_ronda8_a -= 1
        elif self.player.selected_round_8 == 'B':
            self.subsession.count_ronda8_b -= 1
        if self.subsession.count_ronda8_a > self.subsession.count_ronda8_b:
            self.player.grupo_winner_round_8 = 'A'
        elif self.subsession.count_ronda8_a < self.subsession.count_ronda8_b:
            self.player.grupo_winner_round_8 = 'B'
        else:
            self.player.grupo_winner_round_8 = 'Empate'

    #Escoger el ganador de cada ronda
        ## Ronda_1


##rondas para pagar serían a, b, c y d
        ##Diccionario de ganadores        Acá llamo el ganador que defino en models.
        winners = {
            1: {'winner': self.player.winner_round_1, 'my_choose': self.player.selected_round_1,
                'tokens': self.player.tokens_round_1},
            2: {'winner': self.player.winner_round_2, 'my_choose': self.player.selected_round_2,
                'tokens': self.player.tokens_round_2},
            3: {'winner': self.player.winner_round_3, 'my_choose': self.player.selected_round_3,
                'tokens': self.player.tokens_round_3},
            4: {'winner': self.player.winner_round_4, 'my_choose': self.player.selected_round_4,
                'tokens': self.player.tokens_round_4},
            5: {'winner': self.player.winner_round_5, 'my_choose': self.player.selected_round_5,
                'tokens': self.player.tokens_round_5},
            6: {'winner': self.player.winner_round_6, 'my_choose': self.player.selected_round_6,
                'tokens': self.player.tokens_round_6},
            7: {'winner': self.player.winner_round_7, 'my_choose': self.player.selected_round_7,
                'tokens': self.player.tokens_round_7},
            8: {'winner': self.player.winner_round_8, 'my_choose': self.player.selected_round_8,
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
        self.player.tokens_individual = self.player.round_a_to_payoff_tokens + self.player.round_b_to_payoff_tokens + self.player.round_c_to_payoff_tokens + self.player.round_d_to_payoff_tokens
        self.player.tokens_acum = self.player.tokens_individual + self.player.tokens_encription

        return {
            'rounds_to_payoff': lst_rounds, ## las rondas que vamos a pagar
            'winners': winners,
            'tokens_individual': self.player.tokens_individual,
            'tokens_encription': self.player.tokens_encription,
            'tokens_acum': self.player.tokens_acum,
            'pago_monetario_final': self.player.tokens_acum * 200

        }




    def before_next_page(self):
        self.participant.vars['pago_monetario_final'] = self.player.tokens_acum * 200
        self.participant.vars['tokens_total_ind'] = self.player.tokens_individual
        self.participant.vars['winner_round_1'] = self.player.grupo_winner_round_1
        self.participant.vars['winner_round_2'] = self.player.grupo_winner_round_2
        self.participant.vars['winner_round_3'] = self.player.grupo_winner_round_3
        self.participant.vars['winner_round_4'] = self.player.grupo_winner_round_4
        self.participant.vars['winner_round_5'] = self.player.grupo_winner_round_5
        self.participant.vars['winner_round_6'] = self.player.grupo_winner_round_6
        self.participant.vars['winner_round_7'] = self.player.grupo_winner_round_7
        self.participant.vars['winner_round_8'] = self.player.grupo_winner_round_8



    def is_displayed(self):
        return self.round_number == 1

rondas = [Ronda_1_ind, Ronda_2_ind, Ronda_3_ind, Ronda_4_ind, Ronda_5_ind, Ronda_6_ind, Ronda_7_ind, Ronda_8_ind]
random.shuffle(rondas)


page_sequence = [Instrucciones_1, Instrucciones_2, Instrucciones_3, Prueba] + rondas + [Espera, Pagos_ind] #[Instrucciones_1, Instrucciones_2, Instrucciones_3,, Prueba] + rondas + [Espera, Pagos_ind]
print("order pages", page_sequence)

