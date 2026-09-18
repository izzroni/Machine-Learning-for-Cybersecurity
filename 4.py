import re

def classify_url(url):
    score = 0

    if not url.startswith("https://"):
        score += 1

    if len(url) > 75:
        score += 1

    if "@" in url:
        score += 2

    if "-" in url:
        score += 1

    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
        score += 2

    keywords = [
        "login", "verify", "update", "secure",
        "account", "bank", "password", "confirm",
        "free", "bonus"
    ]

    for word in keywords:
        if word in url.lower():
            score += 1

    if score >= 3:
        return "FAKE / SUSPICIOUS URL"
    else:
        return "ORIGINAL / LEGITIMATE URL"


print("URL Classification Program")
print("---------------------------")

url = input("Enter URL: ")
result = classify_url(url)

print("\nURL:", url)
print("Classification:", result)