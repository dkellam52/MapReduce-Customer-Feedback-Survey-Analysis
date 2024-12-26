#!/usr/bin/env python3
import sys
from collections import defaultdict

# Reducer to compute final averages and distributions
metrics = defaultdict(lambda: {"sum": 0, "count": 0})

def main():
    for line in sys.stdin:
        key, value = line.strip().split("\t")
        total, count = map(float, value.split(","))
        metrics[key]["sum"] += total
        metrics[key]["count"] += count

    for key, agg in metrics.items():
        avg = agg["sum"] / agg["count"] if agg["count"] > 0 else 0
        print(f"{key}\t{avg:.2f}")

if __name__ == "__main__":
    main()
