import copy

list04 = list()
print(list({1,2,3}))

a = set(range(3))
print(f'id {id(a)}')
a.add(range(4, 6))
print(f'id추가 {id(a)}')

a = list(range(2))
print(f'python + {id(a)}')
a = list(range(5))
print(f'python2 + {id(a)}')

a = print([1]*5)

print(1,2)
print((1,2))
a = 1,
print(a)
print((1,))
a = list(range(3))
b = ((a,2))
print(id(b))
a.append(3)
print(id(b))
print((a, 2))
print(('23121', 2))
print({tuple(range(2)), 2,3, 'er'})

a = list(range(3))
b, c, d = a
for alphabet in [b, c, d]:
    print(alphabet)
    
a = list(range(8))
print(id(a))
print(a[5:2])
# a = (b = 1)

print(a)
print(b)

print([1,2,3] > [1,2,3,4])

print([1,2,3] < [5,1,1])

a = list(range(3))
b = list(range(5))
print("여기")
a = tuple(range(5))
print(id(a))
a += (1,3)
print(id(a))
print(a[0])


a = [1,3,2,5,2,1,8,2,9,22,45,64,3,2,4]
max = a[0]
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
print(max)

