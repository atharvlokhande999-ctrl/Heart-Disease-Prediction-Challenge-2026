import pandas as pd
import sys
import os
import glob
import json
from datetime import datetime

def find_submission():
    patterns = [
        "submission/submission.csv",
        "submission/*_submission.csv"
    ]
    for pattern in patterns:
        files = glob.glob(pattern)
        if files:
            print(f"✅ Found submission file: {files[0]}")
            return files[0]
    print("❌ No submission file found!")
    print("   Name your file like: group1_submission.csv")
    sys.exit(1)

def grade(submission_path, labels_path):
    try:
        submission = pd.read_csv(submission_path)
        labels     = pd.read_csv(labels_path)
    except Exception as e:
        print(f"❌ Could not read files: {e}")
        sys.exit(1)

    if "prediction" not in submission.columns:
        print("❌ Your file must have a column named 'prediction'")
        sys.exit(1)

    if len(submission) != len(labels):
        print(f"❌ Row count mismatch: got {len(submission)}, expected {len(labels)}")
        sys.exit(1)

    correct  = (submission["prediction"].values == labels["target"].values).sum()
    total    = len(labels)
    accuracy = round(correct / total * 100, 2)

    print(f"✅ Accuracy: {accuracy:.2f}%  ({correct}/{total} correct)")

    # Save result to file for leaderboard
    group_name = os.environ.get("GROUP_NAME", "unknown")
    pr_number  = os.environ.get("PR_NUMBER", "0")

    result = {
        "group": group_name,
        "accuracy": accuracy,
        "correct": int(correct),
        "total": int(total),
        "pr": pr_number,
        "date": datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")
    }

    os.makedirs("leaderboard_data", exist_ok=True)
    with open(f"leaderboard_data/result.json", "w") as f:
        json.dump(result, f)

    print(f"📊 Result saved for leaderboard")

if __name__ == "__main__":
    submission_path = find_submission()
    grade(submission_path, "grader/test_labels.csv")
