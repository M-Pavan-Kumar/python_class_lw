# def gen():
#     yield 1
#     yield 2
#     yield 3
#     yield 4
# res=gen()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

# def normal_func():
#     return 1
#     return 2
#     return 3
# print(normal_func())
# print(normal_func())


# def generate_num():
#     for i in range(1,10):
#         return i
# print(generate_num())

# def generate_num():
#     for i in range(1,10):
#         yield i
# res=generate_num()
# for num in res:
#     print(num)


# def normal():
#     return [i*i for i in range(1,10)]
# print(normal())

# def generator():
#     for i in range(1,10):
#         yield i*i
# res=generator()
# for num in res:
#     print(num,end=" ")

# Generator expression
# gen_expression=(i*i for i in range(1,10))
# print(gen_expression)
# for i in gen_expression:
#     print(i)


# Even numbers generator


# def even_gen(n):
#     for i in range(n):
#         if i%2==0:
#             yield i
# res=even_gen(11)
# for ev in res:
#     print(ev)


# Generator with return

# def gen():
#     yield 1
#     yield 2
#     yield 3
#     return 4
#     yield 5
#     yield 6
# res=gen()
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))

    