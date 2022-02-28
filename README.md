# **Computational Intelligence**

## **Indice**
- [Informazioni sul corso](#informazioni-sul-corso)
- [Introduzione](#introduzione)
- [Problemi di ottimizzazione](#problemi-di-ottimizzazione)
    - [Composizione di funzioni](#composizione-di-funzioni)
    - [Dichiarazione di funzioni](#dichiarazione-di-funzioni)
    - [Dichiarazioni locali di funzioni](#dichiarazioni-locali-di-funzioni)


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
- **simmetrico**: d(i,j) = d(j,i) $\forall$ *i*,*j* 
- **asimmetrico**: d(i,j) != d(j,i) esistono i e j che si verifica ciò (Esempio città in salita e discesa)
    - euclideo: d(i,j) = distanza(posizione città i, posizione città j) -> distanza euclidea (non realistica, realistica solo se la terra fosse piatta)

Il TSP è np-hard se visto come problema di ottimizzazione, oppure è np-complete come problema decisionale.

Definizione: Un problema di ottimizzazione è definito da:
- spazio di ricerca X
- funzione obiettivo f: X -> R (non necessariamente sarà sempre R)

Lo scopo è trovare il valore x* appartenente a X tale che f(x*) sia minimo (o massimo)

Nel problema del commesso viaggiatore:
- X è l'insieme di tutti i cicli Hamiltoniani del grafo
    - un ciclo Hamiltoniano è una sequenza di città che inizia da una città prestabilita c0, passa per tutte le città una sola volta e termina in c0.
    (trovare foto se riesco) <br>
    1 -3-4-2-6-5-1 nel grafo di prima
- La funzione obiettivo f è la distanza totale (o il costo) del ciclo Hamiltonino. <br>
    f(1-3-4-2-6-5-1) = d(1,3) + ecc...
    <br>
    x* è il ciclo Hamiltoniano con la minima distanza totale. Ciò lo rende un problema np-hard.

Trovare un ciclo Hamiltoniano è semplice se il grafo è completo. <br>
Computare f è facile (Calcolare f) <br>
La difficoltà sta nel trovare x* .

X è l'insieme di tutte le permutazioni delle città (dei nodi) (con la prima città che deve essere rimessa anche in fondo). 

In alcuni problemi anche generare un elemento di X può essere difficile (elemento di X = soluzione ammissibile).

Categorie dei problemi di ottimizzazione:
- Discreti (Es: TSP)
    - un problema di ottimizzazione è discreto quando X è un insieme finito
        - Se il grafo ha n città, ci sono (n-1)! cicli hamiltoniani
- Continui
    - X è un insieme infinito (Es: R o un intervallo)
        - Lo spazio di ricerca è costituito da numeri reali, vettori di numeri reali, matrici di numeri reali ecc
        - Es: determinare la posizione di n punti in modo tale da minimizzare la somma complessiva delle distanze da un determinato punto fissato. 

In un problema discreto ogni X(i) ha un dominio finito

In un problema continuo ogni X(i) ha un dominio infinito.
    - Esempio: ho una città e devo mettere delle stazioni di ricarica. Le devo mettere in modo tale che sia minima la somma complessiva delle distanze delle varie città in modo tale che un veicolo non deve fare troppa strata per potersi ricaricare.


Esistono altre categorie. <br>
Problemi di ottimizzazione.
- funzioni obiettivo lineari
    - f(xi, ...., xn) = w1x1+....+wnxn
    - Es funzione problema dello zaino
- funzioni obiettivo non lineari
    - f non è una combinazione lineare x1,...xn

Abbiamo poi:
- problemi vincolati:
    - X è ottenuto aggiungendo vincoli allo spazio di ricerca originale.
    - Es: lo zaino è un problema vincolato. Senza vincoli lo zaino è senza limiti e si prenderbbero tutti gli oggetti, ottenendo il massimo valore. Il problema dello zaino classico è quello vincolato (ogni oggetto ha un valore e un peso e lo zaino ha un limite)
    - X è ristretto

Abbiamo poi:
- problemi con singola funzione a obiettivo
- problemi con più funzioni obiettivo

Es: tsp con tempo e carburante come funzioni obiettivo (che in questo caso sono addirittura in competizione)

Il problema del commesso viaggiatore è un problema np-hard. 
Cosa fare se il problema di ottimizzazione è computazionalmente difficile?
1. Usare un algoritmo esatto (fattibile solo per piccole istanze)
    - All'aumentare dell'istanza anche di poco, i tempi di calcolo crescono esponenzialmente. Perche gli algoritmi sono solitamente esponenziali, al massimo polinomiali.
    - è possibile anche usare alcuni "universal solver". Ad esempio un sat solver, mip solver. Significa formulare il problema di ottimizzazione come un sat o un mixed integer probgramming. 
2. Approssimare il problema di ottimizzazione. Utilizzare un algoritmo approssimato.
    - Anziche trovare x* tale che f(x*) sia massimo o minimo, questi algoritmi trovano un x' tale che f(x') <= kf(x*)

Es: f(x*) = 300
x' ---> f(x') <= 2*300 <br>
Minore è k e meglio è

x' non è un minimo, è qualcosa che gli si avvicina ma quanto è lontano?

Per alcuni problemi di ottimizzazione k può essere scelto.

Per ottenere bassi valori di k è richeisto maggiore tempo.

Ci sono dei problemi di ottimizzazione in cui k non può essere scelto però. Non possono essere approssimati meglio di quel k.

3. Utilizzare una metaeuristica. Una metaeuristica è un algoritmo che da una soluzione del problema, la quale non è necessariamente ottima ma potrebbe essere molto buona, ottenuta soprattuto in un tempo ragionevole. Non c'è nessuna garanzia su quanto è buona la soluzione e non riesco a stimarlo. Questo è il prezzo da pagare per utilizzare una metaeuristica

Metaeuristica significa che la stessa tecnica può essere usata (adattandola) a un'ampia gamma di problemi di ottimizzazione.
    - Esempio: algoritmi genetici (risolvono problemi come lo zaino, il tsp, problemi di scheduling, problemi di ottimizzazione discreti , continui ecc...)
tecnica: È uno schema per un possibile algoritmo (ci sono dei buchi da riempire che dipendono dal problema e altri possono essere scelti dal programmatoree)

Molte metaeuristiche usano i numeri casuali (pseudo casuali). Significa che sono algoritmi randomizzati

```ocaml
Let rec gcd (m, n) = if n=m then n
    Else if n>m then gcd(n-m, m)
        else gcf(m, m-n) ;;
```
