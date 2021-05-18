"""import multiprocessing as mp

def affich(num):
    print('bonjour', num)

if __name__ == "__main__":
    n = 5
    process = mp.Process(target = affich, args=(n,))
    process.start()
    process.join()
    print("process actif ? ", process.is_alive())"""

from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=f, args=('bob',))
    p.start()
    p.join()