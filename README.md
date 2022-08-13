# Real-Estate-Value
I went with Random Forest because it can perform both classification and regression tasks so the code can be scaled to be used as a classifier where you can input house data that fits the features to determine if the house is overpriced or fair market value.

Data cleanup was the toughest part of this project as it had many special characters that had to be removed so I wouldn't have errors in type conversion. I learned there are functions you can use to clean data with NumPy, but for whatever reason it didn't work in this dataset as it may have been implemented incorrectly.

The overall output is a mean of absolute error which is used to show the difference between measured value and “true” value. I imagine this being useful for VA home loans especially because the appraisal process in that compares homes that recently sold with similar specifications as the one you have offered on to see how the house appraises to the market.
