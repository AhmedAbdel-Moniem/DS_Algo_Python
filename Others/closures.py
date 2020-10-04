# Factory Functions & Closures
def maker(N):
	def action(X):
		return (N**X)
	return action

f = maker(2) # factory function one
print(f)
print(f(2))
print(f(3))

g = maker(3) # factory function two
print(g)
print(g(2))
print(g(3))

print('\nEnclosing scopes are often using LAMPADAS:\n')
# Enclosing scopes are often using LAMPADAS
def maker(N):
	return lambda X: X**N
h = maker(2)
print(h)
print(h(2))