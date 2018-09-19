#!/usr/bin/env ruby

require_relative 'prime_list'
require 'pqueue'
require 'set'

def log_n_divisors(pow_2, nth_prime)
  Math.log(pow_2 + 1, 2) + nth_prime - 1
end

primes = PrimeList.new
primes.next
next_prime = primes.next

n = 2

largest_non_prime = 0

options = PQueue.new([2 ** 2, next_prime]) { |a,b| a < b }
# options = SortedSet.new([2 ** 2, next_prime])

(2..500500).each do |x|
  if x % 1000 == 0
    puts "iteration #{x}, #{options.size} elements, #{n}, largest non prime: #{largest_non_prime}"
  end
  next_element = options.pop
  if next_element < 7500000
    options << (next_element ** 2)
  end
  if next_element == next_prime
    next_prime = primes.next
    options << next_prime
  else
    if next_element > largest_non_prime
      largest_non_prime = next_element
    end
  end
  # puts "#{n} * #{next_element}"
  n = (n * next_element) % 500500507
  # puts " = #{n}"
end

puts n

# def n_from_factors(factors, modulo)
#   factors.map { |p, e| p ** e }.reduce(1) { |product, n| (product * n) % modulo }
# end

# primes = PrimeList.new
# current_n = primes.next # 2
# pow_2 = 1
# nth_prime = 1
# next_prime = primes.next
# 
# next_pow_2 = 3
# pow_2_multiple = 2 ** (next_pow_2 - pow_2)
# 
# while log_n_divisors(pow_2, nth_prime) < 500500
#   if next_prime < pow_2_multiple
#     current_n *= next_prime
#     next_prime = primes.next
#     nth_prime += 1
#   else
#     current_n *= pow_2_multiple
#     pow_2 = next_pow_2
#     next_pow_2 = pow_2 * 2 + 1
#     pow_2_multiple = 2 ** (next_pow_2 - pow_2)
#   end
#   current_n = current_n % 500500507
# end
# 
# puts current_n
# puts pow_2
# puts nth_prime
# puts log_n_divisors(pow_2, nth_prime)


# while log_n_divisors(current_n) < 500500
#   puts "#{current_n[0][1]}, #{current_n.size}, #{log_n_divisors(current_n)}"
#   n_next_prime = current_n + [[next_prime, 1]]
#   n_more_twos = current_n.dup
#   n_more_twos[0] = current_n[0].dup
#   n_more_twos[0] = [2, current_n[0][1] * 2 + 1]
#   raise "Bad! #{log_n_divisors(n_next_prime)} != #{log_n_divisors(n_more_twos)}" unless log_n_divisors(n_next_prime) == log_n_divisors(n_more_twos)
#   if Math.log(next_prime, 2) < (n_more_twos[0][1] - current_n[0][1])
#     current_n = n_next_prime
#     next_prime = primes.next
#   else
#     current_n = n_more_twos
#   end
# end

# p current_n
# puts n_from_factors current_n, 500500507
# puts log_n_divisors current_n

