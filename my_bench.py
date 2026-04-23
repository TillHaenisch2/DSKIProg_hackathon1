import bench
import matplotlib.pyplot as plt

# Sammle Ergebnisse
results = {}

for N in (100,500,1000, 2000):
    bench.do_run("random", "built_in", "simple_show", N)
    bench.do_run("random", "bubblesort", "simple_show", N)
