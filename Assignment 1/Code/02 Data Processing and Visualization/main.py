import requests
import matplotlib.pyplot as plt

url = "http://127.0.0.1:8000/students"

def fetch_students():
    response = requests.get(url, timeout = 5)
    response.raise_for_status()
    return response.json()

def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def chart(names, scores):
    plt.figure(figsize=(10, 5))
    plt.bar(names, scores)
    plt.xlabel("Students")
    plt.ylabel("Test Scores")
    plt.title("Student Test Score Analysis")
    plt.tight_layout()
    plt.show()


def main():
    students = fetch_students()

    names = [student["name"] for student in students]
    scores = [student["score"] for student in students]

    avg_score = calculate_average(scores)
    print(f"Average Score: {avg_score:.2f}")

    chart(names, scores)

if __name__ == "__main__":
    main()

