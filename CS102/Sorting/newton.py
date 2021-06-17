# This function estimates the square root of a number using the Newton's method.
# As a remainder these method is based on a iterative acotation of the search field.
# The middle term of the search field is selected as a candidate to be the square root.
# If the difference between the 2-power of the candidate and the target, half of the search field
# is rejected and a new candidate is selected.

def newton_sqrt(target_value, allowed_error): # at a starting point we assume that the sqrt has to be between 0 and the target value
    count = 0 # variable for counting the number of iterations
    lower_bound = 0 # first lower bound
    upper_bound = target_value # first upper bound
    estimated_sqrt = (lower_bound + upper_bound) / 2 # the estimated sqrt is the middle term
    estimated_power = estimated_sqrt ** 2 

    while abs(estimated_power - target_value) > allowed_error: # while the actual error is higher than the allowed

        count += 1

        if estimated_power > target_value: # if the power estimated is higher than then actual one
            upper_bound = estimated_sqrt # set the previous estimated sqrt to be the new upper bound
            estimated_sqrt = (lower_bound + upper_bound) / 2
            estimated_power = estimated_sqrt ** 2

        else: #if the power estimated is not higher than then actual one
            lower_bound = estimated_sqrt # set the previous estimated sqrt to be the new lower bound
            estimated_sqrt = (lower_bound + upper_bound) / 2
            estimated_power = estimated_sqrt ** 2

    return estimated_sqrt, count

print(newton_sqrt(1000, 0.0001))