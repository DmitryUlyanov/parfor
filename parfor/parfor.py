from functools import wraps
from joblib import Parallel, delayed
from tqdm import tqdm

def parfor(original_function=None, *, n_jobs=1, backend=None):
    """ 
    """
    def _decorate(function):
        
        @wraps(function)
        def my_func(itrable, *args, **kwargs):
            return Parallel(n_jobs=n_jobs, backend=backend)(delayed(function)(data, *args, **kwargs) for data in tqdm(itrable))

        return my_func
    
    if original_function:
        return _decorate(original_function)
    
    return _decorate