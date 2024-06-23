# Hashing Scheme Design

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

In this project I'll try to demonstrate a hashing scheme for storing and retrieving data.   

## Introduction

Hearkening from the introduction, we'll be designing a *hash function* which would take in a variety of keys with little collision errors between the keys. 

In our case we'll be working to retrieve student records (admissions creadentials, transcripts, degreeworks, etc.). We'll assume to have `12,000 students` and use an address space of `15,000`.

## Methodology

To start off, let's make our hash function. A straitforwared and commonly used method is the `Modular Division`: 

$$h(k) = k \bmod N $$

Where:
* $k$ is the student ID.
* $N$ is the address space `15,000`.

This method is simpler and more intuitive. We can then empirically test the number of collisions with this hash function.

1) To start off, I import the "sample" method from the random library in order to generate equidistant unique random IDs per the assignment's requirements. I then subsequently instantiate two constants: num_students and address_space 

```python
from random import sample

# Constants
num_students    = 12000
address_space   = 15000
```

2) Afterwards, I create all the student IDs with a random values which range [1, 12000]. I then create a "Modular Division" hash function as well as the hash table consisting of 15000 elements. Just to note, the hash function will compress each inputted key into the range of the address space [0, 15000] no matter whether an arbitrary key is bigger or smaller than the said address space.

```python
# Generate 12,000 unique student IDs
student_ids = sample(range(1, num_students), num_students) # ensure unique IDs

def hash_function(id, N):
    # N - address space
    return id % N 

# Apply the hash function and store in hash table
hash_table = [0] * address_space
```

3) Lastly, let's now test the program for any collisions. Simply put, we run a for loop to go through all the random generated IDs and check whether they were encountered before.

```python
collisions = 0
for student_id in student_ids:
    hash_value = hash_function(student_id, address_space)
    if hash_table[hash_value] == 0:
        hash_table[hash_value] = 1
    else:
        collisions += 1 

print(collisions)
```

## Results and Analysis

When it comes to the results of this simulation I actually get total sum of 0 collisions which is just fantastic. I however decided to test the hash function on more IDs and realized that the collisions start to appear and amplify at this range [1, num_students + 3000] and onwards going. If I were to improve this algorithm I would change the given variables a bit to accommodate for the collisions. For instance, I would use a prime number modular divisor (something like 15013) for the hash function or lessen the spread of the random IDs.

## License
MIT