from cache import LRUCache

def test_cache_set_get():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    assert cache.get('Jesse') == 'James'


def test_cache_set_rem():
    cache = LRUCache(100)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.rem('Walter')
    print(cache.get('Walter'))
    assert cache.get('Walter') == ''

def test_cache_capacity_rem():
    cache = LRUCache(1)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    assert cache.get('Jesse') == ''

def test_cache_capacity_set():
    cache = LRUCache(1)
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    assert cache.get('Walter') == 'White'