import collections

slist = ["eat", "tea", "ate", "nat", "bat"]

sdict = collections.defaultdict(list)

for i in slist:
    sdict["".join(sorted(i))].append(i)

ret = sdict.values()

print(list(ret))
print(type(ret))




