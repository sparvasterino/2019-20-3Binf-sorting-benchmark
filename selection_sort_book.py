from timeit import time

def selection_sort(mylist):
    # Mi riscrivo una funzione che trova il minimo di una lista
    def mymin(list):
        m_idx = 0
        m = list[0]
        for n_idx, n in enumerate(list):
            if n.author < m.author:
                m = n
                m_idx = n_idx
        return m, m_idx

    # Algoritmo di ordinamento
    #print("lista prima:")
    #print(mylist)
    start_time = time.time()
    for idx in range(len(mylist)):
        # compute minimum and the index relative to the slice
        m, m_idx = mymin(mylist[idx::])
        # convert relative index into global index
        m_idx += idx
        swap = mylist[idx]
        mylist[idx] = m
        mylist[m_idx] = swap
        
    stop_time = time.time()
    print(f"{(stop_time-start_time):.7f}")


    # Stampo la lista appena calcolata
    #print("lista dopo:")
    #print(mylist)

    return (stop_time-start_time)

   
