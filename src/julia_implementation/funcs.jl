using Profile
using PythonCall

function bigrams(; text::String)
    tokens = split(text)
    bigrams = [string(tokens[i], " ", tokens[i+1]) for i in 1:length(tokens)-1]
    return pylist(bigrams)
end


function two_sum_n_squared(; nums::PyList{Any}, target::Int)
    for i in 1:length(nums)
        for j in i+1:length(nums)
            if nums[i] + nums[j] == target
                return pylist([i - 1, j - 1])
            end
        end
    end
    return pylist([])
end


function two_sum_n(; nums::PyList{Any}, target::Int)
    num_to_index = Dict{Int, Int}()
    for (i, num) in enumerate(nums)
        if haskey(num_to_index, target - num)
            return pylist([num_to_index[target - num] - 1, i - 1])
        end
        num_to_index[num] = i
    end
    return pylist([])
end


function profile_test(n)
    text = "This is a sample text for generating bigrams to compare performance."
    for _ in 1:n
        bigrams(text=text)
    end
end

# using ProfileView
#
# profile_test(1)  # run once to trigger compilation (ignore this one)
# @profview profile_test(100000)  # run for real
# println("Press Enter to exit...")
# readline()
