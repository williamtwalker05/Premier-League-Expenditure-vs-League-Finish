# Transfer expenditure and Premier League finishing position

Does spending more on transfers lead to a better league finish? This project tests that using Pearson correlation and linear regression on Premier League data, for three cases:

- the **11-season average** (2014/15 to 2024/25)
- the **2015/16** season
- the **2024/25** season

The full write-up is in [`report/Premier_League_Transfer_Report.pdf`](report/Premier_League_Transfer_Report.pdf).

## Results

Hypothesis test: H0: r = 0, H1: r < 0 (one-sided, significance level 0.05).

| Case | n | r | r² | p (one-sided) | Decision |
|---|---|---|---|---|---|
| 11-season average | 18 | -0.7936 | 0.630 | < 0.0001 | Reject H0 |
| 2015/16 | 20 | -0.2301 | 0.053 | 0.1645 | Fail to reject H0 |
| 2024/25 | 20 | -0.0671 | 0.005 | 0.3893 | Fail to reject H0 |

Averaged over many seasons, higher spending is strongly associated with better finishes (Liverpool is the one outlier, finishing much higher than their spending suggests). In the two single seasons there was no significant correlation.

Figures are in the `figures/` folder: `fig1_11_season.png`, `fig2_2015_16.png` and `fig3_2024_25.png`.

## Repository layout

```
README.md
report/
    Premier_League_Transfer_Report.pdf
figures/
    fig1_11_season.png
    fig2_2015_16.png
    fig3_2024_25.png
analysis/
    fig1_11_season.py
    fig2_2015_16.py
    fig3_2024_25.py
    PosVSSpend.csv
    League positions(15-16).csv
    League positions(24-25).csv
```

| Script | Data it reads |
|---|---|
| `fig1_11_season.py` | `PosVSSpend.csv` (average position and average spend per club) |
| `fig2_2015_16.py` | `League positions(15-16).csv` (spend and final position per club) |
| `fig3_2024_25.py` | `League positions(24-25).csv` (spend and final position per club) |

## Setup

Python 3 with:

```
pip install pandas numpy matplotlib scikit-learn scipy nooverlap
```

## Running

Run the scripts from inside the `analysis` folder, which holds the CSV files they read:

```
cd analysis
python fig1_11_season.py
python fig2_2015_16.py
python fig3_2024_25.py
```

Each script saves its figure as a PNG in the folder it is run from and prints n, r, r², the regression slope, the one-sided p-value and whether the result is significant. Outliers are clubs whose residual from the regression line is more than two standard deviations of the residuals.

## Data

- **Transfer expenditure:** [Transfermarkt](https://www.transfermarkt.com/), accessed October 2026. This is gross spend (the total fees paid for incoming players, not net of sales) in euros, with no adjustment for inflation. Loan fees are included. Free transfers, loans without a fee and returns from loan count as zero, and undisclosed fees are left out.
- **League positions:** [Premier League](https://www.premierleague.com/en/), final standings, accessed October 2025.
- **Inclusion:** the 11-season average includes only clubs that played at least six Premier League seasons between 2014/15 and 2024/25. The single-season cases include all 20 clubs.

## Limitations

The results show association, not causation. Transfer fees are only part of what clubs spend (wages are not included), figures are not adjusted for inflation or net of sales, and a club's position in one season also depends on squads built in earlier seasons.
