# backend/data_generator.py

import random  # Add this import statement

def generate_interface_data():
    return {
        "E1": {
            "throughput": random.uniform(100, 1000),  # Mbps
            "latency": random.uniform(10, 100),       # ms
            "spec_ref": "3GPP TS 38.463"
        },
        "F1": {
            "throughput": random.uniform(100, 1000),
            "latency": random.uniform(10, 100),
            "spec_ref": "3GPP TS 38.473"
        },
        # Add more interfaces like Xn, NG-C, etc.
    }
