# **Computational Intelligence**

## **Indice**
- [Informazioni sul corso](#informazioni-sul-corso)
- [Introduzione](#introduzione)
- [Problemi di ottimizzazione](#problemi-di-ottimizzazione)
    - [Categorie dei problemi di ottimizzazione](#categorie-dei-problemi-di-ottimizzazione)
- [Local search](#local-search)
    - [Number Partitioning Problem NPP](#number-partitioning-problem-npp)
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
    - [Applicazione al TSP](#applicazione-di-sa-al-tsp)
    - [Implementazione algoritmo Simulated Annealing](#implementazione-algoritmo-simulated-annealing)


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

### **Applicazione di SA al TSP**
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
