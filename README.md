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

## Results and Analysis

When it comes to the results of this simulation I actually get total sum of 0 collisions which is just fantastic. I however decided to test the hash function on more IDs and realized that the collisions start to appear and amplify at this range [1, num_students + 3000] and onwards going. If I were to improve this algorithm I would change the given variables a bit to accommodate for the collisions. For instance, I would use a prime number modular divisor (something like 15013) for the hash function or lessen the spread of the random IDs.

## License
MIT