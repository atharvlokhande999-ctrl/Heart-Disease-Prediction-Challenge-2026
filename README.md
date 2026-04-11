# Heart Disease Prediction Challenge 2026

Predict whether a patient has heart disease using clinical data.
Submissions are auto-graded and ranked on the live leaderboard.

## 🏆 Leaderboard
Live leaderboard is available here:
👉 https://Sahil-Pasalkar101.github.io/Heart-Disease-Prediction-Challenge-2026/
---

## Dataset

| File | Description |
|------|-------------|
| `data/train.csv` | Training data — includes the `target` column |
| `data/test.csv` | Test data — no labels, predict on this |

**Target:** `1` = Heart Disease, `0` = No Heart Disease

---

## How to Participate

**Step 1 — Get the files**
Click **"Use this template"** at the top of this page and create your own copy of this repository.

**Step 2 — Build your model**
Use `data/train.csv` to train your model, then predict on `data/test.csv`.
A basic starter script is available in `starter_code/starter_code.py`.

### Step 3 — Save your predictions
Your submission file must follow these rules:

✅ Save it inside the `submission/` folder
✅ Name it exactly: `groupN_submission.csv` (e.g. `group1_submission.csv`)
✅ Must have exactly one column named `prediction`
✅ Values must be `0` or `1` only
✅ Must have exactly **61 rows** (one per row in test.csv)

Your file should look like this:
prediction
1
0
1
0

### Step 4 — Submit your predictions
1. Push your `submission/groupN_submission.csv` to your repo
2. Go to your repo on GitHub
3. Click **"Pull requests"** → **"New pull request"**
4. Click **"compare across forks"**
5. Set dropdowns like this:

6. Click **"Create pull request"**
7. Wait for the bot to post your score as a comment!

---

## 📊 Scoring

Your submission will be evaluated on **F1 Score** (primary) and **Accuracy** (secondary).

| Metric | Description |
|--------|-------------|
| F1 Score | Harmonic mean of precision and recall — main ranking metric |
| Accuracy | Percentage of correct predictions |

> F1 Score is used because the dataset may be imbalanced.
> A score of 1.0 is perfect, 0.0 is worst.

---

## 💡 Tips to Improve Your Score

- Try different models: `RandomForest`, `XGBoost`, `SVM`, `LogisticRegression`
- Do feature engineering — create new features from existing ones
- Handle class imbalance using `class_weight='balanced'`
- Use cross validation to avoid overfitting
- Tune hyperparameters using `GridSearchCV`


