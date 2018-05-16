triangle=lambda n:(n*(n+1))//2
pentagonal=lambda n:(n*(3*n-1))//2
hexagonal=lambda n:(n*(2*n-1))

t_vals = set([triangle(i) for i in range(1,1000000)])
p_vals = set([pentagonal(i) for i in range(1,1000000)])
h_vals = set([hexagonal(i) for i in range(1,1000000)])

print(t_vals.intersection(p_vals).intersection(h_vals))



