import numpy as np
from scipy.stats import t

# Function to compute minimum expected value within 1 standard error confidence interval
def compute_min_expected_value(X, Y, estimated_demand):
    # Fit a linear regression model
    slope, intercept, _, _, _ = np.polyfit(X, Y, 1, full=False)

    # Residuals
    residuals = Y - (slope * X + intercept)

    # Standard error of the regression coefficient
    SE_beta1 = np.sqrt(np.sum(residuals ** 2) / (len(X) - 2)) / np.sqrt(np.sum((X - np.mean(X)) ** 2))

    # Margin of error
    margin_of_error = SE_beta1 * t.ppf(0.975, len(X) - 2)

    # Confidence interval bounds
    lower_bound = estimated_demand - margin_of_error

    # Minimum expected value within the confidence interval
    minimum_expected_value = lower_bound

    return minimum_expected_value

# Demand data for Thursday
X_thursday = np.array([1, 2, 3, 4])  # Week numbers
Y_thursday = np.array([99, 118, 113, 110])  # Demand values
estimated_demand_thursday = 117

# Demand data for Friday
X_friday = np.array([1, 2, 3, 4])  # Week numbers
Y_friday = np.array([103, 103, 96, 92])  # Demand values
estimated_demand_friday = 89

# Demand data for Saturday/Sunday
X_saturday_sunday = np.array([1, 2, 3, 4])  # Week numbers
Y_saturday_sunday = np.array([112, 110, 104, 108])  # Demand values
estimated_demand_saturday_sunday = 104

# Compute minimum expected values within 1 standard error confidence interval
min_expected_value_thursday = compute_min_expected_value(X_thursday, Y_thursday, estimated_demand_thursday)
min_expected_value_friday = compute_min_expected_value(X_friday, Y_friday, estimated_demand_friday)
min_expected_value_saturday_sunday = compute_min_expected_value(X_saturday_sunday, Y_saturday_sunday, estimated_demand_saturday_sunday)

# Print results
print("Minimum expected value within 1 standard error confidence interval for Thursday:", min_expected_value_thursday)
print("Minimum expected value within 1 standard error confidence interval for Friday:", min_expected_value_friday)
print("Minimum expected value within 1 standard error confidence interval for Saturday/Sunday:", min_expected_value_saturday_sunday)
