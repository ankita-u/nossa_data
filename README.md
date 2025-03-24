# Sustainability Report Analysis

A collection of Python programs for analyzing sustainability reports which includes word count and search topic-based content.

## Overview

This project provides two main programs:
1. A word count program that counts alphanumeric words in reports
2. A topic search program that extracts and organizes content by specific ESG topics


## Features

### Word Count (`word_count.py`)
- Counts alphanumeric words in each report
- Excludes special characters and punctuation
- Processes multiple files
- Provides per-file word count statistics

### Topic Search (`topic_search.py`)
- Case-insensitive search for predefined ESG topics
- Whole-word matching to prevent partial matches
- Processes multiple reports simultaneously
- Organizes findings by topic in separate output files
- Maintains original context of extracted paragraphs

## Project Structure
```
.
├── data/
│   ├── input/          # Input sustainability reports in markdown format
│   └── output/         # Generated topic-specific results
├── src/
│   ├── topic_search.py # Topic search implementation
│   └── word_count.py   # Word count implementation
└── README.md
```


### Word Count
1. Ensure your reports are in `data/input/`
2. Run the word count script:
   ```bash
   python src/word_count.py
   ```
3. View the console output for word counts per file

### Current Topics

The topic search tool currently looks for these ESG topics:
- Climate Risk Management
- Water Risk Management
- Scope 1
- Scope 2
- Health
- Employees
- Forests

### Topic Search
1. Place markdown files of sustainability reports in `data/input/`
2. Run the search script:
   ```bash
   python src/topic_search.py
   ```
3. Find results in `data/output/` with format `{original_filename}_results.txt`

## Output Format

### Word Count Output
Displays in console:
- Filename: total word count
- Only counts words containing alphanumeric characters

### Topic Search Output
For each input file, generates a results file containing:
- Topic headers marked with asterisks
- Relevant paragraphs under each topic
- Separator lines between topics





