#!/usr/bin/env python3
import sys
from collections import defaultdict

# Combiner to aggregate counts and sums locally
metrics = defaultdict(lambda: {"sum": 0, "count": 0})

def main():
    for line in sys.stdin:
        key, value = line.strip().split("\t")

        try:
            value = float(value)
            metrics[key]["sum"] += value
            metrics[key]["count"] += 1
        except ValueError:
            metrics[key]["sum"] += 1  # For categorical data like country or loyalty level

    for key, agg in metrics.items():
        print(f"{key}\t{agg['sum']},{agg['count']}")

if __name__ == "__main__":
    main()
