# Learner Engagement Analyzer (Python)

A quick Python project that analyzes an online course engagement dataset and produces insights relevant to instructional design and STEM-based learning optimization.

## 📌 What it does
- Loads a CSV file containing course completion data
- Cleans and processes the data with **pandas**
- Calculates:
  - Average completion rate
  - Most popular course
- Creates a **bar chart** visualizing average completion rate by course
- Saves the chart to `completion_by_course.png` for reporting and sharing

## 🛠 Tools & Libraries
- **Python 3**
- **pandas** – data analysis and cleaning
- **matplotlib** – data visualization

## 📂 Dataset
Dataset: [Predict Online Course Engagement Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-course-engagement-dataset)  
Source: Kaggle

## 🚀 How to run
1. Clone this repository or download the files.
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install pandas matplotlib numpy
   ```
3. Place your dataset in the project folder and update the filename in analyze.py if necessary.
4. Run the script:
   ```bash
   python analyze.py
    ```
5. View the results:
- Key metrics will print in the terminal
- A chart will be saved as completion_by_course.png
- The chart will also display on screen

## 📊 Example Output
**Console:**

Average Completion Rate: 50.34%
Most Popular Course: Business

**Chart:**
![Completion Rate Chart](completion_by_course.png)

💡 Why this project matters

This mini-project bridges **instructional design expertise** with **STEM/data skills**, demonstrating:
- Practical use of Python for education analytics
- Evidence-based insights that can inform course design decisions
- Data storytelling through visualizations

📜 License
This project is for educational purposes only.

