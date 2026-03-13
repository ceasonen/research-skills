# Formal Checklist

## Separate These Three Things

1. environment assumptions
2. design assertions
3. cover properties

## Common Property Types

1. reset leads to a legal idle state
2. valid-ready handshakes never lose or duplicate data
3. FIFO pointers preserve ordering and bounds
4. arbiters maintain exclusivity
5. requests are eventually serviced when fairness assumptions hold

## Modeling Rules

1. keep assumptions minimal
2. make undefined inputs explicit
3. bound counters or memories only when justified
4. report any abstraction that can hide a bug

## Counterexample Triage

Check whether the trace indicates:

1. a real design error
2. an over-strong property
3. a missing environment assumption
4. an initialization mismatch between RTL and proof model
