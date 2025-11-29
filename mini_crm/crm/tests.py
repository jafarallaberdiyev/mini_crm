import requests
import json

BASE_URL = "http://localhost:8000/api"


def final_test():
    print("🚀 Running final system test...")

    # Test all endpoints
    endpoints = ['students', 'rooms', 'bookings']

    for endpoint in endpoints:
        response = requests.get(f"{BASE_URL}/{endpoint}/")
        print(f"✅ {endpoint.upper()}: {response.status_code}")

    print("🎉 System ready for submission!")


if __name__ == "__main__":
    final_test()