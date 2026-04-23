# standard plugins

from bench import add_algo, add_data_generator, add_result_display, do_run


add_algo("built_in", sorted)
add_data_generator("random", lambda n: [random.randint(0, n-1) for _ in range(n)])
add_result_display("simple_show", lambda name, N, ncomp, rtime: print(f"{name} with {N} data points runs for {rtime}msec and needs {ncomp} comparisons"))