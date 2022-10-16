word = input()

not_spell = ['C','A','M','B','R','I','D','G','E']

for i in word:
    if i not in not_spell:
        print(i, end="")