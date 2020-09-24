# N21 Challenge

## Instructions

There are no dependencies, simply run:

    python3 python-project.py [--configPath CONFIGPATH] documentPath

Example:

    python3 python-project.py .\examples\document.txt
    
    
## Complexity

Code runs in linear time. Memory is also linear.


## Results

The result is in a json-style format output which shows exact position that an entry 
in the config file occurred. If we had the pandas package, this could be easily
transformed into a pandas dataframe, and the user can do data analysis on it.

    [{'Entry': 'Sanctioned Person', 'LineNum': 9, 'StartPos': 19},
    {'Entry': 'Sanctioned Country', 'LineNum': 10, 'StartPos': 6},
    {'Entry': 'Sanctions', 'LineNum': 4, 'StartPos': 15},
    {'Entry': 'Sanctions', 'LineNum': 10, 'StartPos': 15},
    {'Entry': 'Material Project Party', 'LineNum': 3, 'StartPos': 13},
    {'Entry': 'Affiliates', 'LineNum': 6, 'StartPos': 1},
    {'Entry': 'Affiliates', 'LineNum': 8, 'StartPos': 13},
    {'Entry': 'Person', 'LineNum': 9, 'StartPos': 20},
    {'Entry': 'Anti-Money Laundering Laws', 'LineNum': 4, 'StartPos': 12},
    {'Entry': 'Anti-Money Laundering Laws', 'LineNum': 7, 'StartPos': 8},
    {'Entry': 'Borrower', 'LineNum': 1, 'StartPos': 5},
    {'Entry': 'Borrower', 'LineNum': 1, 'StartPos': 20},
    {'Entry': 'Borrower', 'LineNum': 2, 'StartPos': 12},
    {'Entry': 'Borrower', 'LineNum': 3, 'StartPos': 1},
    {'Entry': 'Borrower', 'LineNum': 3, 'StartPos': 8},
    {'Entry': 'Borrower', 'LineNum': 5, 'StartPos': 3},
    {'Entry': 'Borrower', 'LineNum': 5, 'StartPos': 21},
    {'Entry': 'Borrower', 'LineNum': 6, 'StartPos': 8},
    {'Entry': 'Borrower', 'LineNum': 7, 'StartPos': 12},
    {'Entry': 'Borrower', 'LineNum': 8, 'StartPos': 12},
    {'Entry': 'Borrower', 'LineNum': 8, 'StartPos': 20},
    {'Entry': 'Subsidiaries', 'LineNum': 2, 'StartPos': 2},
    {'Entry': 'Subsidiaries', 'LineNum': 5, 'StartPos': 6},
    {'Entry': 'Subsidiaries', 'LineNum': 7, 'StartPos': 15},
    {'Entry': 'Anti-Corruption Laws', 'LineNum': 4, 'StartPos': 17},
    {'Entry': 'Anti-Corruption Laws', 'LineNum': 7, 'StartPos': 5}]
