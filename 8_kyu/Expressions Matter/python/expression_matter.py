def expression_matter(a, b, c):
    return max([(a + b)*c, a*(b + c), a + b*c, a*b + c, a*b*c, a + b + c])
