# RTL Checklist

## Interface

1. widths and signedness are explicit
2. valid-ready or request-ack semantics are defined
3. reset values are documented
4. illegal states are described

## Sequential Logic

1. nonblocking assignments in clocked logic
2. blocking assignments only in combinational code
3. no accidental latches
4. counters and pointers have wrap behavior defined

## Clocks And Reset

1. every register has one clock owner
2. async reset use is intentional
3. reset release is safe in each domain
4. CDC paths are named and justified

## Memories And FIFOs

1. read and write latency is modeled
2. inferred RAM style matches the target toolchain
3. full and empty conditions are test-covered
4. initialization semantics are not assumed silently

## Testbench

1. include nominal, boundary, and illegal cases
2. check latency and ordering, not just values
3. assert handshake invariants
4. add randomized backpressure if applicable

## Tooling

If tools exist, prefer this order:

1. syntax or lint
2. focused simulation
3. synthesis sanity check

Report tool absence separately from design correctness.
