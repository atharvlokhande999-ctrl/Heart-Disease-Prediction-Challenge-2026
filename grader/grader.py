import pandas as pd
import sys
import os
import glob

def find_submission():
    # Look for any file matching *_submission.csv or submission.csv
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
    print("   File must be named like: submission.csv, group1_submission.csv, team5_submission.csv")
    print("   And must be inside the submission/ folder")
    sys.exit(1)

def grade(submission_path, labels_path):
    try:
        submission = pd.read_csv(submission_path)
        labels     = pd.read_csv(labels_path)
    except Exception as e:
        print(f"❌ Could not read files: {e}")
        sys.exit(1)

    # Check required column exists
    if "prediction" not in submission.columns:
        print("❌ Your file must have a column named 'prediction'")
        sys.exit(1)

    if len(submission) != len(labels):
        print(f"❌ Row count mismatch: got {len(submission)}, expected {len(labels)}")
        sys.exit(1)

    # Calculate accuracy
    correct  = (submission["prediction"].values == labels["target"].values).sum()
    total    = len(labels)
    accuracy = correct / total * 100

    print(f"✅ Accuracy: {accuracy:.2f}%  ({correct}/{total} correct)")

if __name__ == "__main__":
    submission_path = find_submission()
    grade(submission_path, "grader/test_labels.csv")
