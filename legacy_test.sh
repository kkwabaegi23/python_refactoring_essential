#!/usr/bin/env bash
set -e

echo "Running ShippingApp for multiple orders..."
echo

for order_id in 1001 1002 1003; do
    echo "============================"
    echo "Running order ID: $order_id"
    echo "============================"

    python -m legacy_code.src.ShippingApp "$order_id"

    echo
done

echo "Done."
