# **README.md**

# FX Summary — Lab 03  
Refactored Python Package for AIGC 5005  
Author: **Md Kawsarul Islam**

---

## **Overview**

This project refactors the Lab 02 FX analysis script into a fully installable Python package named **fxsummary**.  
The package downloads foreign exchange (FX) rates from the Frankfurter API, converts them into validated `Record` objects, computes multiple statistical summaries, and writes the results to `summary.json`.

Lab 03 focuses on:

- turning Lab 02 logic into a proper Python package  
- using classes, modules, and polymorphism  
- separating concerns (models, sources, aggregations, reporting)  
- reproducible environments (`environment.yml`, `requirements.txt`)  
- writing tests  
- producing identical output to Lab 02  

---

## **Package Structure**

```
week3-lab03/
├── pyproject.toml
├── environment.yml
├── requirements.txt
├── README.md
├── data/
│   ├── raw/
│   └── processed/
│       └── summary.json
├── src/
│   └── fxsummary/
│       ├── __init__.py
│       ├── config.py
│       ├── models.py
│       ├── sources.py
│       ├── aggregations.py
│       ├── report.py
│       └── main.py
└── tests/
    ├── test_record.py
    └── test_aggregations.py
```

### **Key Modules**

| Module | Purpose |
|--------|---------|
| `models.py` | Defines the `Record` class and data validation |
| `sources.py` | Downloads FX data and returns `Record` objects |
| `aggregations.py` | Base class + three aggregation subclasses |
| `report.py` | Writes summary JSON output |
| `main.py` | Wires everything together and runs the program |
| `config.py` | Central configuration (URL, timeout, output path) |

---

## **Installation**

### **Setup
1. Create and activate Conda environment**

#Open Anaconda Prompt and go to your folder.(Example: C:\Users\kawsa\week3-lab03\)
then run below commands
```
conda env create -f environment.yml
conda activate fxsummary
```

### **2. Install dependencies**
pip install -r requirements.txt
pip install -e .

This installs the package in editable mode so changes in `src/fxsummary/` are immediately reflected.

## **Running the Program**

Once installed, run:

```
fxsummary
```

This will:

1. Download FX data  
2. Validate and convert into `Record` objects  
3. Compute three aggregations  
4. Write the summary to:

```
data/processed/summary.json
```

---

## **Design Choices**

### **Record Class**
All data cleaning and validation moved from Lab 02 functions into the `Record` constructor.  
This ensures downstream code receives clean, consistent objects.

### **Source Class**
The download logic is encapsulated in `Source.fetch()`, which returns a list of `Record` objects instead of raw dictionaries.

### **Aggregation Classes**
Lab 02 functions were refactored into subclasses of a common `Aggregation` base class:

- `MonthlyAverage`
- `LargestSingleDayChange`
- `MonthWithMostMovement`

The summary builder loops over these objects, demonstrating polymorphism.

### **Report Module**
File writing is isolated in `report.py`, keeping `main.py` clean and focused.

### **Main Program**
`main.py` only:

- loads configuration  
- downloads records  
- runs aggregations  
- writes output  

This separation improves readability and testability.

---

## **Testing**

Tests are located in the `tests/` folder.
#Open Anaconda Prompt and go to your folder.(Example: C:\Users\kawsa\week3-lab03\tests)
then run below commands

Run them with:

```
pytest
```

### Included Tests

- `test_record.py`  
  - validates correct parsing  
  - checks error handling for malformed data  

- `test_aggregations.py`  
  - tests each aggregation using hand‑made `Record` objects  
  - ensures no network calls occur during testing  

---

## **Reproducibility**

### **environment.yml**
Pins Python version and ensures consistent Conda environment.

### **requirements.txt**
well described the full requirements to reproduce in the requirements.txt file.

## **Comparison with Lab 02**

The output `summary.json` produced by Lab 03 matches the Lab 02 output almost same (one record difference).  
All refactoring preserves behavior while improving structure, modularity, and maintainability.

---

## **Known Limitations**

- The program depends on the Frankfurter API being available.  
- No caching is implemented; each run downloads fresh data.  
- Aggregations assume consistent currency availability across dates.

---

## **License**

This project is for academic use in AIGC 5005.

---
