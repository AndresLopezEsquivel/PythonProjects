# Higher order function
# Andrés López Esquivel

# A higher order functions receives or returns another function

# == EXAMPLE ONE ==

def f(g, a):
    new_a = [g(e) for e in a]
    return new_a


def cube(n):
    return n ** 3


array_one = [i for i in range(5)]

array_two = f(cube, array_one)

print('== EXAMPLE ONE ==')

print(f'array_one => {array_one}')

print(f'array_two => {array_two}')


# == EXAMPLE TWO ==


def html_tag(tag):
    def wrap_text(message):
        print('<{0}>{1}<\{0}>'.format(tag, message))
    return wrap_text


print_p_tag = html_tag('p')
print('== EXAMPLE TWO ==')
print_p_tag('This is a paragraph')