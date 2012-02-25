# import time

def gather(s):
	i = []
	for x in range(0, len(s)):
		for y in reversed(range(x+1, len(s))):
			if (s[x].lower() == s[y].lower()):
				i.append((x, y, y - x))
	return i
	
def test_string(s):
	length = len(s)
	for x in range(0, int(length/2)):
		if (s[x].lower() != s[length - x - 1].lower()):
			return False

	return True

# start = time.clock()
	
s = "FourscoreandsevenyearsagoourfaathersbroughtforthonthiscontainentanewnationconceivedinzLibertyanddedicatedtothepropositionthatallmenarecreatedequalNowweareengagedinagreahtcivilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"

i = gather(s)

for item in sorted(i, key=lambda item: item[2], reverse=True):
	a = item[0]
	b = item[1]
	substr = s[a:b+1]
	res = test_string(substr)
	if (res == True):
		# end = time.clock()
		print(substr)
		# print(end-start)
		exit()
