def is_word_chain(words):
    chained = True
    for i in range(len(words) - 1):
        if words[i][-1] != words[i+1][0]:
            chained = False
    return f"Is chained: {chained}"

print(is_word_chain(['bake', 'eggs', 'snack', 'karat', 'tuna']))
print(is_word_chain(['sycamore', 'elon', 'nonutnovember', 'ricegum', 'maxxis']))
print(is_word_chain(['apple', 'egg', 'snack', 'karat', 'tuna']))