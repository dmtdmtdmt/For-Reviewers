# Simpson's Paradox Analyzer

A Python tool for detecting and analyzing Simpson's Paradox in clinical trial data or other comparative studies.

## Features

- Interactive data input for clinical trial scenarios
- Calculates success rates by treatment group and subgroups
- Checks for Simpson's Paradox conditions
- Provides clear visual output of analysis results
- Supports multiple analyses in a single session

## Requirements

- Python 3.6+
- pandas

## Installation

1. Clone this repository or download the script
2. Install required dependencies:
   ```bash
   pip install pandas
   ```

## Usage

Run the script and follow the interactive prompts:

```bash
python simpson_analyzer.py
```

### Input Process

1. Enter your variable names:
   - Group variable (e.g., hospital size)
   - Treatment variable (e.g., treatment type)
   - Outcome variable (e.g., success)

2. Enter possible values for each variable

3. For each combination, enter:
   - Total number of cases
   - Number of successes

### Output Interpretation

The analyzer provides:
- Success rates for each treatment in all subgroups and overall
- Subgroup proportions comparison
- Condition check for Simpson's Paradox
- Clear warning if paradox is detected

## Example Scenario

Imagine analyzing two treatments (A and B) across small and large hospitals:

```
=== Results ===

Success Rates (%):

A:
  L: 50.0%
  S: 10.0%
  Overall: 16.7%

B:
  L: 20.0%
  S: 23.6%
  Overall: 22.5%

Subgroup Proportions:
  A: 0.20
  B: 0.41

Condition met? NO

Note: No paradox, but proportions differ

Analyze another? (y/n): ****
```

## Technical Details

The analyzer checks three key aspects:
1. Success rates in each subgroup
2. Proportion of cases in each subgroup
3. Whether the subgroup proportions differ significantly between treatments

Simpson's Paradox is detected when:
- One treatment shows better results in all subgroups
- But the overall result favors the other treatment

## License

This project is open-source and available for academic and research use.

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## Author

[Denis Martínez Tápanes/MINSAP]
