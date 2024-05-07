#!/usr/bin/env ruby

#ruby scriot that prints name of sender, name of receiver 
#and flags of a textme app
sender = ARGV[0].scan(/from:(.*?)\]/)
receiver = ARGV[0].scan(/to:(.*?)\]/)
flags = ARGV[0].scan(/flags:(.*?)\]/)
puts [sender, receiver, flags].join(',')
