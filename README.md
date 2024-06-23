# Hashing Scheme Design

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![image](https://img.shields.io/badge/windows%20terminal-4D4D4D?style=for-the-badge&logo=windows%20terminal&logoColor=white)

Author: [Andrew Gyakobo](https://github.com/Gyakobo)

In this project I'll try to demonstrate a hashing scheme for storing and retrieving data.   

## Introduction

Hearkening from the introduction, we'll be designing a *hash function* which would take in a variety of keys with little to no collision errors between the keys.  

## Methodology

To start off, we'll use a hash function based on a combination of division and multiplication methods. The division method ensures we stay within the address space, and the multiplication method helps distribute the hash values more uniformly.

Hash Function:
$$ h(k) = \lfloor m * (k * A \bmod 1) \rfloor $$

## License
MIT