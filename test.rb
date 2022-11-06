hi = "     고 거 앨 없 도 칸 빈 고 리 그 야 거 을 집 뒤 걸 이 난        "
hi2 = hi.reverse
hi3 = hi.reverse.strip.upcase
#puts(hi2)
#puts(hi3)

ki = "     I will reverse this and make lower to upper        "
ki2 = ki.reverse
ki3 = ki.reverse.strip.upcase
#puts(ki2)
#puts(ki3)

def convert(input)
	return input.reverse.strip.upcase
end

puts(convert(ki))
puts(convert(hi))