from automat import *
import string
class DomolAutomat(Automat):
    def __init__(self, alphabet, state_transitions, start_state, accepting_states, backup, read):
        super().__init__(alphabet, state_transitions, start_state, accepting_states)
        self.backup = backup
        self.read = read 

    def validate(self, s):
        self.state = self.start_state
        i = 0
        while i < len(s):
            #print(self.state, end=" ")
            #print(self.state_transitions[self.state], end=" ")
            try:
                alph = ""
                Type = "other"
                if self.backup[self.state]:
                    i -= 1
                elif self.read[self.state]:
                    #print(s[i], end="")
                    if s[i] in string.digits:
                        Type = "number"
                    elif s[i] in string.ascii_letters or s[i] in "áéíóöőúüűÁÉÍÓÖŐÚÜŰ":
                        Type = "letter"
                    elif s[i] == "{":
                        Type = "{"
                    elif s[i] == "}":
                        Type = "}"
                    elif s[i] == "(":
                        Type = "("
                    elif s[i] == "*":
                        Type = "*"
                    elif s[i] == ")":
                        Type = ")"
                    elif s[i] == ":":
                        Type = ":"
                    elif s[i] == "=":
                        Type = "="
                    elif s[i] == "<":
                        Type = "<"
                    elif s[i] == ">":
                        Type = ">"
                    elif s[i] == " ":
                        Type = "space"
                    elif s[i] == "$":
                        Type = "$"
                    else:
                        Type = "other"
                    i += 1

                alph = self.findAlph(Type)   
                self.state = self.state_transitions[self.state][alph]
                if self.state == 0:
                    return False
            except ItemNotFound:
                return False
            #print()
        return self.isInAcceptingState()
