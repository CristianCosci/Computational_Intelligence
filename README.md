# **Computational Intelligence**

## **Indice**
- [Informazioni sul corso](#informazioni-sul-corso)
- [Introduzione](#introduzione)
- [Problemi di ottimizzazione](#problemi-di-ottimizzazione)
    - [Categorie dei problemi di ottimizzazione](#categorie-dei-problemi-di-ottimizzazione)
- [Local search](#local-search)
    - [Number Partitioning Problem NPP](#number-partitioning-problem-npp)
        - [Fenotipo e Genotipo](#fenotipo-e-genotipo)
    - [Minimo Ottimo Locale](#minimo-ottimo-locale)
    - [Local Search Algorithm](#local-search-algorithm)
    - [Attrazione del bacino su un minimo locale](#attrazione-del-bacino-su-un-minimo-locale)
    - [Iterated Local Search](#iterated-local-search-ils)
    - [Implementazione degli algoritmi Local Search](#implementazione-degli-algoritmi-local-search)
        - [Best improvement Local Search](#best-improvement-local-search)
        - [First improvement Local Search](#first-improvement-local-search)
        - [Iterated Local Search](#iterated-local-search)
- [Simulated annealing](#simulated-annealing)
    - [Principali caratteristiche](#principali-caratteristiche-di-sa)
    - [Implementazione algoritmo Simulated Annealing](#implementazione-algoritmo-simulated-annealing)
- [Applicazioni di algoritmi al problema del commesso viaggiatore (TSP)](#applicazioni-di-algoritmi-al-problema-del-commesso-viaggiatore-tsp)
- [Algoritmi Genetici](#algoritmi-genetici)
    - [Introduzione e Caratteristiche](#caratteristiche)
    - [Pseudocodice di GA](#pseudocodice-di-ga)
    - [Mating Pool](#mating-pool)
        - [Roulette Wheel](#roulette-wheel-ruota-della-fortuna)
        - [Tornei](#selezione-baata-su-tornei)
    - [Crossover](#1-crossover)
    - [Mutazione](#2-mutazione)
    - [Selezionare la nuova popolazione](#selezionare-la-nuova-popolazione)
    - [Criteri di Terminazione](#criteri-di-terminazione)
    - [Implementazione di un GA](#implementazione-di-un-ga)
    - [Implementazione GA per il problema MAX-CUT](#implementazione-di-un-algoritmo-genetico-per-il-problema-max-cut)
    - [Implementazione GA per il problema TSP](#implementazione-di-un-algoritmo-genetico-per-il-problema-tsp)
    - [Influenza dei parametri negli algoritmi](#parametri-su-cui-si-può-agire-in-un-ga-e-la-loro-influenza)
- [Problemi Vincolati](#problemi-vincolati)
    - [Algoritmi genetici per problemi vincolati](#algoritmi-genetici-per-problemi-vincolati)
    - [Penalizzazione e Riparazione](#riparazione-e-penalizzazione)
        - [Confronto](#confronto-tra-i-due-metodi-penalizzazione-e-riparazione)
- [Algoritmi evolutivi per l'ottimizzazione continua](#algoritmi-evolutivi-per-lottimizzazione-continua)
    - [Strategie evolutive](#strategie-evolutive)
        - [(1+1)-ES](#11-es)
        - [(λ, μ)-ES](#λ-μ-es)
        - [(λ + μ)-ES](#λ--μ-es)
        - [CMA-ES](#cma-es)

### Informazioni sul corso
- **Esame** (2 parti):
    - **Progetto**
        - Implementazione di qualche algoritmo (linguaggio di programmazione a scelta):
            - algoritmi evolutivi
            - sistema fuzzy
            - sistema probabilistico
            - libreria per velocizzare alcune cose e quindi applicarlo ad un problema effettivo
        - Analisi di un articolo di ricerca (solo per studenti che hanno un interesse scientifico (tesi, dottorato ecc...))
    - **Orale**:
        - domande sul programma
        - presentazione progetto

- **Materiale**:
    - libri di testo (qualche capitolo indicato dal prof)

<hr>

# **Introduzione**

### **Che cos'è la computational intelligence?**
È una parte dell'Intelligenza Artificiale che comprende alcuni strumenti che si utilizzano in essa. Argomenti principali:
1. **Reti neurali** (*già trattato nel corso di Machine Learning e quindi non lo trattiamo*)
    - Sono lo strumento più famoso ma non l'unico che può essere utilizzato nelle applicazioni di intelligenza artificiale.
2. **Algoritmi evolutivi**
    - Ne fanno parte le **Metaeuristiche**.
    - Sono uno strumento utilizzato per risolvere i **problemi di ottimizzazione** particolarmente difficili. <br>
    Esempi di problemi di ottimizzazione:
        - Il training delle reti neurali;
        - Clustering;
        - Costruzione degli alberi decisionali ecc...
        - Uno dei problemi di ottimizzazione più famosi è il "*Problema del commesso viaggiatore*".
3. **Logica Fuzzy**
    - È uno strumento che serve per rappresentare **concetti vaghi**.
        - Esempio di concetto vago: *La temperatura è alta* (non ti dico esattamente una soglia secondo cui la temperatura inizia ad essere alta o meno). Esiste un confine sfumato tra *alto* e *non alto*.
4. **Modelli probabilistici**
    - Usati per rappresentare l'**incertezza**.
        - Esempio: La probabilità che il paziente abbia una determinata malattia è 0.25 , come posso usare questa informazione all'interno di un sistema di AI? I modelli probabilistici consentono di trattare questo tipo di informazioni (probabilistiche).

Gli ultimi 3 argomenti completano il bagaglio degli strumenti che possono essere utilizzati nell'AI. 

Esistono 2 livelli nelle Intelligenze Artificiali (e da questo anche 2 modi per approcciare l'AI):
- **Livello simbolico** (*Intelligenza Artificiale classica*)
    - Logica proposizionale/booleana (algoritmi di ricerca come: BFS, DFS, A*, planning ecc...)
        - **Opera ad alto livello**: l'informazione è codificata in modo simbolico (rappresentazione simbolica).
- **Livello subsimbolico** (*Intelligenza Artificiale "moderna"*)
    - Ad esempio il riconoscimento delle immagini funziona meglio a livello subsimbolico (lavoro sui pixel e non sulle forme geometriche individuabili nelle immagini, come viene invece fatto a livello simbolico).
    - Rappresentazione numrica invece della rapresentazione logica/discreta (esempio nel riconoscimento delle immagini sopra).

<hr>

# **Problemi di ottimizzazione**
Molti problemi di ottimizzazione sono computazionalmente difficili (Es: np-hard o peggio).<br>
*Breve cenno sul significato di **NP***: La classe di problemi ***NP*** comprende tutti quei problemi decisionali che, per trovare una soluzione su una macchina di Turing non deterministica, impiegano un tempo polinomiale. La classe NP prende il suo nome dall'abbreviazione di *Nondeterministic Polynomial Time*.

### **Problema del commesso viaggiatore *TSP***
- *n* città <br>
![grafo](./imgs/tsp1.png)

- Il grafo è solitamente completo (da ogni città posso andare ad ogni altra città) e può essere sia orientato che non orientato.
- Ho una matrice che rappresenta le distanze/costi:
    - d(i,j) è la distanza tra la città *i* e la città *j* (o il costo per andare da *i* a *j*)
    - Se il grafo è completo ogni entrata ha un numero reale
    - Se non c'è collegamento tra *i* e *j* si può mettere che d(i,j) = *infinito*

Il problema TSP può essere:
- **simmetrico**: d(i,j) = d(j,i) $\forall$ (per ogni) *i*,*j* 
- **asimmetrico**: d(i,j) != d(j,i) $\exists$ (esistono) *i* e *j* per cui si verifica ciò (Esempio: città in salita e discesa).
    - **euclideo**: d(i,j) = distanza(posizione città *i*, posizione città *j*) -> distanza euclidea (non realistica, realistica solo se la terra fosse piatta).

#### Il TSP è *NP*-hard se visto come problema di ottimizzazione, oppure è *NP*-completo come problema decisionale.

***Definizione***. Un problema di ottimizzazione è definito da:
- uno spazio di ricerca X
- una funzione obiettivo f: X -> R (non necessariamente sarà sempre R)

Lo scopo è trovare il valore x* appartenente a X tale che f(x*) sia minimo (o massimo)

Nel problema del commesso viaggiatore:
- X è l'insieme di tutti i cicli Hamiltoniani del grafo
    - un ciclo Hamiltoniano è una sequenza di città che inizia da una città prestabilita *c0*, passa per tutte le città una sola volta e termina in *c0*. <br>
    Es: 1->3->4->2->6->5->1 (nel grafo di prima)
- La funzione obiettivo f è la distanza totale (o il costo) del ciclo Hamiltoniano. <br>
    f(1->3->4->2->6->5->1) = d(1,3) + ... + d(5,1)
    <br>
    - x* è il ciclo Hamiltoniano con la minima distanza totale. <br>
    Ciò lo rende un problema *NP*-hard.

*Note*:
- Trovare un ciclo Hamiltoniano è semplice se il grafo è completo.
- Computare f è facile (Calcolare f).
- La difficoltà sta nel trovare x*

X è l'insieme di tutte le permutazioni delle città (dei nodi del grafo) (con la prima città che deve essere rimessa anche in fondo). 

In alcuni problemi anche generare un elemento di X può essere difficile (elemento di X = soluzione ammissibile).

## **Categorie dei problemi di ottimizzazione**:
- **Discreti** (Es: TSP)
    - Un problema di ottimizzazione è discreto quando X è un insieme finito.
    - In un problema discreto ogni X(*i*) ha un dominio finito.
        - *Es:* Se il grafo ha n città, ci sono (n-1)! cicli hamiltoniani.
- **Continui**
    - X è un insieme infinito (Es: R o un intervallo)
        - Lo spazio di ricerca è costituito da numeri reali, vettori di numeri reali, matrici di numeri reali ecc...
        - *Es*: determinare la posizione di *n* punti in modo tale da minimizzare la somma complessiva delle distanze da un determinato punto fissato. 
    - In un problema continuo ogni X(*i*) ha un dominio infinito.
        - *ES*: ho una città e devo mettere delle stazioni di ricarica. Le devo mettere in modo tale che sia minima la somma complessiva delle distanze delle varie città in modo tale che un veicolo non deve fare troppa strata per potersi ricaricare.

Si distingue anche tra problemi di ottimizzazione con:
- **funzioni obiettivo lineari**
    - f(x*i*, ... , x*n*) = w*1*x*1*+....+w*n*x*n*
    - *Es*: funzione problema dello zaino.
- **funzioni obiettivo non lineari**
    - f non è una combinazione lineare x*1*, ... , x*n*

Si hanno inoltre:
- **problemi vincolati**:
    - X è ottenuto aggiungendo vincoli allo spazio di ricerca originale.
        - Es: lo zaino è un problema vincolato. Senza vincoli lo zaino è senza limiti e si prenderbbero tutti gli oggetti, ottenendo il massimo valore. Il problema dello zaino classico è quello vincolato (ogni oggetto ha un valore e un peso e lo zaino ha un limite)
    - X è quindi ristretto.

I problemi di ottimizzazione possono anche avere:
- **una singola funzione obiettivo**
- **più funzioni obiettivo**
    - *Es*: TSP con tempo e carburante come funzioni obiettivo (che in questo caso sono addirittura in competizione).

### Quali sono le possibili soluzioni algoritmiche per un problema di ottimizzazione combinatoria come TSP?
1. **Algoritmi esatti**: 
    - Risolvono in maniera esatta il problema. Non sono comunque in grado di risolvere istanze medio-grandi.
    - All'aumentare dell'istanza anche di poco, i tempi di calcolo crescono esponenzialmente. Perche gli algoritmi sono solitamente esponenziali, al massimo polinomiali.
    - È possibile anche usare alcuni "*universal solver*". Ad esempio un SAT solver o MIP solver. Significa formulare il problema di ottimizzazione come un SAT o un *mixed integer probgramming*.
2. **Algoritmi Approssimati**: 
    - Sono algoritmi studiati ad Hoc per il problema che trovano soluzioni sub-ottimali in tempo polinomiale. La soluzione trovata non è peggio di una certa quantità rispetto all’ottimo. Usano delle euristiche pensate appositamente per il problema.
    - **Approssimare il problema di ottimizzazione**: utilizzare un algoritmo approssimato.
        - Anziche trovare x* tale che f(x*) sia massimo o minimo, questi algoritmi trovano un x' tale che f(x') <= *k* * f(x*)
            - *Es*: f(x*) = 300 <br>
            x' ---> f(x') <= 2*300 <br>
        Ovviamente minore è *k* e meglio è.
        - x' non è un minimo, è qualcosa che gli si avvicina ma quanto è lontano?
        - Per ottenere bassi valori di *k* è richiesto maggiore tempo.
        - Ci sono dei problemi di ottimizzazione in cui *k* non può essere scelto però. Non possono essere approssimati meglio di quel *k*.
3. **Metaeuristiche**:
    - Trovano soluzioni sub-ottimali in tempo polinomiale. Non danno la garanzia di un limite per la soluzione, ma il vantaggio è che lo schema si può applicare con opportuni cambiamenti a molti problemi di natura diversa. Questi metodi fanno poche o nessuna ipotesi sul problema da ottimizzare e possono cercare spazi molto ampi di soluzioni candidate.
    - Una **metaeuristica** è un algoritmo che da una soluzione del problema, la quale non è necessariamente ottima ma potrebbe essere molto buona, ottenuta soprattuto in un tempo ragionevole. Non c'è nessuna garanzia su quanto è buona la soluzione e non riesco a stimarlo. Questo è il prezzo da pagare per utilizzare una metaeuristica.
    - Metaeuristica significa che la stessa `tecnica` può essere usata (adattandola) a un'ampia gamma di problemi di ottimizzazione.
        - *Es*: algoritmi genetici (risolvono problemi come lo zaino, il TSP, problemi di scheduling, problemi di ottimizzazione discreti, continui ecc...).
    - `Tecnica`: È uno schema per un possibile algoritmo (ci sono dei buchi da riempire che dipendono dal problema e altri possono essere scelti dal programmatore).
    - Molte metaeuristiche usano i numeri casuali (pseudo casuali). Significa che sono algoritmi randomizzati. 
        - Più esecuzioni possono tornare soluzioni diverse:
            - si prende la migliore oppure la media delle soluzioni

<hr>

## **Local search**
- Si utilizza in problemi di ottimizzazione discreta.

Le soluzioni nello spazio di ricerca sono connesse e formano un grafo orientato. <br>
![ls0](./imgs/ls0.png) <br>
- *S* e *S'* sono soluzioni
- Si dice che *S'* è un vicino di *S*
- *S''* è un vicino di *S'*
- *S'''* non è vicino di *S*

*S'* è un **vicino** di *S* se:
1. C'è un arco che va da *S* a *S'*
2. *S'* può essere ottenuto da *S* usando una **trasformazione elementare**

*Primo esempio*:
### **Number partitioning problem (NPP)**:
#### *Rappresentazione con sottoinsiemi*
- dati *n* numeri interi x*1*, ... , x*n* <br>
Dividere i numeri in due sottoinsiemi disgiunti S*1* e S*2* <br>

S1 e S2 devono soddisfare la seguente condizione: <br>
![sum](./imgs/sum1.png) <br>
è **minima**.

*Per esempio*: <br>
x*i* = {14, 20, 13, 8, 21, 10, 9, 4} <br>
S*1* = {14, 20, 8 , 10} -> somma = 52 <br>
S*2* = {21, 13, 9, 4} -> somma = 47 <br>
F(s1, S2) = |52-47| = 5 <br>

S*1* = {14, 20, 4 , 10} -> somma = 48 <br>
S*2* = {21, 13, 9, 8} -> somma = 51 <br>
F(s1, S2) = |48-51| = 3 *questa soluzione è migliore di quella precedente* <br>

**Una soluzione di NPP è una coppia di sottoinsiemi S1 e S2.**

#### *Rappresentazione con vettore di n-bit*
Ma una differente rappresentazione può essere basata su un **vettore di n-bit b**.

{14, 20, 8, 10} {13, 21, 9, 4} -> [00101011] <br>
b*i* = 0 -> x1 ∈  S*1* <br>
b*i* = 1 -> xi ∈  S*2*

### **Fenotipo e Genotipo**
- La rappresentazione binaria è chiamata **genotipo** ed è una rappresentazione interna (può essere ad esempio utilizzata da un algoritmo in modo efficace)
- La rappresentazione sui sottoinsieme è chiamata **fenotipo** ed è una rappresentazione esterna.

La differenza sta che l'utente è interessato al fenotipo e invece l'algoritmo può utilizzare il genotipo perchè potrebbe funzionare meglio.

Il passaggio(mapping) da genotipo a fenotipo e viceversa deve essere computazionalmente veloce e facile, ma potrebbe non essere necessariamente 1:1 (ad un genotipo corrisponde ad un fenotipo, l'importante è che ogni genotipo abbia un fenotipo diverso. Potrebbero esserci due genotipi che corrispondono ad un fenotipo).

Un algoritmo può decidere di usare una rappresentazione ridondante dove differenti genotipi corrispondono allo stesso fenotipo.

*Ritornando all'esempio di prima*: <br>
Fenotipo S1, S2 <br>
Genotipo b

Tra i vettori di n-bit c'è l'operazione elementare chiamata **bit-flip**.

Dato un vettore n-bit e un indici i<= k <= n, negare il k-esimo bit <br>
b = [0010**1**100] <br>
k = 5 <br>
b -> [0010**0**100] <br>

[00101100] si può trasformare in tanti modi applicando il bit-flip a tutti i possibili bit. *Esempi*:

1. [10101100]
2. [01101100]
3. [00001100]

I possibili vicini di questa soluzione sono 8 e ognuno si ottiene facendo il flip di un bit. <br>
Lo spazio di ricerca del NPP con la rappresentazione binaria è composto da 2^n vettori di n-bit , ciascuno dei quali è collegato a n vicini ottenuti tramite un bit-flip.

Questo spazio di ricerca si chiama **ipercubo**:
- per n=2 è un quadrato
- per n=3 è un cubo
- n = 4 non è facilmente disegnabile
- ecc...

**La funzione obiettivo  f(S*1*,S*2*) può essere riscritta come f(b)** <br>
![fb](./imgs/fb.png)

Partendo da una soluzione **b**, alcuni vicini (*b*') potrebbero essere migliori e altri (*b*'') potrebbero essere peggiori. Altri vicini possono essere buoni quanto b. Il paragone dei vicini si fa con le funzioni obiettivo. <br>
![fb1](./imgs/fb1.png)

<hr>
 
### **Minimo ottimo locale**
*In NPP è il minimo locale*.

- **L'ottimo locale** è una soluzione x | nessun vicino è meglio di x, ∀ y | y è vicino di x , f(y) >= f(x).
- x è un **minimo locale stretto** se ∀ y | y è vicino di x, f(y) < f(x).

*NOTAZIONE*: **N(x) = {vicini di x}**

Minimo:
- **locale** -> confronto con i vicini.
- **globale** -> confronto il punto con tutti
    - Un **minimo globale** per una funzione f è una soluzione x | f(x) <= f(y) ∀ y ∈ X
    - Un **minimo globale stretto** f(x) < f(y) ∀ y ∈ X

`Il problema di ottimizzazione è risolto se trovo il minimo globale. Altrimenti ho trovato una soluzone sub-ottimale.`

Un semplice algoritmo che trova un minimo locale si chiama **Local Search**.

### **Local search algorithm**
```pseudocode
function_LS(f,X)
    x: scelto randomicamente (o con qualhe criterio) (soluzione)
    found = false
    do 
        y:= migliore dei vicini di x (prendo x trovo i vicini, calcolo f e prendo quella con valore più basso)
        if f(y) >= f(x) then 
            found:= True
        else 
            x:= y
    while not found
return x
```
*Come scegliere il miglior vicino?*
```pseudocode
    y:= primo elemento di N(X)
    fy:= f(y)
    for z in N(X)
        fz:= f(z)
        if fz < fy then
            y:= z
            fy:= fz
        end if
    end for
return y
```
- È facile provare che **LS** **restituisce sempre il minimo locale**. C'è qualche probabilità di ottenere il minimo globale anche se solitamente la soluzione restituita ottenuta non è il minimo globale.

### **Attrazione del bacino su un minimo locale**
L'attrazione del bacino su un minimo local x* è l'insieme delle soluzioni x tali che se LS parte da x produce x*. <br>
![bacino](./imgs/bacino.png) <br>

- L'algoritmo di ricerca locale appena visto è chiamato **best improvement local search**.

Un'altra possibilità è di scegliere (se c'è) un vicino di x che è migliore di x (non il migliore) -> **first improvement local search**

```pseudocode
Function_LS_fi(X,f)
    x:= initial solution (Random)
    fx:= f(x)
    found = false
    do 
        y, fy := un vicino migliore di x (esplora N(X) con un ordine casuale)
        if y = Φ (vuoto) then
            found:= true
        else 
            x:= y
            fx:= fy
    while not found
return x
```

## **Iterated local search (ILS)**
![ils1](./imgs/ils1.png)

*Elementi dell'algoritmo*:
- LS con scelta iniziale della soluzione
- **nt** = numero di tentativi del secondo tipo (tentativi infruttuosi)

```pseudocode
Function_ILS(f,X, nt)
    x0:= sluzione iniziale
    x, fx := LS(f, X, x0)
    k = 0
    while k <= nt
        y:= perturbation(x)
        z, fz := LS(f,X, y)
        if fz < fx then
            x:= z
            fx:= fz
            k:= 0
        else
            k:= k+1
        end if
    end while
return x
```

- La **perturbazione** è una piccola modifica.
    - Deve essere piccola perchè se lo stravolgo mi sposto troppo ed è come se ricominciassi da zero.
- **h** rappresenta la forza della perturbazione
    - *Per esempio in NPP h è il numero dei bit-flip applicati a x*.

`I concetti di local minimum e global minimum e gli algoritmi LS e ILS funzionano per ogni problema di ottimizzazione discreta data la struttura di vicinato.`

*Per esempio nel TSP i vicinati* <br>
![ils2](./imgs/ils2.png) <br>
in rosso gli archi che non c'erano.

<hr>

## **Implementazione degli algoritmi Local Search**
Innanzitutto è necessario definire la classe `Problem` per definire la struttura di base del problema, la sua inizializzazione e le funzioni di comodo.
### **Best improvement Local Search**
```python
# number partition problem
import numpy as np

class Problem:
    def __init__(self, num):
        self.dim = num
        self.numbers = np.random.randint(1, 100000, num)    # Creazione istanza

    def objective_function(self, sol):
        # La soluzione è un vettore di 0 e di 1
        '''
        - 0 rappresenta che stanno nel primo sottoinsieme
        - 1 rappresenta che stanno nel secondo sottoinsieme
        '''
        s = 0
        for i in range(self.dim):
            if sol[i] == 0:
                s += self.numbers[i]
            else:
                s -= self.numbers[i]
            
        return abs(s)
    
    def objective_function(self, sol):  # Molto più efficiente
        s = sum((1-2*sol)*self.number)
        
        return np.abs(s)

    def get_dim(self):
        return self.dim
```
Si può ora procedere all'implementazione dell'algoritmo di ricerca `Local Search`
```python
import numpy as np
from NPP import *

# local search algorithm for a binary problem
# BEST IMPROVEMENT
def local_search(prob, init_sol=None):
    n = prob.get_dim()
    if init_sol is None:
        x = np.random.randint(0, 1+1, n)
    else:
        x = init_sol.copy()
    
    improved = True
    fx = prob.objective_function(x)
    print("Initial value {}".format(fx))
    while improved:
        best_f = 1e300  # Numero grande per i confronti seguenti
        for i in range(0, n):
            x[i] = 1-x[i] # Bit-flip -> questa logica può essere migliorata e resa più efficiente in quanto ci mette O(n^2) operazioni
            fy = prob.objective_function(x)
            if fy < best_f:
                y = x.copy()
                best_f = fy
            x[i] = 1-x[i] 
        if best_f < fx:
            fx = best_f
            x = y
            improved = True
            print("New value {}".format(fx))
        else:
            improved = False
    return x, fx 
```
- Il **bit-flip** può essere chiamato Δf(x, i) = f(x con i-esimo bit complementare) - f(x) <br>
Nel problema NPP è anche semplice trovare il miglior vicino di x, in O(n) anzichè O(n^2). <br>
A sua volta se riduco il tempo di ricerca della Local Search lo riduco anche delle versione iterata in quanto usa essa stessa.




Per testare l'algoritmo e vedere le varie info si consigliano i seguenti comandi (disponibili nel file ***test.py*** nella directory apposita).
```python
from local_search import *

np.random.seed(42) # Fisso il seed per la riproducibilità degli esperimenti

p = Problem(100) # Creo istanza problema di lunghezza 100

print(p.numbers) # Stampo i vari numeri che popolano il vettore popolato randomicamente
print(p.get_dim())

x, fx = local_search(p) # Eseguo la Local Search
print(x, fx)

x, fx = local_search(p,x) # Se la rieseguo partendo dalla soluzione di prima si vede che ritorna sempre lo stesso valore e quindi non migliora

risultati = [local_search(p) for run in range(100)] # Eseguo Local Search 100 volte
print(risultati)

# Analisi sui valori dei risultati ottenuti
ff = [coppia[1] for coppia in risultati]

min = np.min(ff)
# Altri tipi di analisi
'''
np.mean(ff)
np.max(ff)
np.min(ff)
np.median(ff)
'''
```
### **First Improvement Local Search**
Si passa ora all'implementazione della ***Local Search*** nella sua versione **First improvement**.
```python
import numpy as np
from NPP import *

# local search algorithm for a binary problem
# FIRST IMPROVEMENT
def local_search(prob, init_sol=None, verbose= False):
    n = prob.get_dim()
    if init_sol is None:
        x = np.random.randint(0, 1+1, n)
    else:
        x = init_sol.copy()
    
    improved = True
    fx = prob.objective_function(x)
    if verbose:
        print('Initial value {}'.format(fx))
    while improved:
        best_f = fx
        ordering = list(range(0,n))
        np.random.shuffle(ordering)
        for i in ordering:
            x[i] = 1-x[i]
            fy = prob.objective_function(x)
            if fy < best_f:
                y = x.copy()
                best_f = fy
                x[i] = 1-x[i]
                break
        
            x[i] = 1-x[i]
        if best_f < fx:
            fx = best_f
            x = y
            improved = True
            if verbose:
                print("New value {}".format(fx))
        else:
            improved = False
    return x, fx 
```
Questa versione è molto più veloce di quella precedente.
### **Iterated Local Search**
```python
from local_search_fi import *
from NPP import *

def iterated_local_search(prob, num_tries, num_flips, init_sol= None):
    n = prob.get_dim()
    if init_sol is None:
        x = np.random.randint(0, 1+1, n)
    else:
        x = init_sol.copy()
    nt = 0
    fx = prob.objective_function(x)
    while nt < num_tries:
        y =perturbation(x, num_flips)
        z, fz = local_search(prob, y)
        if fz < fx:
            x = z
            fx = fz
            nt = 0
        else:
            nt+=1
    return x, fx

def perturbation(x, num_flips):
    n = len(x)
    y = x.copy()
    for flip in range(num_flips):
        i = np.random.randint(0, n)
        y[i] = 1 - y[i]
    
    return y
```
Quest'ultima può essere in realtà implementata utilizzando entrambe le tipologie di `Local Search` (best improvemente e first improvement), con la quale si noteranno differenti prestazioni in termini di tempo e probabilmente anche della soluzione trovata.

Per quanto riguarda il codice sorgente completo, eventuali comandi di test e altro vedere i relativi file nell'apposita directory per la ***Local Search***.

<hr>

## **Simulated annealing**
- Nella *ricerca locale* (anche nella sua versione *iterata*), si passa da un elemento ***x*** a un elemento **migliore**.
    - **Nella ricerca locale** il passaggio avviene in maniera *diretta* perchè si prende un vicino di x e lo si cerca di migliorare passando per uno dei vicini di quest'ultimo. 
    - Nella ricerca locale devo quindi migliorare ad ogni passaggio. **Quando non è più possibile, l'algoritmo termina**.
- **Nella ricerca locale iterata**, il procedimento è diverso, ma ad ogni passaggio si deve comunque migliorare. <br>
Si parte da un punto ***x0***, si applica la ricerca locale e si arriva in ***x1*** (minimo locale). Si applica una perturbazione a quest'ultimo (che potrebbe anche peggiorare la situazione ma non importa) e si riapplica la ricerca locale arrivando in ***z***. Se z è migliore la ricerca procede da questo punto, se invece ho peggiorato non si accetta (perchè si deve comunque sempre migliorare). <br>
Dopo un tot di tentavi infruttuosi la ricerca termina (oppure si possono scegliere altre condizioni di terminazione. Es. quante volte ho valutato f).

Nel **Simulated annealing** invece, si può anche peggiorare (ma di poco) e soprattutto all'inizio. <br>
Si intende che **le soluzioni** possono anche peggiorare.

```pseudocode
x:= initial solution                        # può essere preso random
fx:= f(x)
t:= initial temperature
for i:= 1 to num_iterations
    y:= selecet a random neighbor of x
    fy:= f(y)
    df=fy-fx                                # differenza in f
    p:= exp(-df/t)                          # se df è negativo, p è maggiore di 1
    if random(0,1) < p then                 # Se fy<fx, y è accettato come nuovo valore di x
        x:= y
        fx:= fy
    end if
    t:= t * delta_t                         # delta_t = 0.95
end for

return x, fx
```
***Cosa accade?*** <br>
Quando f(y) >= f(X), y è accettato con una probabilità ***exp(-df/t)***. <br>
Più è basso df e maggiore è la probabilità di accettazione. Se la differenza fosse 0 o negativa, lo accetterebbe sempre. <br>
Maggiore è t, maggiore è la probabilità di accettazione. <br>
- I peggioramenti non gravi sono quindi accettati meglio dei peggioramenti gravi.
- I peggioramenti sono accettati soprattutto quando la temperatura è alta.

È altresì importante che la temperatura diminuisce mano a mano.

All'inizio quindi la tendenza ad accettare peggioramenti è alta e poi scende. Verso la fine il **simulated annealing (SA)** accetta solo miglioramenti (perchè la probabilità di accettazione è così bassa che è come se fosse 0).

**Questo algoritmo è molto più casuale** (randomico) della ricerca locale e della ricerca locale iterata (vedere quanti eventi random ci sono nello pseudocodice).

### **Principali caratteristiche di SA:**
1. È molto più randomico di LS e ILS
2. C'è un bilanciamento tra **exploration** e **exploitation**. <br>
**Exploration**: guardare intorno a x (esplorare lo spazio di ricerca), senza prendere troppo in considerazione la funzione obiettivo f. <br>
**Exploitation**: cerca necessariamente il vicino migliore. <br>
All'inizio prevale l'exploration e mano a mano che la temperatura scende, la componente di exploitation prevale.
3. SA può essere usato anche per l'ottimizzazione continua, facendo una piccola modifica (Vedi sotto). <br>
**Ottimizzazione continua**: x non è un vettore o una permutazione di numeri (0 e 1), ma è fatto di numeri reali (il concetto di vicini non ha senso nei numeri reali). <br>
```pseudocode 
y:= x+delta_x 
```
dove delta_x è un vettore di numeri casuali piccoli nell'intervallo *[-epsilon, +epsilon]*. <br> Ciò indica "muoviti da x di un passettino".

**Uno dei problemi principali di SA è come gestire la temperatura**:
- trovare il valore iniziale per t_init
- trovare come aggiornare t

<hr>

## **Implementazione algoritmo Simulated Annealing**
L'implementazione seguente tratta l'algorimto **SA** sul problema **NPP**, quindi è necessario fare riferimento al file ***NPP.py***.
```python
import numpy as np
from NPP import *

# simulated annealing per il problema binario
def simulated_annealing(prob, num_iter, init_sol=None):
    n = prob.get_dim()
    if init_sol is None:
        x = np.random.randint(0, 1+1, n)
    else:
        x = init_sol.copy()
    fx = prob.objective_function(x)
    temp = 0.1 * fx / (-np.log(0.5))
    for i in range(num_iter):
        j = np.random.randint(0, n)
        y = x.copy()
        y[j] = 1 - y[j]
        fy = prob.objective_function(y)
        df = fy - fx
        pr = np.exp(-df / temp)
        if np.random.random() < pr:     # if fy < fx or np.random.random() < pr
            x = y
            fx = fy
        temp = temp*0.95
    
    return x, fx
```
Il codice per fare eventuali test è il seguente:
```python
from NPP import *
from simulated_annealing import *

np.random.seed(1918)

instance = Problem(100)
x, fx = simulated_annealing(instance, 10000)
print(x, fx)
```
Nel caso in cui si abbia overflow nel decadimento di temp cambiare il tasso di decadimento (qui è 0.95).

<hr>

## **Applicazioni di algoritmi al problema del commesso viaggiatore (TSP)**
**TSP** = *problema del commesso viaggiatore*. <br>
In questo problema, una soluzione è una lista di vertici tale che:
1. inizia e finisce con lo stesso vertice
2. non ha vertici duplicati (tranne il primo e l'ultimo)
3. ha lunghezza **n+1**

Nel TSP ci sono vari concetti si vicini (possibili implementazioni):
- **SWAPE/EXCHANGE** <br>
*x* = `[0 2 3 5 4 1 0]` ---> *x'* (**vicino**) = `[0 2 1 5 4 3 0]` <br> 
Ci sono **O(n^2)** vicini.
- **2-OPT** <br>
**Tecnica 2-OPT** : prendo due archi che non devono essere vicini e li inverto. <br>
*x* = `[0 2 3 5 4 1 0]` ---> *x'* (**vicino**) = `[0 2 4 5 3 1 0]` <br>
Ci sono sempre O(n^2) vicini <br>
**2-OPT ha un'interessante proprietà:**
    - ***f(x'') = f(x) - d(2,3) - d(4,1) + d(2,4) + d(3,1)***
    - ![2opt](./imgs/2opt.png) <br>
    - *Nel TSP simmetrico, f(x'') può essere calcolato da f(x) in O(1)* -> **MOLTO INTERESSANTE** (di solito costa O(n))

File per il TSP
```python
import numpy as np

class Problem_tsp:
    def __init__(self, nc, mat):
        self.ncities = nc
        self.dmat = mat # Matrice che contiene le distanze

    def create_random_instance(nc):
        # Crea due vettori x e y che contengono le coordinate di ciascuna città nel range [-50,50]
        x = 100 * np.random.random(nc) - 50
        y = 100 * np.random.random(nc) - 50
        m = np.zeros((nc, nc))
        for i in range(nc):
            for j in range(nc):
                m[i,j] = np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
        return Problem_tsp(nc,m)
    
    # l è l'elenco dei nodi visitati, includendo il primo e l'ultimo (che sono uguali)
    def objective_function(self, l):
        s = 0
        for i in range(self.ncities):
            c1 = l[i]
            c2 = l[i+1]
            d = self.dmat[c1,c2]
            s = s+d
        return s
    
    def do_2_opt(l, i, j):
        l1 = l[:i+1]
        l2 = l[i+1:j]
        l3 = l[j:]
        return l1+l2[::-1]+l3
    
    # Compute the difference on the objective functuion if the 2-opt operation is performed
    def delta_2_opt(self, l, i, j):
        return -self.dmat[l[i], l[i+1]] - self.dmat[l[j-1], l[j]] + self.dmat[l[i], l[j-1]] + self.dmat[l[i+1], l[j]]
```
Il `delta` è in grado di calcolare quanto cambia la funzione obiettivo se io applico il `2-opt`, senza però farlo effettivamente e senza ricalcolare interamente la funzione obiettivo. <br>
Effettuare `2-opt` e ricalcolare la funzione obiettivo costa **O(n)**, invece così costa **O(1)**. <br>
A questo punto si può implementare una ricerca locale che usa `2-opt`.
```python
def local_search(self, init_sol=None, verbose=False):
        n = self.ncities
        if init_sol is None:
            # Creazione di una soluzione casuale
            x = list(range(1, n))
            np.random.shuffle(x)
            x = [0]+x+[0]
        else:
            x = init_sol.copy()
        improved = True
        fx = self.objective_function(x)
        if verbose:
            print("Initial value {}".format(fx))
        while improved:
            best_delta = 1e300  # Numero grande per i confronti seguenti
            # Il delta sarebbe quanto aumenta la funzione obiettivo se io faccio la 2-opt (l'obiettivo è averlo più basso possibile)
            for i in range(1, n-1): # Controllo cosa succede se applico 2-opt senza effettivamente modificare x (lo cambio solo dopo aver trovato la migliore configurazione possibile)
                for j in range(i+3, n):
                    delta = self.delta_2_opt(x, i, j)
                    if delta < best_delta:
                        i_best = i
                        j_best = j
                        best_delta = delta
            if best_delta < 0:
                fx = fx + best_delta
                x = Problem_tsp.do_2_opt(x, i_best, j_best)
                improved = True
                if verbose:
                    print("New value {}".format(fx))
            else:
                improved = False
        return x, fx 
```
Per provare l'implementazione, vedere il file ***test2.py***. Qui di seguito sono comunque riportati dei comandi di esempio.
```python
from TSP import * 
p = Problem_tsp.create_random_instance(50)
print(p.ncities)
print(p.dmat)

l = list(range(0, 50))
l.append(0)
print(len(l))

print(p.objective_function(l))

l1 = Problem_tsp.do_2_opt(l, 22, 44)
print(p.objective_function(l1))

delta = p.delta_2_opt(l, 22, 44)
print(delta)
print(p.objective_function(l)+delta)

p = Problem_tsp.create_random_instance(20)
print(p.local_search(verbose=True))
```
- applicare ILS
- applicare SA

Per quanto riguarda le istanze del TSP, è possibile:
- generarle a caso
- leggerle da file
    - Sono disponibili delle repo contenenti varie istanze <br>
    Vedi:
        - https://github.com/mastqe/tsplib.git
        - http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/

<hr>

# **Algoritmi genetici**
### **Caratteristiche**
È l'algoritmo più famoso in letteratura. <br>
L'algoritmo genetico si applica per risolvere un problema di ottimizzazione. <br>
È la più famosa metaeuristica.

È basata su una metafora semplice da capire
- **L'algoritmo usa una popolazione di individui**
- **Ciascun individuo è una soluzione del problema ed è rappresentato in genere come una stringa** (binaria)

Questa popolazione è modificata attraverso 3 operazioni
1. **Crossover**
2. **Mutazione**
3. **Rimpiazzamento**

C'è anche un'operazione antecedente al crossover: <br>
**0.** **selezione**: non modifica la popolazione, serve come punto di partenza per il crossover

La rappresentazione degli individui è detta **cromosomi**. 
- Ogni individuo è rappresentato come un cromosoma. Il cromosoma è il patrimonio genetico di un individuo.

Altre caratteristiche:
- Gli **GA** (genetich algorithm) sono molto studiati in molti articoli scientifici. Sia dal punto di vista teorico che dal punto di vista applicativo.
- GA **possono essere applicati a moltissimi problemi di ottimizzazione, sia discreti che continui.**
    - GAs hanno una **predisposizione per il discreto**. Sono naturalmente applicati a problemi discreti perchè gli individui sono stringhe.
- *GA sono stati introdotti da Holland nel 1970 e da allora sono la metaeuristica più famosa in assoluto* (da allora sono studiati e applicati in tantissime situazioni in cui gli algoritmi tradizionali non riescono a funzionare).

### **Rappresentazione cromosomi** 
#### **Applicazione di un algoritmo genetico ad un problema binario:**
s = [0,1,0,1,0,0,1,1]
- 8 **alleli**, ciascuno dei quali contiene un 0 o 1 (che sono chiamati **geni**)
    - gli **alleli** sono le **posizioni**
    - i **geni** sono che cosa **contiene**

<hr>

Ripassando, nei GA si ha:
- ***f*** funzione obiettivo
- ***X*** spazio di ricerca
- Popolazione di ***N*** individui, chiamati **cromosomi**. 
    - *Ciascun cromosoma codifica una soluzione, cioè un elemento di X*

Se il cromosoma *c* è direttamente la soluzione, f può essere applicata al cromosoma *c*. <br>
Altrimenti *f* deve essere riscritta (ridefinita) in modo da poter essere applicata a *c*, oppure *c* deve essere decodificato in modo da ottenere la soluzione corrispondente.

***Esempio***:
### **Applicazione degli algoritmi genetici al TSP***
Sono possibili molte rappresentazioni dello spazio di ricerca X:
1. Un cromosoma è la lista dei vertici visitati <br>
    `[0, 2, 3, 1, 5, 4, 0]`
2. Un cromosoma è la lista degli archi visitatu <br>
   `[(0,2), (2,3), (3,1), (1,5), (5,4), (4,0)]`
3. Un cromosoma è una matrice binaria di dimensione ***n x m*** tale che l'elemento M[i,j] = 1 se e solo se l'arco (i-->j) è visitato. <br>
*Questa rappresentazione funziona correttamente solo se il TSP è simmetrico.*
4. *Potrebbero esistere anche altre rappresentazioni*

**La funzione obiettivo f** va quindi riscritta per ognuna di queste rappresentazioni, oppure decido una volta per tutte quale deve essere la rappresentazione esterna, scrivo la funzione per quest'ultima e ogni volta che l'algoritmo genetico deve valutare f trasformo il cromosoma in soluzione. <br>
Quindi, ci sono 2 approcci per valutare la funzione obiettivo:
1. **Scrivo il codice per valutare f secondo la rappresentazione.**
2. **Scrivo un codice per valutare f usando uno standard per la soluzione** (per esempio una lista di vertici visitati). <br> 
Ogni volta che la funzione deve essere valutata da GA, si traduce il cromosoma nella forma standard applicando una funzione di decodifica per ottenere la soluzione.

Quindi, GA può decidere, per qualsiasi motivo, una rappresentazione interna (**GENOTIPO**) diversa da quella su cui l'utente ragiona (rappresentazione standard) (**FENOTIPO**).

<hr>

## **Pseudocodice di GA**
```pseudocode
function GA(X, f,                       //parametri del problemma
    N, Ngen, pCross, pMut)              //parametri dell'algoritmo

    inizializzo la popolazione
    for g:=1 to Ngen
        select the mating pool
        apply the crossover operation
        apply the mutation operator
        update the population
    end for
    
    return il miglior individuo trovato x* e il corrispondente f value f(x*)
```
*Cosa significa il miglior individuo trovato?*
- Molte metauristiche basati su metauristiche possono produrre, in qualsiasi passaggio, individui che sono peggiori o migliori di quelli prodotti nei passaggi precedenti.
    - Quindi ha senso memorizzare il miglior individuo trovato fino a quel punto (stato corrente).
    - C'è quindi una variabile nell'algoritmo che mi permette di controllare se il nuovo individuo è migliore di quello momentaneamente memorizzato.
        - Li confronto e in caso positivo salvo quello nuovo.

Ciò è molto utile se:
- L'algoritmo non sempre accetta miglioramenti
- L'algoritmo usa qualche meccaniscmo di restart (non riesco a migliorare allora provo a ripartire)

***NOTA***: Miglior individuo trovato -> variabile che conserva il miglior individuo di sempre.

La popolazione può essere inizializzata in 3 modi principali:
1. **Completamente a caso**
    - Se il problema **non ha vincoli**, tutte le soluzioni sono valide.
    - Se il problema **ha vincoli** (ad esempio il problema dello zaino), significa che non tutti gli individui rappresetano una soluzione valida
2. **Creare solo cromosomi validi**
3. **Creare 'buoni' individui** (non così scarsi). Per esempio utilizzando un'euristica ***h*** che mi permette di farlo.
    - **se h è deterministica**, può produrre un solo individuo. Di conseguenza gli altri N-1 vanno scelti a caso.
    - **in generale**, usare h solo per generare soltanto alcuni individui e gli altri generati in modo casuale.

#### **Differenza tra euristica e metaeuristica:**
- euristica è dipendente dal problema
- la metaeuristica no

## **Mating Pool**
Tornando alla spiegazione dello pseudocodice dell'algoritmo: <br>
***Primo passaggio:***
- *select of the mating pool M*

***Definizione***. <br>
Il mating pool M è un insieme di N/2 coppie di individui presi dalla popolazione (per esempio la popolazione attuale).
- M è usato per il passaggio successivo (Crossover)
- L'idea principale è di scegliere i migliori individui

*Come scegliere gli individui migliori?*
- **Roulette wheel**
- **Tornei**

### **Roulette wheel (ruota della fortuna)**

![rw](./imgs/rw.png)

- Selezionare un individuo in modo casuale secondo la probabilità (in modo proporzionale) alla **fitness F** per ogni individuo.
    - *Un GA ha l'obiettivo implicito di massimizzare il valore di fitness degli elementi della popolazione degli individui.*
        - Posso accontentarmi anche di un singolo individuo con un alto valore di fitness F

**Caratteristiche:**
- Se il problema è di ottimizzazione è un problema di **massimizzazione**:
    - F può coincidere con la funzione obiettivo f.
    - Oppure **F è una trasformazione crescente di f**.
        - Es. F(x) = f(x)^2 <br>
- Se il problema di ottimizzazione è un problema di **minimizzazione**: 
    - **F deve essere una trasformazione decrescente**.
        - Es. F(x) = 1/f(x) <br>
        F(x) = 1000 - f(x) <br>
        F(x) = -log f(x) <br>
    - In questo caso se `f(x1) < f(x2)` (x1 è migliore di x1), allora `F(x1) > F(x2)` (x1 ha un valore di fitness maggiore di x2)
    - *Il TSP è un problema di minimizzazione*

Supponiamo che le fitness F(x) > 0 (siano tutte positive) per ogni x. <br>
La probabilità di pescare l'individuo x[i] è data da: <br>
```
F(x[i]) / F(x[1]) + F(x[2]) + ... + F(x[N])
```
***Per esempio***: <br> 
F(x1) = 10, F(x2) = 5, F(x3) = 15, F(x4) = 20, F(x5) = 10 <br>
p(x1) = 10 / (10 + 5 +15 +20 +10)    ----> 10/60 <br>
p(x2) = 5/60 <br>
ecc....

- Per pescare un individuo, si genera un numero reale casuale r tra 0 e 60.
    - Se r < 10 ---> estrai x1
    - Se r è tra [10, 15[ ---> estrai x2
    - se r è tra [15, 30[ ---> estrai x3
    - se r è tra [30, 50[ ---> estrai x4
    - se r è tra [50, 60[ ---> estrai x5

In questo modo genero ogni numero x[i] con una **probabilità proporzionale** a F(x[i]). <br>
**Il costo computazionale della singola estrazione è O(N)**.

- F può essere considerata anche come **rank** di x nella popolazione.
    - F=N per il *miglior individuo*
    - F=N-1 per il secondo miglior individuo
    - ...
    - F = 1 per il *peggior individuo*


### **Selezione baata su tornei**
- **scelgo k individui a caso e scelgo il migliore tra di loro** (a mo' di sfida)
- **è più veloce rispetto a fare la roulette wheel**
    - il costo di selezionare N/2 coppio è **O(kN)**, invece di **O(N^2)** per la roulette wheel

In questo modo il peggior individuo non verrà mai selezionato (non ha chance di essere selezionato perchè prendendo anche solo due individui. Il peggiore non sarà mai scelto a meno che tra le selezione degli individui io posso pescare più volte lo stesso individuo. In questo modo potrei prendere due peggiori e quindi viene selezionato). <br>
Questi metodi di selezione possono produrre un mating pool con individui identici

- I migliori individui possono essere rappresentati più volte.
    - Migliore è l'individuo e più coppie potrebbero esserci di lui.
    - I peggiori individui potrebbere anche essere assenti nel mating pool.
- Se un individuo è molto più buono degli altri:
    - con la roulette ci possono essere tante copie di lui a discapito degli altri
    - con i tornei non è detta ma potrebbe esserci comunque un numero abbastanza alto di copie

<hr>

## 1. **Crossover**
- L'operazione di crossover prende due cromosoimi **s1** e **s2**, genera 1 o 2 **nuovi  cromosomi**
- s1 e s2 sono chiamati **genitori**
- I due nuovi cromosomi **c1 e c2** sono chiamati **figli** 
- Si parte quindi da **N/2** coppie di individui
    - p1, p2
    - p3, p4
    - ...
    - p[N/2 -1], p[N/2]

Ciascuna di queste coppie è copiata e inviata allo step successivo (con probabilità **1-pCross**) oppure è modificata utilizzando l'operatore di crossover (con probabilità **pCross**).
- Ciascuna coppia p[i], p[i+1] produce 2 figli c[i], c[i+1]
    - c[i] = p[i] e c[i+1] = p[i+1] con probabilità **1-pCross**
    - c[i], c[i+1] = crossover(p[i] , p[i+1]) con probabilità **pCross**

***Operazioni di Crossover:*** <br>
Crea 2 figli (qualche volta un solo figlio ma deve essere applicato 2 volte, altre volte più figli e ne scelgo solo due) dai due genitori.
- ***one-point crossover***:
    - Utilizzato quando i due cromosomi sono stringhe o vettori di lunghezza fissa L
    - seleziona un **punto di taglio k casuale** tra 1<=k<L
    - *Per esempio:* <br>
    L'operazione chiamata <br>
    s1 = [0,1,0,1,0,0,1,1] <br>
    s2 = [1,1,0,1,0,1,0,0] <br>
    Si prende un **punto di taglio** e si crea un figlio con gli elementi a sinistra del taglio di uno e a destra del taglio dell'altro, e viceversa per l'altro figlio. <br>
    ![crossover](./imgs/crossover.png) <br>
    In questo modo si può vedere che ***ciascun figlio eredita parte del patrimonio genetico dal primo genitore e parte dal secondo***. <br>
    `Si può dire che il crossover mescola i patrimoni genetici di due elementi di una popolazione, creando due elementi che sono nuovi.`
- È semplice gneralizzare il **one-point crossover al multi-point crossover**
    - ***2-point crossover***
        - **selezione 2 punti di taglio k e h** in modo casuale tale che k<h
        - *Per esempio:* <br>
        ![crossover2](./imgs/crossover2.png)
- ***Crossover uniforme:***
    - i figli ereditano da un genitore o dall'altro in modo casuale
    - *Per esempio:* <br>
    ![crossover3](./imgs/crossover3.png)
- *Ci sono anche molti altri tipi di crossover per altri tipi di cromosomi*
    - *Per esempio*: <br>
    **In TSP il one-point crossover non funziona bene**
        - da una coppia di cromosomi validi(genitori), può produrre 2 figli non validi
            - `p1 = 0 1 3 4 5 2 0`
            - `p2 = 0 2 1 5 3 4 0`
            - Se faccio il crossover ad un punto: <br>
            ![crossover4](./imgs/crossover4.png) <br>
            c1 visita 3 due volte, ma non visita 2. <br>
            c2 fa il contrario. <br>
            Il problema sta in questo punto. Questo perchè in una soluzione del TSP ogni figlio deve visitare ogni nodo esattamente una volta.
            - Questo metodo di ricombinazioni non è adatto per il TSP (e anche per altri problemi basati sulle permutazini).
            - Neanche il Crossover uniforme funziona, ha ancora più chance di creare doppioni rispetto al one-point.
            - **Nel TSP si utilizzano altri sistemi per il crossover**

<hr>

## 2. **Mutazione**
***Definizione***. <br>
Mutazione significa alterare il cromosoma dei figli. <br>
I figli possono essere sia copie dei genitori o prodotti dal crossover (non è importante).
- Crea un nuovo individuo **mutando/alterando** un figlio appena prodotto dal crossover.
    - ***c -----> c'***
    - Lo si altera ad esempio **cambiando uno o più geni**.
- Queste operazioni si possono fare sulla rappresentazione e non sull'individuo (**differenza tra fenotipo e genotipo**)
- Il crossover usa il materiale genetico dalla popolazione
    - Il crossover ricombina tra loro cose che già esistono, non si hanno componenti nuovi per produrre individui. L'originialità è dovuta al fatto che li combino in modo diverso.
- **Invece la mutazione può produrre nuove componenti**

### **Operatore di Mutazione Standard**
Può essere usato quando i cromosomi sono vettori o stringhe. <br>
Altera ogni gene con una probabilità pMut *(probabilità di mutazione)*.

`c[i] = 0 1 0 1 0 0 1 1 1 0` *(stringa di bit binaria)* <br>
pMut = 0.1
- Significa che in media solo un gene (bit) su 10 viene alterato.
    - Con probabilità 1/10 lo altero
    - Con probabilità 9/10 lo lascio invariato.

`c'[i] = 0 1 0 1 0 1 1 1 1 0`

**NOTA**: ****pMut*** in generale si tiene bassa*

### **Selezionare la nuova popolazione**
Si hanno questi elementi tra cui scegliere:
- **N genitori**      (elementi della popolazione corrente) <br>
- **N figli**         (prodotti da crossover+mutazione)

1. **Valutare tutti gli N figli**
    - La nuova popolazione è composta dagli N figli (sostituzione dei genitori con i figli). Questo è ciò che accade a lungo andare in natura. Potrebbe tuttavia verificarsi che non tutti i figli siano adatti a vivere in questo ambiente.  
2. **Elitismo**: <br>
    La nuova popolazione è composta da 
    - K migliori individui tra i genitori e i figli
    - N-K figli <br>
    ***Esempio***: <br>
    K = 1   -> se il miglior individuo è un genitore, quest'ultimo viene selezionato e il peggior figlio non viene selezionato.
3. **Sopravvivono i migliori**: <br>
    È una condizione particolare del punto precedente. <br>
    Ovvero K = N. <br>
    La nuova popolazione è composta dai N migliori individui tra i genitori e i figli. <br>
    Non importa quindi l'età. È possibile che il miglior individuo rimanga sempre nella popolazione (immortale). Ciò è possibile anche nell'elitismo.
    
### **Breve recap sugli algoritmi genetici**: <br>
L'implementazione di un algoritmo genetico richiede molte scelte:
- **I parametri dell'algoritmo**:
    - `N` -> grandezza della popolazione
    - `num_gen` -> numero di generazioni (iterazioni dell'algoritmo genetico)
    - `pCross` -> probabilità del crossover (probabilità che una coppia selezionata durante il mating pool gli venga applicato il crossover)
    - `pMut` -> probabilità della mutazione
    - *Come si selezionano?* <br>
        Si fanno un pò di tentativi. Non ci sono regole generali che funzionano sempre. <br>
        **In generale**
        - pCross dovrebbe essere abbastanza alto (tra 0.8 e 1)
        - pMut dovrebbe essere bassa
        - N dovrebbe andare di pari passo alla dimensione del problema. Un problema più grande dovrebbe avere una popolazione più grande
        - Il numero di iterazioni (num_gen) dovrebbe essere sostituito da un altro criterio -> ***Criteri di terminazione***

### **Criteri di Terminazione**
- Dopo **num_gen** iterazioni/generazioni (criterio di iterazioni)
- Dopo **num_sec** secondi (criterio temporale)
    - ***Svantaggio***: dipende dalla velocità di esecuzione del programma. Il criterio ha senso se voglio una risposta velocemente. Il criterio non ha senso se voglio testare algoritmi testati su macchine diverse, è dipendente dalla macchina.
- Termino quando la funzione obiettivo ha raggiunto un livello prefissato

### Punti di scelta dell'algoritmo (oltre ai parametri):
- Criteri di terminazione
- Inizializzazione
- Selezione del mating pool
- Come fare il crossover
- Come fare la mutazione
- Come fare il rimpiazzamento (selezione della nuova popolazione)

***Crossover e mutazione dipendono fortemente dal problema. Dipendono dalla rappresentazione che si fa delle soluzioni.***

<hr>

## **Implementazione di un GA (recap)**
1. **Si deve implementare il problema** (la classe, i suoi metodi e funzioni)
    - Creare un'istanza a caso
    - Caricare un'istanza da file
    - Calcolare la funzione obiettivo (data una soluzione in qualche forma)
        - *Scegliere come rappresentare la soluzione* (già qui si deve scegliere che rappresentazione utilizzare)
2. **Implementare il Crossover e la Mutazione per la rappresentazione scelta dal programmatore**
3. **Il programamtore deve anche scegliere tutti i passaggi che devono essere fatti all'interno dell'algoritmo:**
    1. Inizializzazione
    2. Criterio di terminazione
    3. Selezione
    4. Rimpiazzamento (replacement)
    5. (Eventualmente) Altri passaggi (non solo in GA ma anche in altre metaeuristiche):
        - Metodi di ricerca locale per migliorare le soluzioni (*combinare la forza di un GA con un algoritmo di ricerca locale*: **Algoritmo Memetico**)
        - Un possibile modo per applicare la ricerca locale è quello di cercare di migliorare la miglior soluzione trovata dal GA. <br>
        ![gals](./imgs/gals.png) <br>
        - Un altro possibile modo si applica nella situazione in cui talvolta la popolazione perde diversità (gli individui iniziano ad assomigliarsi molto l'un l'altro). La peggior situazione è che diventino tutti uguali. <br>
        Molti operatori di Crossover hanno la seguente proprietà: <br>
        *Se p1 = p2 allora il Crossover(p1, p2) produce figli uguali ai genitori*. <br>
        Quando un individuo è molto meglio degli altri (**super-individuo**), quest'ultimo tende a monopolizzare la popolazione (la porta ad essere simile a lui). Quando tutti gli individui sono uguali GA non funziona. L'unica operazione che potrebbe far uscire da questo stallo è la Mutazione. <br>
        **Prima cosa**: riconoscere quando la popolazione ha significativamente perso la sua diversità (ci sono varie tecniche per farlo). <br>
        **Seconda cosa**: Reagire (Ad esempio fermare l'algoritmo o reinizializzare la popolazione o una parte di essa, magari salvando la best solution ever found).
    6. Parametri

La configurazione di un algoritmo genetico (scegliere tutto quello che deve essere scelto, ovvero i parametri e i metodi) può essere automatizzata. Cioè io posso avere dei meccanismi che scelgono i parametri in maniera da ottimizzarli.

### **Crossover per le permutazioni**
***p1*** = 0 2 **3 5 1** 6 4 <br>
***p2*** = 2 5 **1 4 3** 0 6

c1 prende gli elementi mancanti nell'ordine in cui si trovano in p2. <br>
c1 = 2 4 **3 5 1** 0 6
c2 = 0 2 **1 4 3** 5 6

Questo si chiama ***ordered crossover**:
- Significa prendere un segmento di ognuna delle due permutazioni, ricopiarlo nei figli e poi gli elementi che mancano, prenderli dall'altro genitore nell'ordine in cui si trovano (non nelle stesse posizioni).

### **Mutazione per le permutazioni**
Scambia **k** coppie in modo casuale. <br>
K deve essere compatibile con pMut. <br>
***Esempio:*** <br>
![knsu2](./imgs/knsu2.png)

<hr>

## **Implementazione di un algoritmo genetico per il problema MAX-CUT**
Dato un grafo non orientato G=(V,E) trovare un sottoinsieme U1 ⊂ in V tale che il numero di tagli indotto da U1, U2 = V \ U1 è massimo. <br>
**Un **taglio** è un arco (x,y) ∈ E tale che x ∈ U1, y ∈ U2 o x ∈ U2, y ∈ U1.**

![tagliga](./imgs/tagliGA.png) <br>
I tagli sono in verde. Un taglio è quindi un arco da un vertice di un insieme verso uno di un altro.

**MAX-CUT è un problema NP-hard**.

**Lo scopo è quello di trovare U1 in modo tale che f sia massima.** <br>
Una soluzione può essere descritta come una stringa di n-bit dove n è il numero dei vertici n=|V| (si presta bene agli algoritmi genetici). <br>
x = (1,0,0,1,1,0,1) <br>
xi = 1 se i ∈ U1 <br>
xi = 0 se i ∈ U2 <br>

```python
# Un'istanza è data dal numero dei nodi numerati da 0 al numero di nodi -1 (0, . . ., num_nodes-1) -> se ho 6 nodi sono numerati da 0 a 5
# È data anche dalla lista degli archi (una coppia di nodi) 
import numpy as np

class Maxcut_problem:
	
	def __init__(self, num_nodes, edges):
		self.num_nodes = num_nodes
		self.edges = edges

	def create_random_instance(num_nodes, edge_prob):
		edges=[]
		for i in range(0,num_nodes):
			for j in range(i+1,num_nodes):
				if np.random.random()<edge_prob:
					edges.append((i,j))
		return maxcut_problem(num_nodes,edges)

	def objective_function(self,c):
        # c è un vettore di n-bit
		# c is a num_nodes binary string
		num_cuts = 0
		for x,y in self.edges:
			if c[x]!=c[y]:
				num_cuts +=1
		return num_cuts

	def get_dim(self):
		return self.num_nodes
```
```python
# A simple genetic algorithm for unconstrained binary maximization problems
import numpy as np

class Binary_genetic_algorithm:

	def __init__(self, problem, num_elem=None, num_gen=100, pcross=0.9, pmut=0.01):
		self.problem=problem
		self.num_bits=problem.get_dim()
		if num_elem is None:
			self.num_elem=self.num_bits
		else:
			self.num_elem=num_elem
		self.pcross=pcross
		self.pmut=pmut
		self.num_gen=num_gen

	def run(self):
		self.init_population()
		for gen in range(0,self.num_gen):
			mating_pool=self.select_mating_pool()
			children=self.do_crossover(mating_pool)
			self.do_mutation(children)
			self.select_new_population(children)
		return self.best, self.best_f

	def init_population(self):
		self.population=[]
		self.f_obj=np.zeros(self.num_elem)
		self.best=None
		self.best_f=-1
		for i in range(0,self.num_elem):
			ind=np.random.randint(0,1+1,self.num_bits)
			self.population.append(ind)
			self.f_obj[i]=self.problem.objective_function(ind)
			self.update_best(ind,self.f_obj[i])
		
	def update_best(self, x, fx):
		if fx>self.best_f:
			self.best_f=fx
			self.best=x
			print("new best ",fx)
	
	def select_mating_pool(self):
		mating_pool=[]
		for i in range(0,self.num_elem//2):
			p1=self.roulette_wheel()
			p2=self.roulette_wheel()
			mating_pool.append((p1,p2))
		return mating_pool

	def roulette_wheel(self):
		s=np.sum(self.f_obj)
		r=np.random.random()*s
		i=0
		while r>s:
			r=r-self.f_obj[i]
			i=i+1
		return self.population[i]

	def do_crossover(self, mating_pool):
		children=[]
		for p1, p2 in mating_pool:
			if np.random.random()<self.pcross:
				c1, c2 = self.crossover_operator(p1,p2)
			else:
				c1=p1.copy()
				c2=p2.copy()
			children.append(c1)
			children.append(c2)
		return children

	def crossover_operator(self, p1, p2):
		# one point crossover
		l1=list(p1)
		l2=list(p2)
		j=np.random.randint(1,self.num_bits)
		c1=np.array(l1[:j]+l2[j:])
		c2=np.array(l2[:j]+l1[j:])
		return c1,c2

	def do_mutation(self,children):
		for c in children:
			for i in range(0, self.num_bits):
				if np.random.random()<self.pmut:
					c[i]=1-c[i]

	def select_new_population(self,children):
		# Find the best among the children and the parents
		f_child=np.array([self.problem.objective_function(c) for c in children])
		ib1=np.argmax(self.f_obj)
		ib2=np.argmax(f_child)
		# First case: the best child is better than the the best parent
		if f_child[ib2]>self.f_obj[ib1]:
			self.population=children
			self.f_obj=f_child
			self.update_best(children[ib2],f_child[ib2])
		else:
			iw=np.argmin(f_child)
			children[iw]=self.population[ib1]
			f_child[iw]=self.f_obj[ib1]
			self.population=children
			self.f_obj=f_child		
```
Per provare l'implementazione, vedere il file ***test.py***. Qui di seguito sono comunque riportati dei comandi di esempio.
```python
from binary_genetic_algorithm import *
from maxcut import *

p = Maxcut_problem.create_random_instance(20, 0.1)
g = Binary_genetic_algorithm(p, num_elem=20)
print(len(p.edges))
g.run()
```
<hr>

## **Implementazione di un algoritmo genetico per il problema TSP**
Qui di seguito è riportata l'implementazione del TSP, vedere l'apposito file nella directory degli algoritmi genetici.
```python
class Tsp_problem:

	def __init__(self,n_cities, dist_matrix):
		self.n_cities=n_cities
		self.dist_matrix=dist_matrix


	def create_random_instance(n):
		x=np.random.random(size=n)
		y=np.random.random(size=n)
		m=np.zeros((n,n))
		for i in range(n):
			for j in range(n):
				m[i,j]=np.sqrt((x[i]-x[j])**2+(y[i]-y[j])**2)
		
        return Tsp_problem(n,m)


	def objective_function(self,x):
		 # x è la lista ordinata dei nodi visitati, eccetto l'ultimo vertice (che è anche il primo)
        # 1 2 0 4 5 3 1
		cost=0
		for i in range(0,self.n_cities-1):
			c1=x[i]
			c2=x[i+1]
			cost+=self.dist_matrix[c1,c2]
		# Costo per tornare al primo
		c1=x[-1]
		c2=x[0]
		cost+=self.dist_matrix[c1,c2]
		
        return cost


	def get_dim(self):
		return self.n_cities
```
È ora necessario modificare l'algoritmo genetico definito per il problema del MAX-CUT in modo tale che sia possibile utilizzarlo per il problema TSP (vedi file `permutation_genetic_algorithm.py`).
```python
# A simple genetic algorithm for unconstrained permutation minimization problems
import numpy as np

class Permutation_genetic_algorithm:

	def __init__(self, problem, num_elem=None, num_gen=100, pcross=0.9, pmut=0.01):
		self.problem=problem
		self.num_nodes=problem.get_dim()
		if num_elem is None:
			self.num_elem=self.num_nodes
		else:
			self.num_elem=num_elem
		self.pcross=pcross
		self.pmut=pmut
		self.num_gen=num_gen

	def run(self):
		self.improvements=[]
		self.init_population()
		for gen in range(1,self.num_gen+1):
			mating_pool=self.select_mating_pool()
			children=self.do_crossover(mating_pool)
			self.do_mutation(children)
			#self.select_new_population_best(children,gen)
			self.select_new_population_elit(children,gen)
		return self.best, self.best_f, self.improvements

	def init_population(self):
		self.population=[]
		self.f_obj=np.zeros(self.num_elem)
		self.best=None
		self.best_f=1e300 # very large number
		for i in range(0,self.num_elem):
			ind=list(range(0,self.num_nodes))
			np.random.shuffle(ind)
			self.population.append(ind)
			self.f_obj[i]=self.problem.objective_function(ind)
			self.update_best(ind,self.f_obj[i],0)
		
	def update_best(self, x, fx, g):
		if fx<self.best_f:
			self.best_f=fx
			self.best=x
			print("new best ",fx," at gen. ",g)
			self.improvements.append((g,fx))
	
	def select_mating_pool(self):
		mating_pool=[]
		self.fitness=np.array([1/f for f in self.f_obj])
		for i in range(0,self.num_elem//2):
			p1=self.roulette_wheel()
			p2=self.roulette_wheel()
			mating_pool.append((p1,p2))
		return mating_pool

	def roulette_wheel(self):
		s=np.sum(self.fitness)
		r=np.random.random()*s
		i=0
		while r>s:
			r=r-self.fitness[i]
			i=i+1
		return self.population[i]

	def do_crossover(self, mating_pool):
		children=[]
		for p1, p2 in mating_pool:
			if np.random.random()<self.pcross:
				c1, c2 = self.crossover_operator(p1,p2)
			else:
				c1=p1.copy()
				c2=p2.copy()
			children.append(c1)
			children.append(c2)
		return children

	def crossover_operator(self, p1, p2):
		ok=False
		while not ok:
			i1=np.random.randint(1,self.num_nodes-1)
			i2=np.random.randint(1,self.num_nodes-1)
			if i1!=i2:
				ok=True
		j1=min(i1,i2)
		j2=max(i1,i2)
		c1=Permutation_genetic_algorithm.ordered_crossover(p1,p2,j1,j2)
		c2=Permutation_genetic_algorithm.ordered_crossover(p2,p1,j1,j2)
		return c1,c2

	def ordered_crossover(p1,p2,j1,j2):
		n=len(p1)
		c=[None]*n
		for j in range(j1,j2+1):
			c[j]=p1[j]
		h=0
		for j in range(n):
			if p2[j] not in c:
				assert(c[h]==None)
				c[h]=p2[j]
				h+=1
				if h==j1:
					h=j2+1
		return c

	def do_mutation(self,children):
		for c in children:
			if np.random.random()<self.pmut:
				Permutation_genetic_algorithm.perform_exchanges(c,1)

	def perform_exchanges(c,ns):
		for i in range(ns):
			ok=False			
			while not ok:
				i1=np.random.randint(1,len(c)-1)
				i2=np.random.randint(1,len(c)-1)
				if i1!=i2:
					ok=True
			c[i1],c[i2]=c[i2],c[i1]
					
	def select_new_population_best(self,children,g):
        '''
        Ricapitolando:
            Ho messo insieme i padri (self.population) e i figli.
            Ho calcolato la funzione obiettivo per ogni figlio.
            Ho messo insieme, in un'unica lista, le funzioni obiettivo dei padri (che già avevo) e dei figli.
            Ho creato una lista che contiene gli indici di tutti (sia padre che figli):
                - i padri hanno un indice che va da 0 a num_elem-1
                - i figli da num_elem in poi
            Ho ordinato questa lista di indici in base al valore della funzione f.
            Ho preso la prima parte di questi indici.
            Ho ricostruito la nuova popolazione prendendo i valori di l soltanto per indici migliori e i valori di f.
            Infine ho chiamato la funzione update_best.
            Questo meccanismo in generale si potrebbe usare come select new population anche per i problemi binari.
        '''
		l=self.population+children
		fc=[self.problem.objective_function(c) for c in children]
		f=list(self.f_obj)+fc
		l1=list(range(2*self.num_elem))
		l1.sort(key=lambda i: f[i])
		l1best=l1[:self.num_elem]
		self.population=[l[i] for i in l1best]
		self.f_obj=[f[i] for i in l1best]
		self.update_best(self.population[0],self.f_obj[0],g)
		
	def select_new_population_elit(self,children,g):
		# find the best among the children and the parents
		f_child=np.array([self.problem.objective_function(c) for c in children])
		ib1=np.argmin(self.f_obj)
		ib2=np.argmin(f_child)
		# first case: the best child is better than the the best parent
		if f_child[ib2]<self.f_obj[ib1]:
			self.population=children
			self.f_obj=f_child
			self.update_best(children[ib2],f_child[ib2],g)
		else:
			iw=np.argmax(f_child)
			children[iw]=self.population[ib1]
			f_child[iw]=self.f_obj[ib1]
			self.population=children
			self.f_obj=f_child
```
È comunque possibile ottimizzare i vari paranetri come pCross e pMut per avere i migliori risultati. <br>
È inoltre consigliato fissare un seed per rendere i risultati riproducibili.

Non sempre la migliore soluzione è generare istanze di cui la soluzione non è nota, un'opzione migliore potrebbe essere quella di utilizzare istanze preparate appositamente per vedere se si raggiunge la soluzione ottima o quanto ci si avvicina ad essa. Per questo è disponibile una libreria apposita, come già detto, contente istanze per il problema del TSP.

Si possono anche osservare le curve di convergenza, plottandole. Per vedere delle prove, fare riferimento all'apposito file di test.

<hr>

### **Parametri su cui si può agire in un GA e la loro influenza**
- ***N*** -> *dimensione della popolazione*
- ***maxgen*** -> *numero di generazioni*
- ***pCross*** -> *probabilità di Crossover*
- ***pMut*** -> *probabilità di Mutazione*

#### **N dimensione della popolazione**
*Che effetto ha aumentare la dimensione della popolazione?* <br>
È chiaro intiutivamente che più la popolazione è piccola e minore è la ricchezza del patrimonio genetico (una popolazione piccola è più soggetta alla perdita di diversità in modo molto veloce). Allo stesso modo è chiaro che N influenza il tempo di esecuzione dell'algoritmo.
- Quando **N è piccolo**, il rischio di perdere diversità è molto alto -> **non c'è più evoluzione**
- Quando **N è alto**, il tempo di computazione cresce (il tempo di calcolo è proporzionale a N)
- I GA non sono così sensibili ai valori di N, tranne quando N è troppo piccolo
- In genere si sceglie N in modo da essere proporzionale alla dimensione del problema

#### **maxgen Numero di generazioni**
*Influenza direttamente la terminazione*. <br>
Se lo faccio terminare troppo presto, è probabile che le soluzioni trovate non siano buone. Anche questo parametro dipende dalla dimensione del problema. <br>
Solitamente un buon valore per max-gen può essere calcolato dalla dimensione del problema
- **Idea generale**: più è grande la dimensione del problema, più è grande lo spazio di ricerca e quindi servono più generazioni.
- Quindi: ***problem size -> search space size -> number of generation needed***

#### **pCross probabilità di Crossover**
È la probabilità di utilizzare l'operazione di Crossover su una coppia del mating pool. <br>
***Normalmente pCross è alta -> tra 0.8 e 1***

#### **pMut probabilità di Mutazione**
Nelle stringhe di bit è la probabilità di mutare il singolo gene (se muto ogni singolo gene in maniera indipendente, allora possiamo fare una singola mutazione per genere che deve essere mutato). <br>
Nel TSP invece non c'è il discorso dei geni (perchè si ha a che fare con permutazioni), ma il discorso dei cromosomi (io quindi devo specificare quanto mutare il cromosoma. Quanto lo muto? Nella nostra implementazione si considerava il numero degli scambi).

***pMut è la probabilità di mutare il gene/cromosoma***

Nelle **permutazioni** non si può fare la mutazione a livello di gene perchè non si può alterare un singolo elemento della permutazione. <br>
**NOTA**: Nelle permutazioni, l'operatore di Mutazione deve essere applicato all'intera permutazione e non ad un singolo gene.
***Esempio***:
0 5 **1** 4 3 2 <br>
Qualsiasi individuo che metto al posto di **1**, produce una lista che non è una permutazione!

1. La Mutazione è necessaria (nell'esempio del TSP se si mette pMut=0 si rimane bloccati alle prime iterazioni) perchè **senza di essa non c'è evoluzione** (o ce ne è veramente poca). Il motivo è che la mutazione è l'unico modo per introdurre del materiale genetico non esistente.
2. Quando la Mutazione è troppo forte, produce degli individui che sono molto diversi dallo ***standard*** della popolazione. <br>
Un buon valore per la probabilità di mutazione è tendenzialmente basso, es: <br>
0.01; 0.001; 0.02 <br>
Nonostante deve essere bassa, la Mutazione deve comunque essere presente.

### **Metodi di Rimpiazzamento/Replacement (selezione della nuova popolazione)**
1. **Generazionale**
    - I figli vanno al posto dei geniori
    - Non importa quanto sono peggio o meglio dei genitori
2. **Elitismo**
    - Conserva il migliore individuo della popolazione, o i migliori individui
3. **I migliori individui tra i genitori e i figli**

Negli algoritmi genetici si privilegia l'elitismo o il far sopravvivere i migliori (punto 3). <br>
In generale l'elitismo funziona abbastanza bene. Favorisce uno svecchiamento della popolazione.

- L'elitismo può rinnovare la popolazione senza perdere i migliori individui. Qui vince l'*età*.
- Selezionare i migliori ***n*** individui tra i genitori e i figli solitamente funziona meglio. Qui ha la meglio la *fitness* (più gli individui sono buoni più sopravvivono).
    - Questo meccanismo ha però più proabilità di bloccarsi perchè possono rimanere sempre gli stessi individui

Si può vedere la differenza tra l'elitismo e la scelta dei migliori n individui nel problema del TSP in cui sono state implementate entrambe le versioni per la scelta della nuova popolazione. Per maggiori informazioni vedere il codice di `permutation_genetic_algorithm.py`.

<hr>

### **Info sugli algoritmi**
***Caratteristiche implementative*** <br>
Supponiamo di avere due o più metodi per fare la stessa operazione (ad es. selezione dei migliori e selezione per elitismo). Dal punto di vista implementativo conviene fare due classi (che non contengono l'intero algoritmo ma i due codici).

Esempio sulla selezione (elitismo e migliori):
- classe che implementa la selezione:
    ```python
    class selection_best:
    def __call__(self, pop, children): #call permette di vedere l'oggetto di questa classe come se fosse una funzione
        #implement the selection
        # i migliori individui trai i genitori e i figli
    ```
- Fare stessa cosa per l'altro metodo:
    ```python
    class selection_elite:
        def __call__(self, pop, children):
        # implement the elitism selection
    ```
Si hanno quindi due classi che si possono utilizzare come se fossero due funzioni. <br>
Nell'algoritmo genetico:
```python
class gentic_algorithm:
    def __init__(self, problem, num_elem, pCross, pMut, . . ., sel_method):
    .
    .
    .
    .
    .
    if sel_method == 'best':
        self.selection = selection_best()
    elif sel_method == 'elite'
        self.selection = selection_elite()



    def run(self):
        self.selection(self.population, children) # invoca il metodo scelto nel costruttore
```
Questa cosa può essere fatta in più linguaggi di programmazione oltre a python. <br>
È raccomandato utilizzare questo **design pattern** per tutte le alternative del nostro algoritmo. In questo modo è possibile controllare l'esecuzione da riga di comando, non c'è bisogno di duplicare il codice ed è veloce.

Ci sono molti operatori di crossover e mutazione.
Per esempio, una permutazione può essere mutata con un'inserzione

In particolare, ci sono alcuni operatori di crossover studiati appositamente per il TSP.

<hr>

# **Problemi vincolati**
(applicazione degli algoritmi genetici ad un problema vincolato)
## **Algoritmi genetici per Problemi Vincolati**
**vincolato** = ho uno spazio di ricerca ottenuto partendo da uno spazio di ricerca più ampio e poi **elimando** alcune soluzioni.

***Spazio di ricerca***: <br>
X = {x ∈ Y: x soddisfa una condizione C} <br>
Y spazio di ricerca più grande.

Esempio: <br>
***0-1 Knapsack***
- n **oggetti** 1, 2, . . ., n
- ogni oggetto ha un **peso** w1, w2, ..., wn
- ogni oggetto ha un **valore** v1, v2, ..., vn
- **Zaino** con **capacità** C in kg

L'obiettivo è trovare la composizione ottimale: <br>
**Seleziona qualche oggetto tale che la somma dei pesi(sommatoria pesi) è <= C e la somma dei valori (sommatoria valori) è massima.**

È possibile ricondurre questo problema ad un problema binario. <br>
Rappresentazione come un vettore binario x1, x2, ... , xn

![01zaino](./imgs/01zaino.png) <br>
(st = such that)

Tutte le stringhe di n-bit possono essere **ammissibili** <br>
![01zaino1](./imgs/01zaino1.png)

o **non ammissibili**: <br>
![01zaino2](./imgs/01zaino2.png)

In generale una soluzione per un problema vincolato **è ammissibile se rispetta i vincoli**.

## **Penalizzazione e Riparazione**
Negli algoritmi genetici si hanno due possibilità per quanto riguarda le soluzioni da considerare nella popolazione:
- **Non ammettere soluzioni non ammissibili nella popolazione**.
    1. Serve un meccanismo che quando inizializza la popolazione, crea solo soluzioni ammissibili
    2. Il crossover e la Mutazione devono generare solo funzioni ammissibili
    
    Ci sono problemi di ottimizzazione in cui è difficile perfino creare soluzini ammissibili ed **è ancora più difficile garantire che crossover e mutazione producano soluzioni ammissibili**.

    Si consideri che il 1-point crossover non funziona sulle permutazioni.

    Vediamo come è possibile invece risolvere il problema del knapsack con un algoritmo genetico.
- **Ammettere soluzioni non ammissibili**. <br>
    Una soluzione non ammissibile è una soluzione che non risolve il problema, tuttavia potrebbe non essere lontana dall'essere ammissibili. Di conseguenza valuto quanto è lontana dall'essere ammissibile e, valuto anche quello. <br>
    funzione obiettivo (come **fitness**) -> invece di fare max f(x), faccio max f(x) - k * p(x) <br>
    dove p rappresenta la penalità. <br> <br>
    p(x) = 0 se x è ammissibile <br>
    altrimenti p(x) quantifica "*quanto x è distante dall'essere ammissibile*". <br>
    ![01zaino3](./imgs/01zaino3.png)

    Nel problema dello zaino: <br>
    ![01zaino4](./imgs/01zaino4.png)

    La valutazione della funzione obiettivo è quella considerando la penalità.

Per implementare il secondo approccio, è necessario utilizzare:
- problem.objective_function(x) - penality_coefficient * problem.penalization(x) <br>
    per valutare gli individui della popolazione.

k = penality_coefficient, deve essere grande abbastanza per far si che la penalità sia minore del minimo valore di f(x), quando x è ammissibile. <br>
![01zaino5](./imgs/01zaino5.png) <br>
In altre parole x è sempre meglio di y (una soluzione ammissibile è sempre meglio di una soluzione non ammissibile).

Ricordare che la **fitness function** utilizzata ad esempio nella roulette wheel deve essere positiva (aggiungere una costante a f(x) segnato).

Il principio dietro la penalizzazione è che all'inizio le soluzioni potrebbero essere tutte non ammissibili, ma pian piano emergono soluzioni ammissibili. Le soluzioni ammissibili diventano sempre più presenti nella popolazione, perchè l'algoritmo genetico privilegia le soluzioni ammissibili nella popolazione e prova a ridurre il "gap di non aamissibilità" (penalità). <br>
Questo metodo si può sempre utilizzare per risolvere problemi di ottimizzazione vincolati. I due criteri generali sono:
1. Definisci una funzione di penalizzazione per quantificare la non ammissibilità (ovvero per valutare soluzioni ammissibili)
2. Trovare il valore per **k**

Tuttavia, è necessario calcolare **f anche se x non è ammissibile**. Quando questo non è possibile, si può definire così:<br>
![01zaino6](./imgs/01zaino6.png) <br>
Non è possibile calcolarlo quando ad esempio f non è definito. <br>
***Es.*** <br>
x deve essere diverso da 0. Che succede se x è 0 ? È un vincolo e in questo caso f non è calcolabile.

Questo non è l'unico modo, c'è un altro approccio: **riparare le solzuzioni non ammissibili**. <br>
**Riparare** = utilizzare un metodo che parte da una soluzione non ammissibile y e produce una soluzione ammissibile x, effettuando il minor numero possibile di modifiche su y. <br>
![01zaino7](./imgs/01zaino7.png)

Nell'inizializzazione:
```pseudocode
for N individuals
    generate a random solution
    if not feasible, repair it
    evaluate it
```
Nel ciclo principale si ha uno step in più (riparazione):
```pseudocode
    CROSSOVER
    MUTATION
    REPAIR IF UNFEASIBLE
    EVALUATION
```

### ***Come si fa a riparare una soluzione nel problema dello zaino?***
Per il problema dello zaino, un meccanismo di riparazione ragionevole (basso costo computazionale) per le soluzioni non ammissibili x:
1. Rimuovi alcuni oggetti da x, finchè x non diventa ammissibile <br>
    ![01zaino8](./imgs/01zaino8.png) <br>
    Posso scegliere gli oggetti da rimuovere secondo diversi criteri (randomico, secondo un ordine, rapporto peso/valore ecc...)
2. Aggiungi alcuni oggetti a x, fintanto che x rimane ammissibile.

**Il meccanismo di riparazione** dipende dal problema (dipende dalla forma dei vincoli). <br>
Definire un operatore di riparazione è molto più difficile dello scrivere una funzione di penalizzazione.

#### **Confronto tra i due metodi (penalizzazione e riparazione):**
- La penalizzazione porta il GA a cercare soluzioni ammissibili (che possono, soprattutto inizialemnte, non esserlo). Le generazioni sono più veloci.
- La riparazione porta il GA a lavorare sempre con soluzioni ammissibili (minor spreco di calcolo per effettuare generazioni, in quanto ne vengono effettuate di meno. Tuttavia può essere più pesante dal punto di vista computazionale l'effettuare le riparazioni)

![01zaino9](./imgs/01zaino9.png) <br>
![01zaino10](./imgs/01zaino10.png) <br>

Ci sono anche altre alternative alla riparazione e alla penalizzazione: <br>
**Scartare le soluzioni non ammissibili**: nell'inizializzazione, ogni volta che genero una soluzione non ammissibile, la rigenero. Quando crossover e mutazione producono una soluzione non ammissibile, non la metto nella lista dei children.

Nella fase di inizializzazione si looppa finche N soluzioni ammissibili non vengono create (non strettamente necessario). <br>
Nel main loop non vengono memorizzate soluzioni non ammissibili nella lista dei children.

La penalizzazione ritiene che tutti gli individui siano utili nell'evoluzione, anche quelli non ammissibili. In quanto è possibile trovare soluzioni ammissibili partendo da soluzioni non ammissibili.

<hr>

## **Algoritmi evolutivi per l'ottimizzazione continua**
**continua** = opposto di discreta

Objective function <br>
![es1](./imgs/es1.png)

L'obiettivo è (come per l'ottimizzazione discreta) trovare **x*** **∈ D tale che f(x*** **) è massimo (o minimo)**.

Un elemento di D è un elemento di **d** numeri reali.

Per usare un algoritmo genetico è possibile discretizzare il problema, utiizzando **p** bits per rappresentare un numero reale. Quindi una soluzione potrebbe essere rappresentata come stringa di **p x d** bits. <br>
In linea teorica è quindi possibile applicare un algoritmo genetico per ottimizzare f.

L'ottimizzazione di una funzione continua è più facile in generale rispetto ad ottimizzare una funzione discreta. <br>
***Come mai?*** <br>
Matematicamente, se io mi muovo in uno spazio continuo e sono in x, se mi muovo di un Δ piccolo: <br>
from x to x + Δx <br>
f(x) -> f(x + Δx) ≈ f(x)<br>
La differenza |f(x+ Δx) - f(x)| può essere **piccola**

***Perche è più facile?***:
- **Prima motivazione**: <br>
    se f è differenziabile, è possibile utilizzare algoritmi molto efficienti di ottimizzazione, basati sul **gradiente** di f (gradiente = vettore delle derivate).<br>
    **Il gradiente di f in un punto x ∈ D da un'informazione su quale è la direzione in cui la f cresce e decresce.** <br>
    Calcolare il gradiente aiuta gli algoritmi, in quanto quest'ultimi sono guidati dal gradiente. <br>
    L'algoritmo più famoso basato sul gradiente è: "**L'algoritmo di discesa del gradiente**" (per la minimizzazione -> è utilizzato per allenare le reti neurali). <br>
    Esistono anche molti altri algoritmi basati sulle derivate. Tuttavia questi algoritmi trovano sempre un **minimo locale**, perchè questi algoritmi nel minimo locale hanno gradiente = 0. <br>
    ![es2](./imgs/es2.png) <br>
- **Seconda motivazione**: <br>
    Ci sono degli algoritmi di ottimizzazione chiamati "***derivative-free***", i quali possono trovare il minimo o massimo globale di f in modo efficiente. Esempi (già implementati nella libreria **scipy** di python):
    - Nelder-mead;
    - Poquel;
    - LBFGS;
    - ecc...

#### **Differenza tra spazio discreto e spazio continuo**
![es3](./imgs/es3.png)

### **Risultati di Complessità** per cui l'ottimizzazione discreta è più difficile di quella continua
Se f è lineare e D è definito in termini di vincoli lineari, il problema di ottimizzare f si chiama problema di programmazione lineare. <br>
- Per spazi discreti, è un problema NP-HARD. <br>
- Per spazi continui, c'è un algoritmo che risolve il problema in tempo polinomiale.

L'utilizzo di algoritmi genetici e altri algoritmi evolutivi per l'ottimizzazione continua è giustificata nelle seguenti situazioni:
1. Ci sono dei problemi dove gli algoritmi evolutivi trovano soluzioni migliori rispetto agli algoritmi classici. Questo per esempio per problemi in cui la funzione obiettivo f ha molti minimi (o massimi) locali. Oppure quando l'obiettivo non è trovare più minimi (o massimi).
2. Quando f non è esattamente una funzione continua. Ci sono due possibilità:
    - La funzione ha dei punti di discontinuità -> **Discontinuità**. <br>
    ![es4](./imgs/es4.png) <br>
    - f può essere scritta in termini di variabili continue e variabili discrete -> **Ibrido: variabili continue e discrete**<br>
    ![es5](./imgs/es5.png)

Altre situazioni in cui sono utilizzati gli algoritmi evolutivi in problemi di ottimizzazione continua:
1. f è dinamica -> f cambia nel tempo -> **Dinamicità**
2. f è alterata dal rumore esterno (la f quando viene valutata non è esatta, potrebbe quindi succedere che valutando la f nello stesso punto ritorna valori diversi. Un algoritmo traduzionale non riuscirebbe ad andare avanti o ad esempio calcolarsi il gradiente, a differenza degli algoritmi evolutivi.) -> **Casualità**

## **Strategie evolutive**
### **(1+1)-ES**
```pseudocode
    x <-- random point in D
    for g <-- 1 to max_gen
        ε <-- random vector of dimension d
        x' <-- x + ε    # è una sorta di mutazione
        z' <-- f(x')
        if z' <-- z
            x <-- x'
            z <-- z'
    return x, z
```
***Come viene generato il vettore ε ?*** <br>
ε può essere generato usando una distribuzione normale di dimensione d. <br>
![es6](./imgs/es6.png) <br>
![es7](./imgs/es7.png) <br>
![es8](./imgs/es8.png)

Tutte le componenti di ε sono indipendenti (le estraggo indipendentemente dalle altre). <br>
Per estrarre ε si può fare così:
```python
    eps = np.zeros(d)
    for in range(0,d):
        eps[i] = random.normal(0, sigma2)
```
Lo schema evolutivo precedenete non fa utilizzo di una popolazione. <br>
La **popolazione** può essere introdotta dal seguente schema di generalizzazione:
### **(λ, μ)-ES**
**λ = dimensione della popolazione** <br>
**μ = numero di figli** <br>
λ > μ
```pseudocode
    for i <-- 1 to λ
        generate xi
    for g <-- 1 to max_gen
        for i <-- 1 to μ
            generate x'i by manipulating some xj
        select the best λ individuals among the children as new value x1, ..., xλ for next iteration # Non c'è elitismo
    return the best individuals ever found 
```

Un'altra alternativa è di utilizzare:
### **(λ + μ)-ES**
La selezione prende i migliori λ individui tra i genitori e i figli.
- λ = 1 e μ = 1 --> **(1+1)-ES** <br>
- λ > 1 e μ = 1 --> **mutare un individuo tra la popolazione** o scelto secondo qualche 
criterio come tornei o roulette wheel. <br>
    L'unico figlio può sostituire il peggiore della popolazione.
- λ > 1 e μ > 1 --> **caso generale** <br>

Parametri di una ES (evolutionary strategies):
- λ
- μ
- σ^2 (o in generale Σ)

Le strategie evolutive possono usare anche meccanismi per adattare σ^2 o farlo evolvere:
- **rule 1/5** : adatta σ in modo da mantenere la percentuale di **mutazione con successo** intorno a 1/5 <br>
    Mutazione con successo = genero un individuo che è migliore. La mutazione se io genero un x' la cui f è migliore di x.
- Un'altra tecnica è assegnare ad ogni individuo un valore per σ <br>
    ![es9](./imgs/es9.png)

### **CMA-ES**
È una delle strategie evolutive più performanti. <br>
Non fa utilizzo della popolazione, al suo posto fa uso di un modello probabilistico. <br>
Invece di generare μ figli dalla popolazione (ad esempio tramite mutazione), i figli sono campionati dal modello M.

Il modello probabilistico utilizzato è un modello Gaussiano (utilizza la distribuzione normamle) con **n** come vettore delle medie.

### **CMA-ES abstract scheme**
```pseudocode
    genera i valori iniziali per i parametri di M
    for g <-- 1 to max_gen
        genera μ individuo da M     # utilizzare un generatore di numeri pseudo casuali da M e estrarre μ individui x1, ... , xμ
        scegliere i migliori λ individui
        usare x(1), ... , x(λ) per aggiornare i parametri di M
    return il miglior individuo
```
Aggiornare i parametri di M dovrebbe produrre individui sempre migliori (non è certo). L'idea è che l'aggiornamento dovrebbe spingere sia la media che la varianza della popolazione verso individui buoni.
