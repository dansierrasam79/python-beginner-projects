A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
C = {10, 20}
D = {30, 40}
E = {10, 50}
S1 = {1, 2}
S2 = {1, 2, 3, 4}

# Using the Operator
union_set_operator = A | B
print(f"Union (Operator |): {union_set_operator}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Using the Method
union_set_method = A.union(B)
print(f"Union (Method union()): {union_set_method}") # Output: {1, 2, 3, 4, 5, 6, 7, 8}

# Using the Operator
intersection_set_operator = A & B
print(f"Intersection (Operator &): {intersection_set_operator}") # Output: {4, 5}

# Using the Method
intersection_set_method = A.intersection(B)
print(f"Intersection (Method intersection()): {intersection_set_method}") # Output: {4, 5}

# Elements in A but NOT in B
difference_A_B = A - B
print(f"A Difference B: {difference_A_B}") # Output: {1, 2, 3}

# Elements in B but NOT in A
difference_B_A = B.difference(A)
print(f"B Difference A: {difference_B_A}") # Output: {8, 6, 7}

# Using the Operator
sym_diff_operator = A ^ B
print(f"Symmetric Difference (Operator ^): {sym_diff_operator}") # Output: {1, 2, 3, 6, 7, 8}

# Using the Method
sym_diff_method = A.symmetric_difference(B)
print(f"Symmetric Difference (Method): {sym_diff_method}") # Output: {1, 2, 3, 6, 7, 8}

# issubset()
print(f"Is S1 a subset of S2? {S1.issubset(S2)}") # Output: True

# is_proper_subset (Note: use operators for strict checks)
print(f"Is S1 a proper subset of S2? {S1 < S2}") # Output: True

# issuperset()
print(f"Is S2 a superset of S1? {S2.issuperset(S1)}") # Output: True

# is_proper_superset
print(f"Is S2 a proper superset of S1? {S2 > S1}") # Output: True

# C and D have no common elements
print(f"Are C and D disjoint? {C.isdisjoint(D)}") # Output: True

# C and E have '10' in common
print(f"Are C and E disjoint? {C.isdisjoint(E)}") # Output: False
