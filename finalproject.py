print "\t\t\t ----------------"
print "\t\t\t THE DARK FOREST"

print "\t\t\tInstructions: Use number or answer with 'y' or 'n'"
print "\t\t\t ----------------"

print "You wake up alone . Your friends have left you behind in an unknown part of the woods. You become scared."
print "Your friends ran off supposedly hearing the sounds of a beast said to roam these forests at night."
print "You have heard the stories of the creature, but there's no way they can be true."
print "Did you hear that?"
print "1. Yes"
print "2. No"

heard_noise = raw_input()

if heard_noise == 1 or heard_noise == "Yes":
print "You heard a scary noise behind the bushes"
else:
print "You didn't hear anything"