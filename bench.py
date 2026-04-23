import random
from TrackedValue import TrackedValue
from time import perf_counter

# plugin based test bench for evaluating runtime complexity of sorting algorithms

# user can supply plugins to evaluate algorithm implementations, plugins to create data 
# and plugins to display the benchmark results
# 
# plugins are implemented as functions with a defined interface.

# we use a global table with all plugins, containg their names, 
# a function pointer and some other stuff

# Plugin types
PLG_ALGO = 1  # plugin for sorting algorithm implementation
PLG_DATA = 2  # plugin for creating data to be sorted
PLG_SHOW = 3  # plugin for showing the results of the benchmark

_functions = []

# a few example plugins for testing
def bench_test(data):
  return sorted(data)

def bench_data(N):
  return [random.randint(0,N-1) for l in range(N)]

def bench_show(name, N, ncomp, rtime):
  print(f"{name} with {N} data points runs for {rtime}msec and needs {ncomp} comparisons")

# decorator for plugins
def do_bench(name,data_list):
  stats = {'comparisons': 0}
  func=find(_functions,name,PLG_ALGO)
  # Daten einhüllen, bevor sie an den Studi-Code gehen
  tracked_data = [TrackedValue(x, stats) for x in data_list]
  # Aufruf der Plugin-Funktion
  start = perf_counter()
  func(tracked_data) # type: ignore
  end = perf_counter()

  #print(f"Algorithmus: {name} | Vergleiche: {stats['comparisons']}") # type: ignore
  #return tracked_data
  return [stats['comparisons'], round(1000*(end - start))]

# helper function to find a plugin by name and type
def find(l,name,type):
  found=[f for f in _functions if (f["name"] == name and f["type"] == type)]
  if (len(found) == 1):
    return found[0]["func"]
  else:
    return None


def add_algo(name, func):
  _functions.append({"name":name, "func":func, "type":PLG_ALGO})

def add_data_generator(name, func):
  _functions.append({"name":name, "func":func, "type":PLG_DATA})

def add_result_display(name, func):
  _functions.append({"name":name, "func":func, "type":PLG_SHOW})


def do_run(data_gen_name, algo_name, show_name, N):
  data = (find(_functions,data_gen_name,PLG_DATA))(N) # type: ignore
  result = do_bench(algo_name, data)
  find(_functions,show_name,PLG_SHOW)(algo_name,N,result[0],result[1]) # type: ignore 

# standard plugins

add_algo("built_in", sorted)
add_data_generator("random", lambda n: [random.randint(0, n-1) for _ in range(n)])
add_result_display("simple_show", lambda name, N, ncomp, rtime: print(f"{name} with {N} data points runs for {rtime}msec and needs {ncomp} comparisons"))
# basic test of the core functionality

if __name__ == "__main__":
  print("AD-Bench - simple performance benchmarks for sorting algorithms")
  add_algo("bench_test", bench_test)
  add_data_generator("bench_data", bench_data)
  add_result_display("bench_show", bench_show)
  N=1000
  data = (find(_functions,"bench_data",PLG_DATA))(N) # type: ignore
  result = do_bench("bench_test", data)
  find(_functions,"bench_show",PLG_SHOW)("bench_test",N,result[0],result[1]) # type: ignore

  do_run("random", "built_in", "simple_show", 1000)





