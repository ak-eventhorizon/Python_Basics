def solve(s):
    return ' '.join([word.capitalize() for word in s.split(' ')])


print(solve('john  q  smith green 12abc'))
print(solve('q w e r t y u i o p a s d f g h j  k l z x c v b n m Q W E R T Y U I O P A S D F G H J  K L Z X C V B N M'))
