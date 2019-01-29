##### Basic PetriNet Framework ##### 

class Place():
    def __init__(self, name = 'untitled_place'):
        self.name = name
        self.tokens = 0

    def set_tokens(self,val):
        self.tokens += val
        if(self.tokens < 0):
            print('No token at: |'+ self.name + '|')
            self.tokens = 0
            return False
        return True
    def get_tokens(self):
        return self.tokens


class Transition():
    def __init__(self,name = 'untitled_transition'):
        self.name = name
        self.input_places = []
        self.output_places = []

    def make_connections(self,place,type):
        if type == 'input':
            self.input_places.append(place)
        elif type == 'output':
            self.output_places.append(place)
        else:
            print('Wrong Input type given. Try: input or output')

    def play_transition(self):

        is_transition_possible = True
        for place in self.input_places:
            place_has_token = place.set_tokens(-1)
            is_transition_possible = is_transition_possible and place_has_token

        if not is_transition_possible:
            print('Transition not allowed: |'+ self.name +'|')
        else:
            for place in self.output_places:
                place.set_tokens(1)


class PetriNet():
    def __init__(self,name = 'untitled_framework'):
        self.name = name
        self.transitions = {}
        self.places = {}

    def make_framework(self,transition_groups):   # group = [transition_name, [list of inputs],[list of outputs]]
        for group in transition_groups:
            transition_name = group[0]
            input_places = group[1]
            output_places = group[2]

            transition = Transition(transition_name)
            for input_place in input_places:
                if input_place in self.places:
                    place = self.places[input_place]
                else:
                    place = Place(input_place)
                    self.places[input_place] = place
                transition.make_connections(place,'input')
            for output_place in output_places:
                if output_place in self.places:
                    place = self.places(output_place)
                else:
                    place = Place(output_place)
                    self.places[output_place] = place
                transition.make_connections(place,'output')

            self.transitions[transition_name] = transition

    def play_framework(self,transition_sequence): # ['t1','t2']
        self.print(0)
        for i,transition in enumerate(transition_sequence):
            self.transitions[transition].play_transition()
            self.print(i+1)

    def print(self,iter):
        print('______TRANSITION: '+str(iter)+'______')
        print('place\t\t\ttokens')
        print('`````\t\t\t``````')
        for place in self.places:
            if self.places[place].tokens or 1:
                print('{}\t\t\t\t{}'.format(self.places[place].name,self.places[place].tokens))


p = PetriNet('PetriNet')
p.make_framework([['t1',['st'],['a','b']],['t2',['a','b'],['end']]])
p.places['st'].set_tokens(1)
p.play_framework(['t1','t2'])





