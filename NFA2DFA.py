
def rem(s):
        a = list(s)
        if('-' in a):
                a.remove('-')
        if(a):
                b = ''
                return(b.join(a))
        else:
                return('-')

def closure(transitions, states, symbols,start):
        start_state = start
        flag = 1
        t = ''
        while(flag):
                for i in start_state:
                        if(transitions[ord(i)-65][len(symbols)-1] == '-'):
                                flag = 0
                                break
                        else:
                                for j in transitions[ord(i)-65][len(symbols)-1] :
                                        t = t + str(transitions[ord(i)-65][len(symbols)-1])
                                        if(not transitions[ord(j)-65][len(symbols)-1] in t and not transitions[ord(j)-65][len(symbols)-1] == '-'):
                                                t = t + str(transitions[ord(j)-65][len(symbols)-1])
                                                flag = 1
                                        else:
                                                flag = 0
        return(sorted(set(t)))


def find_trans(transitions,states,symbols,close,s,sym):
        t = ''
        for i in s:
                if(not i == '-' ):
                        t = t + transitions[ord(i)-65][sym]
                        for j in t:
                                if not j == '-' :
                                        t = t + close[j]

        k = ''
        return(k.join(sorted(set(t))))
        

def conv(transitions, states, symbols, final):

        close = {}
        for i in states:
                t = ''
                close[i] = t.join(closure(transitions, states, symbols, i))
                
        start_state = states[0] + close[states[0]]

        print('\n')
        dfa_states = []
        dfa_transitions =  {}
        dfa_states.append(start_state)
        for i in dfa_states :
                for k in i:
                        dfa_transitions[i] = []
                        for j in range(len(symbols)-1):
                                dfa_transitions[i].append(find_trans(transitions,states,symbols,close,i,symbols[j]))
                                if(not find_trans(transitions,states,symbols,close,i,symbols[j]) in dfa_states):
                                        dfa_states.append(find_trans(transitions,states,symbols,close,i,symbols[j]))

        temp = {}
        for i in dfa_transitions:
                if(rem(i) not in temp):
                        temp[rem(i)] = []
                        for j in dfa_transitions[i]:
                                temp[rem(i)].append(rem(j))

        
        print("STATES OF DFA:", end="   ")
        for i in (temp):
                print(i,end=' ')
                
        print("\n")
        print("GIVEN SYMBOLS FOR DFA: ",end="   ")
        for i in range(0,len(symbols)-1):
                print(i, end=" ")
                
        print("\n")
        print("DFA TABLE\n")
        print("              ",end="")
        for i in range(len(symbols)-1):
                print(str(symbols[i]), end= "           ")
        for i in temp:
                if(not i == '-'):
                        print("\n")
                        print(i,end= " "*(12-len(i)))
                        for j in temp[i]: 
                                print(j, end= " "*(12-len(j)))
        
        print("\n")
        print("FINAL STATES IN THE DFA ARE\n")
        for i in temp:
                flag = 1
                for j in i:
                        if(j in final and flag):
                                print(i)
                                flag = 0
        



print("ENTER THE NUMBER OF STATES")
n = int(input())

print("ENTER THE NUMBER OF SYMBOLS")
sys = int(input())

states =[]
print("STATES OF NFA:", end="   ")
for i in range(0,n):
    print(chr(65+i),end=' ')
    states.append(chr(65+i))

print("\nGIVEN SYMBOLS FOR NFA: ",end="   ")
symbols = []
for i in range(0,sys):
    print(i, end=" ")
    symbols.append(i)
print("lambda")
symbols.append("lambda")

print("ENTER THE FINAL STATE")
final = input()
final = final.upper()

transitions = []
flag = 1
for i in states:
    transitions.append([])
    for j in symbols:
        print('('+ str(i) +',' + str(j) +') ->', end=' ')
        temp = input()
        temp = temp.upper()
        for k in temp:
            if(not (k in states or k=='-')):
                flag = 0 
        
        if(flag):
                transitions[ord(i)-65].append(temp)
        
        else:
            exit()

print("\nNFA TABLE\n")
print("         ",end="")
for i in symbols:
        print(str(i), end= "      ")
for i in states:
    print("\n")
    print(i,end='       ')
    for j in transitions[ord(i)-65]: 
        print(j, end= " "*(7-len(j)))


conv(transitions, states, symbols, final)

"""
a
b
c
-
d
-
c
-
d
f
e
-
dg
f
-
f
e
dg
f
e
-
"""