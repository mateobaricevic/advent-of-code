import re

input = open('input.txt').readlines()
rules = {}
words = []
for l in input:
    if ':' in l:
        m = re.findall(r'[\dab|]+', l)
        rules[m[0]] = m[1:]
    elif len(l):
        words.append(l.strip())

def x(n):
    if n == '|': return n
    if n == '8': return '(?:%s)+' % x('42')
    if n == '11': return '(?:%s)' % '|'.join(map(lambda c: x('42') * c + x('31') * c, range(1, 11)))
    r = rules[n]
    if not r[0].isdigit(): return r[0]
    return '(?:%s)' % ''.join(map(x, r))

rx = re.compile(x('0'))
print(sum(1 for w in words if rx.fullmatch(w)))