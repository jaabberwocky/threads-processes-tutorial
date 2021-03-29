# Tutorial

## Points to note

### Threading:
1. New thread is spawned within existing process
2. Starting a thread is faster than starting a process
3. Memory is shared across all threads
4. Mutexes often necessary to control access to shared data
5. One GIL

### Multiprocessing:
1. A new process is started independent from first process
2. Starting a process is slower than starting a thread
3. Memory is not shared between processes
4. Mutexes not necessary
5. One GIL