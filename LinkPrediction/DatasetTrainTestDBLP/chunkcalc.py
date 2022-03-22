1348332879858

def calc_chunksize(n_workers, len_iterable, factor=8):
    """Calculate chunksize argument for Pool-methods.

    Resembles source-code within `multiprocessing.pool.Pool._map_async`.
    """
    chunksize, extra = divmod(len_iterable, n_workers * factor)
    if extra:
        chunksize += 1
    return chunksize

print(calc_chunksize(8,80367))