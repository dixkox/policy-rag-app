import requests
import json
import time

# Your full evaluation question set (30 questions)
QUESTIONS = [
    "What is the main objective of the PTO policy?",
    "How many PTO days are employees entitled to per year?",
    "How should employees request PTO?",
    "Does unused PTO roll over to the next year?",
    "What happens if an employee takes unauthorized leave?",
    "What are employees required to do to maintain information security?",
    "What should employees do if they notice suspicious activity?",
    "What are the core hours employees must be available during remote work?",
    "What cybersecurity guidelines must remote employees follow?",
    "What should employees do to ensure a professional remote work environment?",
    "What is the main objective of the Information Security Policy?",
    "What is the main objective of the Remote Work Policy?",
    "What is the main objective of the Code of Conduct?",
    "How often do employees accrue PTO?",
    "Where should employees report suspicious activity?",
    "What type of passwords must employees use?",
    "What is MFA and why must employees enable it?",
    "What should employees avoid to prevent conflicts of interest?",
    "How should employees behave to maintain integrity?",
    "What happens if employees fail to follow data handling procedures?",
    "What must employees do to comply with laws?",
    "What are employees expected to do during core hours?",
    "How should employees maintain availability while working remotely?",
    "What should employees do to follow cybersecurity guidelines?",
    "How many PTO hours can roll over each year?",
    "Where do employees request time off?",
    "What ensures work-life balance for employees?",
    "What protects company data and systems?",
    "What defines expectations for remote employees?",
    "What establishes ethical standards for employees?"
]

API_URL = "http://127.0.0.1:8000/ask"

results = []

print("Running full evaluation...")

for idx, question in enumerate(QUESTIONS, start=1):
    print(f"Running Q{idx}: {question}")
    start = time.time()

    response = requests.post(API_URL, json={"question": question})
    latency = (time.time() - start) * 1000

    if response.status_code == 200:
        data = response.json()
        data["measured_latency_ms"] = latency
        results.append(data)
    else:
        results.append({
            "question": question,
            "error": f"HTTP {response.status_code}"
        })

with open("eval_results.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nEvaluation complete.")
print("Results saved to eval_results.json")
