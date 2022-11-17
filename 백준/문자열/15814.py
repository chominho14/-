word=list(input())
t=int(input())

for _ in range(t):
    a, b=map(int,input().split())
    word[a],word[b] = word[b],word[a]

print(''.join(word))


# word=input()
# t=int(input())

# for _ in range(t):
#     a, b=map(int,input().split())
#     temp=word[a]
#     word[a]=word[b]
#     word[b]=temp

# print(word)