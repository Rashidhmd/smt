# Symbolic AI and SMT solving

Symbolic AI is an approach to Artificial Intelligence that relies on deductive reasoning to produce exact, explainable solutions to well-defined problems. This contrasts with sub-symbolic methods (e.g., machine learning, NNs, and LLMs), which use statistical learning to address a wide range of (possibly vaguely defined) tasks, producing plausible but not always correct results that are typically hard to explain. Integrating symbolic and sub-symbolic techniques is a hot topic in AI (neuro-symbolic AI).

SMT (Satisfiability Modulo Theories) solvers are automated tools for reasoning about and rigorously solving problems involving arithmetic, arrays, bit vectors, and more. They are widely used in industrial settings for tasks such as program verification, planning, and testing.

In this seminar, we introduce Z3, an efficient and user-friendly SMT solver developed by Microsoft. We will compare it to both hand-written algorithms and LLM-based approaches on a simple illustrative problem, such as solving a Sudoku. Then, we will show how SMT solving can be used for program verification (i.e., checking whether a program satisfies a given specification), discussing some applications in smart contract security.

Throughout the seminar, students will actively engage with the material by working on a series of simple, guided exercises that will be assigned during the session, allowing them to experiment directly with the tool and reinforce the concepts discussed.


## Exam

Solve this [problem](Exercises/Exam.py) using z3. Submit your solution through this [form](https://forms.gle/LLEMJDBheKmvUrw4A).


## Requirements

Install z3 Python APIs through pip: 
```pip3 install z3-solver```

[z3Py Tutorial](https://ericpony.github.io/z3py-tutorial/guide-examples.htm)

[Programming z3](https://theory.stanford.edu/~nikolaj/programmingz3.html)

## Content
- [Material](Material/)
    - [01 - Basics](Material/01_Basics.py)
    - [02 - Proofs and Counterexamples](Material/02_Certificates.py)
    - [03 - Optimization and Model Counting](Material/03_Optimization.py)
    - [04 - Bounded Model Checking](Material/04_BoundedModelChecking.py)
    - [05 - Quantifiers](Material/05_Quantifiers.py)
- [Exercises](exercises/): one file per each file in Material, with exercises of increasing difficulty



## References

- C. Barrett, R. Sebastiani, S. Seshia, C. Tinelli: [Satisfiability Modulo Theories](https://link.springer.com/chapter/10.1007/978-3-319-10575-8_11), 2018
- L. de Moura, N. Bjørner: [Z3: An Efficient SMT Solver](https://link.springer.com/chapter/10.1007/978-3-540-78800-3_24), 2008
- A. Biere, D. Kröning:  [SAT-Based Model Checking](https://link.springer.com/chapter/10.1007/978-3-319-10575-8_10), 2018
- A. Biere, M. Heule, H. Van Maaren, T. Walsh: [Handbook of Satisfiability](https://www.iospress.com/catalog/books/handbook-of-satisfiability-2), 2021
- J. Aldrich: [Lecture Notes on Satisfiability Modulo Theories](https://www.cs.cmu.edu/~aldrich/courses/17-355-19sp/notes/notes12-smt.pdf), 2019
- M. Fredrikson: [Lecture Notes on Bounded Model Checking](https://www.cs.cmu.edu/~15414/s22/lectures/17-bmc.pdf), 2022
