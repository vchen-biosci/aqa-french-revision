flashcards_list = {}

comparisons = """plus/moins

more/less

plus que/moins que

more than/less than

bon/meilleur/le meilleur

good/better/best

mauvais/pire/le pire

bad/worse/worst

bien/mieux/le mieux

well/better/best

mal/plus mal/le plus mal

badly/worse/worst

beaucoup/plus/le plus

lots/more/the most

peu/moins/le moins

few, little/less/the least""".splitlines()

conjunctions_connectives = """à cause de

because of

à part

apart from

ainsi

so, therefore

alors

so, therefore, then

aussi

also

car

because

cependant

however

c’est-à-dire

that is to say, i.e.

comme

as, like

d’un côté/de l’autre côté

on the one hand/on the other hand

donc

so, therefore

ensuite

next

évidemment

obviously

mais

but

même si

even if

ou

or

par contre

on the other hand

par exemple

for example

pendant que

while

pourtant

however

puis

then

puisque

seeing that, since

quand

when

sans doute

undoubtedly, without doubt, probably

si

if

y compris

including""".splitlines()

prepositions = """à

to, at

à côté de

next to

à travers

across, through

au bord de

at the side/edge of

au bout de

at the end of (ie length, rather than time)

au-dessous de

beneath, below

au-dessus de

above,over

au fond de

at the back of, at the bottom of

au lieu de

instead of

au milieu de

in the middle of

autour de

around

contre

against

de

of, from

depuis

since, for

derrière

behind

devant

in front of

en

in, within (time)

en dehors de

outside (of)

en face de

opposite

entre

between

jusqu’à

up to, until

malgré

despite, in spite of

parmi

amongst

pour

for, in order to

près de

near

sans

without

selon

according to

sous

under

sur

on

vers

towards""".splitlines()



lists = [comparisons, conjunctions_connectives, ]

for list in lists:
    new_list = []
    for vocab in list:
        if vocab:
            new_list.append(vocab)
            
    flashcard_set = {}
    i = 1
    for item in new_list:
        i += 1
        i = i % 2
        if i == 0:
            key = item
        else:
            flashcard_set[key] = item
            
    flashcards_list[input("What would you like to name this flashcard set?")](flashcard_set)
