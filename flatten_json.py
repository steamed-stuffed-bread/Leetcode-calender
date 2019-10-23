def flatten_json(y):
    out = {}
    i = 0

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

if __name__ == '__main__':
    m = { "a": 1, "b": { "c": 2, "d": [3,4] }, "e": {"f": {"g": 5}, "h":6} } 
    print flatten_json(m)
