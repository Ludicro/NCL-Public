# Context
```
    2       3       4        5
1  Time | Ticket | Price | Change
4  data |  data  |  data |  data
```

# Q1: Which ticker experienced abnormal behavior?
**A1:**
`awk -F '|' 'NR > 3 { gsub(" ", "", $5); if ($5 + 0 > 2 || $5 + 0 < -2) print $3, $4, $5 }' stocks.log | sort -k3,3n`

`awk -F '|'`: This option sets the input field separator to |. This means that awk will treat | as the delimiter between fields in each line of the input.

`'NR > 3`: This condition checks if the line number is greater than 3, which effectively skips the first three lines of the input (usually the header in a log file).

`gsub(" ", "", $5);`: This function call removes all spaces from the fifth field (which corresponds to the Change column). gsub stands for "global substitution," and it replaces all occurrences of the first argument (a space in this case) with the second argument (an empty string).

`if ($5 + 0 > 2 || $5 + 0 < -2`: Checks if the numerical value of the Change is greater than 2 or less than -2 to filter for significant changes.

`sort -k3,3n`: Sorts the output based on the third field (the Change), using numeric sorting in reverse order to display the highest changes first.
