# Bring-Up Checklist

## Reproduction Facts

1. board revision
2. power source
3. oscillator or PLL setup
4. firmware commit
5. compiler and optimization flags

## Early Boot

1. reset cause
2. stack and heap placement
3. vector table
4. clock tree
5. watchdog behavior

## Peripheral Debug

1. pin mux and alternate function
2. peripheral clock enable
3. interrupt routing and priority
4. DMA ownership and cache coherency
5. timeout and retry behavior

## Concurrency

1. ISR versus task ownership
2. volatile and atomic correctness
3. lock ordering
4. buffer lifetime
5. stack depth

## Best Next Probe

Choose one:

1. register dump
2. timestamped trace
3. minimal loopback test
4. power or clock measurement
5. single-feature firmware build

Prefer the next probe that most cleanly separates firmware causes from hardware causes.
