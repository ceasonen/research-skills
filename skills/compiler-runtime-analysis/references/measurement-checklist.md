# Compiler Measurement Checklist

Before attributing a speedup to the compiler, check:

1. identical inputs and shapes
2. warmup and cache effects
3. compilation time versus execution time
4. autotuning cost and reuse policy
5. backend library versions
6. generated code or IR differences
7. host-device transfer path
8. fusion side effects on memory usage
9. correctness on edge-case shapes
10. variance across repeated runs
