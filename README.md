# gravityai-isprime
Prime Number Testing for Gravity AI
- https://www.gravity-ai.com/dashboard/project-version/0b14440f-761a-436b-8fe9-f04f487cd6ae/b5552f48-e594-4b84-a1e4-28d23a913d50

## CLI Interface

Setup
``` 
pip-compile -v
pip3 install -r requirements.txt
python3 -m pytest -v .
```

Runtime
```
./gravity_is_prime.py.py run ./csv/is_prime/input.csv ./csv/is_prime/output.csv 
```

## Implementation

> Test if n is a prime number (True) or not (False). For n < 2^64 the answer is definitive; larger n values have a small probability of actually being pseudoprimes.
>
> Negative numbers (e.g. -2) are not considered prime.
>
> The first step is looking for trivial factors, which if found enables a quick return. Next, if the sieve is large enough, use bisection search on the sieve. For small numbers, a set of deterministic Miller-Rabin tests are performed with bases that are known to have no counterexamples in their range. Finally if the number is larger than 2^64, a strong BPSW test is performed. While this is a probable prime test and we believe counterexamples exist, there are no known counterexamples.
>
> - https://docs.sympy.org/latest/modules/ntheory.html?highlight=prime#sympy.ntheory.primetest.isprime

## Questions 
- How should data validation / invalid data be handled?
- Should True/False or 0/1 be used for boolean output?