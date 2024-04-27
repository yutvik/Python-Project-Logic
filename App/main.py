from timeit import timeit
                                                    # Performance and optimization
my_list = list(range(1_000_000))
my_set = set(range(1_000_000))

list_time = timeit('999_999 in my_list', number=1000,globals=globals())
print(f"List:{list_time:.6} seconds")

set_time = timeit("999_999 in my_set", number=1000, globals=globals())
print(f"Set:{set_time:.6f} seconds")

speed_diffrent = (list_time-set_time) / list_time * 100
print(f"{speed_diffrent:.3f}% faster")
