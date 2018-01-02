from TV import TV

def main():
    tv1 = TV()
    tv1.turnOn()
    tv1.setChannel(30)
    tv1.setVolume(3)

    tv2 = TV()
    tv2.turnOn()
    tv2.channelUp()
    tv2.channelUp()
    tv2.volumeUp()

    print("tv1's channel is {} and volume level is {}.".format(tv1.getChannel(), tv1.getVolumeLevel()))
    print("tv2's channel is {} and volume level is {}.".format(tv2.getChannel(), tv2.getVolumeLevel()))

main()