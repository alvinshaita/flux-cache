import hashlib
import pickle

def generate_cache_key(func, args, kwargs):
	key_data = (func.__module__, func.__name__, args, kwargs)
	raw_data = pickle.dumps(key_data)
	return hashlib.sha256(raw_data).hexdigest()


def one():
	return "one"


def two():
	print(one())
	return "two"