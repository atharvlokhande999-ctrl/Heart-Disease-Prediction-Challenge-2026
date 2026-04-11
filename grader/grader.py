import pandas as pd
import sys

def grade(submission_path, labels_path):
    try:
        submission = pd.read_csv(submission_path)
        labels     = pd.read_csv(labels_path)
    except Exception as e:
        print(f"❌ Could not read files: {e}")
        sys.exit(1)

    # Check required column exists
    if "prediction" not in submission.columns:
        print("❌ Your submission.csv must have a column named 'prediction'")
        sys.exit(1)

    if len(submission) != len(labels):
        print(f"❌ Row count mismatch: got {len(submission)}, expected {len(labels)}")
        sys.exit(1)

    # Calculate accuracy
    correct  = (submission["prediction"].values == labels["label"].values).sum()
    total    = len(labels)
    accuracy = correct / total * 100

    print(f"✅ Accuracy: {accuracy:.2f}%  ({correct}/{total} correct)")

if __name__ == "__main__":
    grade("submission/submission.csv", "grader/test_labels.csv")
