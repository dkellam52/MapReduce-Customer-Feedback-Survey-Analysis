#!/usr/bin/env python3
import sys

# Mapper for filtering and emitting key-value pairs for high feedback scores
def main():
    for line in sys.stdin:
        # Skip header or empty lines
        if not line.strip() or line.startswith("CustomerID"):
            continue

        # Parse CSV line
        fields = line.strip().split(",")
        if len(fields) < 10:
            continue

        # Extract relevant fields
        _, _, _, country, income, product_quality, service_quality, purchase_frequency, feedback_score, loyalty_level = fields

        try:
            feedback_score = float(feedback_score)
            product_quality = float(product_quality)
            service_quality = float(service_quality)
            purchase_frequency = int(purchase_frequency)
            income = float(income)

            # Filter high-feedback scores
            if feedback_score >= 8:
                # Emit key-value pairs for each metric
                print(f"ProductQuality\t{product_quality}")
                print(f"ServiceQuality\t{service_quality}")
                print(f"PurchaseFrequency\t{purchase_frequency}")
                print(f"Country\t{country}")
                print(f"LoyaltyLevel\t{loyalty_level}")
                print(f"Income\t{income}")

        except ValueError:
            continue

if __name__ == "__main__":
    main()
