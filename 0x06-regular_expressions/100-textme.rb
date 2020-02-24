#!/usr/bin/env ruby
print ARGV[0].scan(/from:(\w+)/).join
print ","
print ARGV[0].scan(/to:(\+?\d+)/).join
print ","
puts ARGV[0].scan(/flags:(\-?\d:\-?\d:\-?\d:\-?\d:\-?\d)/).join
