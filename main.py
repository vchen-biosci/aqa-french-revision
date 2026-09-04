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

negatives = """ne...jamais

never

ne…pas

not

ne...personne

nobody, no-one

ne...plus

no more, no longer

ne…que

only, nothing but

ne…rien

nothing

ni…ni

neither….nor

pas encore

not yet""".splitlines()

number_expressions = """une dizaine

about 10

une douzaine

dozen

nombre de

number of""".splitlines()

questions = """combien ?

how much, how many?

comment ?

how?

est-ce que ?

expression put before a verb to make sentence into a question

où ?

where?

pourquoi ?

why?

quand ?

when?

que ?

what?

quel/quelle ?

which?

qu’est-ce que ?

what?

qu’est-ce qui ?

what?

qu’est-ce que c’est ?

what is it?

qui ?

who?

quoi ?

what?""".splitlines()

common_questions = """à quelle heure ?

at what time?

ça s’écrit comment ?

how is that written?

c’est combien ?

how much is it?

c’est quelle date ?

what is the date?

c’est quel jour ?

what day is it?

de quelle couleur ?

what colour?

d’où ?

from where?

pour combien de temps ?

for how long?

que veut dire... ?

what does... mean?

quelle heure est-il ?

what time is it?""".splitlines()

greetings_and_exclamations = """à bientôt

see you soon

à demain

see you tomorrow

à tout à l’heure

see you soon/later

allô

hello (on phone)

amitiés

best wishes

au secours

help

bien sûr

of course, certainly

bienvenue

welcome

bon anniversaire

happy birthday

bon appétit

enjoy your meal

bon voyage

have a good trip

bonne année

happy new year

bonne chance

good luck

bonne idée

good idea

bonne nuit

good night

bonnes vacances

have a good holiday

bonsoir

good evening

d’accord

ok

de rien

don't mention it

désolé (e)

sorry

excusez-moi

excuse me

félicitations

congratulations

joyeux Noël

Merry Christmas

meilleurs voeux

best wishes

pardon

excuse me

quel dommage

what a pity

salut

hi

santé

cheers

s’il te/vous plaît

please""".splitlines()

opinions = """à mon avis

in my opinion

absolument

absolutely

affreux

awful

agréable

pleasant

amusant

funny

barbant

boring

bien entendu

of course

bien sûr

of course

ça dépend

that depends

ça m’énerve

it gets on my nerves

ça me fait rire

it makes me laugh

ça me plaît

I like it

ça m’est égal

it’s all the same to me

ça ne me dit rien

it means nothing to me/I don't fancy that/I don't feel like it

ça suffit

that’s enough

casse-pieds

annoying

certainement

certainly

cher

dear, expensive

chouette

great

comme ci comme ça

so-so

compliqué

complicated

content

happy

croire

to believe

désagréable

unpleasant

désirer

to want

détester

to hate

dire

to say

drôle

funny

embêtant

annoying

en général

in general

enchanté

delighted

ennuyeux

boring

espérer

to hope

étonné

astonished, amazed

facile

easy

faible

weak

formidable

great

franchement

frankly

généralement

generally

génial

great

grave

serious

habile

clever

intéressant

interesting

(s’)intéresser à

to be interested in

inutile

useless

incroyable

incredible

inquiet/inquiète

worried

marrant

funny

marre (en avoir)

(to be) fed up

mauvais

bad

merveilleux/merveilleuse

marvellous

mignon/mignonne

cute

moche

ugly

(moi) non plus

nor me neither, nor do I

nouveau

new

nul

rubbish

parfait

perfect

passionnant

exciting

peine la

the bother

penser

to think

peut-être

perhaps

pratique

practical

préférer

to prefer

promettre

to promise

ridicule

ridiculous

rigolo

funny

sage

well behaved

sembler

to seem

sensass

sensational

supporter

to put up with

utile

useful

vouloir

to wish, want

vraiment

really, truly""".splitlines()

seasons = """printemps le

spring

l'été (m)

summer

l'automne (m)

autumn

l'hiver (m)

winter""".splitlines()

time_expressions = """à la fois

at the same time

à l’avenir

in the future

à l’heure

on time

à temps partiel

part-time

an l' (m)

year

année l' (f)

year

après

after

après-demain

the day after tomorrow

après-midi

afternoon

aujourd’hui

today

auparavant

formerly, in the past

avant

before

avant-hier

the day before yesterday

bientôt

soon

d’abord

at first, firstly

d’habitude

usually

de bonne heure

early

début le

start

demain

tomorrow

dernier/dernière

last

de temps en temps

from time to time

déjà

already

de nouveau

again

en attendant

whilst waiting (for), meanwhile

en avance

in advance

en ce moment

at the moment

en retard

late

en train de (faire...)

(to be) doing

en même temps

at the same time

encore une fois

once more, again

enfin

at last, finally

environ

about, approximately

fin la

end

hier

yesterday

il y a

ago

jour le

day

journée la

day

lendemain le

the next day

longtemps

for a long time

maintenant

now

matin le

morning

mois le

month

normalement

normally

nuit la

night

parfois

sometimes

passé le

past

pendant

during

plus tard

later

presque

almost, nearly

prochain

next

quelquefois

sometimes

rarement

rarely

récemment

recently

semaine la

week

seulement

only

siècle le

century

soir le

evening

soudain

suddenly

souvent

often

suivant

following

sur le point de (être)

(to be) about to

tard

late

tôt

early

toujours

always, still

tous les jours

every day

tout à coup

suddenly, all of a sudden

tout de suite

immediately

vite

quickly""".splitlines()

location_and_distance = """à droite

on/to the right

à gauche

on/to the left

banlieue la

suburb

centre-ville le

town centre

campagne la

countryside

chez

at the house of

de chaque côté

from each side

de l’autre côté

from the other side

en bas

down(stairs)

en haut

up(stairs)

est l' (m)

east

ici

here

là

there

là-bas

over there

loin de

far from

nord le

north

nulle part

nowhere

ouest l' (m)

west

par

by

partout

everywhere

quelque part

somewhere

situé (e)

situated

sud le

south

tout droit

straight ahead

tout près

very near

toutes directions

all directions

ville la

town""".splitlines()

colours = """châtain

light brown

clair

light

foncé

dark

marron

brown

noisette

hazel

pourpre

purple

rose

pink

roux

ginger""".splitlines()

weights_and_measures = """assez

enough, quite

bas

low

boîte la

box, tin, can

bouteille la

bottle

court

short

demi le

half

encore de

more

étroit

narrow

gros

fat

haut

high

large

wide

maigre

skinny, thin

mince

slim, thin

moitié la

half

morceau le

piece

moyen/moyenne

medium, average

nombre le

number

paquet le

packet

pas mal de

lots of

peser

to weigh

plein de

full of, lots of

pointure la

size (for shoes)

suffisamment

sufficiently

taille la

size (for clothes)

tranche la

slice

trop

too (much)""".splitlines()

lists = [comparisons, conjunctions_connectives, prepositions, negatives, number_expressions
         , questions, common_questions, greetings_and_exclamations, opinions, seasons, 
         time_expressions, location_and_distance, colours]

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
