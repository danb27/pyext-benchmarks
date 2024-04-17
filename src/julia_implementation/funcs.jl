using Profile
using PythonCall

function bigrams(; text::String)
    tokens = split(text)
    bigrams = [string(tokens[i], " ", tokens[i+1]) for i in 1:length(tokens)-1]
    return bigrams
end


function two_sum_n_squared(; nums::PyList{Any}, target::Int)
    for i in 1:length(nums)
        for j in i+1:length(nums)
            if nums[i] + nums[j] == target
                return [i - 1, j - 1]
            end
        end
    end
    return []
end


function two_sum_n(; nums::PyList{Any}, target::Int)
    num_to_index = Dict{Int, Int}()
    for (i, num) in enumerate(nums)
        if haskey(num_to_index, target - num)
            return [num_to_index[target - num] - 1, i - 1]
        end
        num_to_index[num] = i
    end
    return []
end


function fibonacci_recursive(; n::Int)
    if n <= 1
        return n
    else
        return fibonacci_recursive(n=n-1) + fibonacci_recursive(n=n-2)
    end
end
