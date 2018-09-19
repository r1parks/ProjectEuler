
class PrimeList
  def initialize
    @lines = File.readlines('prime_list.txt').each
  end

  def next
    @lines.next.to_i
  end
end
