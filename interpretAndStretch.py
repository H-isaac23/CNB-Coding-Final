def interpretAndStretch(s):
    string = []
    eval_str = []
    multipliers = []
    nums = '0123456789'
    for x in s:
        if x in nums:
            multipliers.append(x)
        elif x == '[':
            string += x
        elif x == ']':
            while True:
                if string[-1] != '[':
                    eval_str.insert(0, string.pop())
                else:
                    string.pop()
                    string += eval_str*int(multipliers.pop())
                    eval_str = []
                    break
        else:
            string += x
    return ''.join(string)


print(interpretAndStretch('2[f2[g]h]'))
print(interpretAndStretch("3[f]2[gh]"))
print(interpretAndStretch("3[x2[y]]"))
print(interpretAndStretch("2[abc]3[cd]ef"))
print(interpretAndStretch( "abc3[cd]xyz"))