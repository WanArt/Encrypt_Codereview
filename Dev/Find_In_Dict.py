# Получить ключ по значению
def get_symbol(sl, val):
    for a, b in sl.items():
        if val == b:
            return a
