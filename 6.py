import re

def extract_features(url):
    features = {}

    features["length"] = len(url)
    features["dots"] = url.count(".")
    features["hyphens"] = url.count("-")
    features["special_chars"] = len(re.findall(r"[@?=&%]", url))

    if re.search(r"https?://\d+\.\d+\.\d+\.\d+", url):
        features["ip_address"] = 1
    else:
        features["ip_address"] = 0

    return features


def detect_anomaly(url):
    f = extract_features(url)
    score = 0
    reasons = []

    if f["length"] > 75:
        score += 1
        reasons.append("Unusually long URL")

    if f["dots"] > 3:
        score += 1
        reasons.append("Too many dots")

    if f["hyphens"] > 2:
        score += 1
        reasons.append("Too many hyphens")

    if f["special_chars"] > 3:
        score += 1
        reasons.append("Many special characters")

    if f["ip_address"] == 1:
        score += 2
        reasons.append("Uses IP address")

    if score >= 3:
        result = "ABNORMAL / SUSPICIOUS"
    else:
        result = "NORMAL"

    return f, score, result, reasons


print("================================")
print("       URL ANOMALY DETECTOR     ")
print("================================")

url = input("Enter a URL: ")

features, score, result, reasons = detect_anomaly(url)

print("\nURL:", url)
print("\nExtracted Features:")
for key, value in features.items():
    print(key, ":", value)

print("\nAnomaly Score:", score)
print("Classification:", result)

print("\nAnalysis:")
if reasons:
    for reason in reasons:
        print("-", reason)
else:
    print("- No abnormal patterns found")

print("\nURL anomaly detection completed successfully.")