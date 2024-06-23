from random import sample

# Constants
num_students    = 12000
address_space   = 15000
# address_space   = 15013

# Generate 12,000 unique student IDs(assuming IDs are integers for simplicity)
student_ids = sample(range(1, 20000), num_students) # ensure unique IDs

def hash_function(id, N):
    return id % N 

# Apply the hash function and store in hash table
hash_table = [0] * address_space
collisions = 0

for student_id in student_ids:
    hash_value = hash_function(student_id, address_space)
    if hash_table[hash_value] == 0:
        hash_table[hash_value] = 1
    else:
        collisions += 1 

print(collisions)