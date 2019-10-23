def store(a):
    res = ""
    for ele in a:
        if type(ele) is dict:
            for k in ele.keys():
                res = res + str(k) + "=" + str(ele[k]) + ";"
        res = res[:-1]
        res = res + r"\n"
    return res

def load(a):
    res = []
    ds = a.split(r"\n")
    for ele in ds:
        if ele != "":
            temp = dict()
            data = ele
            if ";" in ele:
                data = ele.split(";")
                for d in data:
                    key,value = d.split("=")
                    temp[key] = value
            else:
                key,value = data.split("=")
                temp[key] = value
            res.append(temp)
    return res

if __name__ == '__main__':
    a = [{"key1": "value1", "key2": "value2"}, {"keyA": "valueA"}]
    text = store(a)
    array = load(text)
