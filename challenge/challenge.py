ipAddress = input("Enter an IP Address: ")
segmentNumber = 0
segmentSize = 0
i = ""
for i in ipAddress:
    if i == '.':
        print("Segment {0} has a size of {1}".format((segmentNumber + 1), segmentSize))
        segmentNumber += 1
        segmentSize = 0
    else:
        segmentSize += 1
print("Segment {0} has a size of {1}".format((segmentNumber + 1), segmentSize)) 