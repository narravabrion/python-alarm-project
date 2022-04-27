import os
import pafy 
import vlc 
import time
import random


def read_alarm_file(file_name):
        '''takes file name as parameter
        checks for the file name in cwd
        returns a list of all the song links in the file
        '''
        # check current directory for file with alarm ringer links
        try:
                with open(os.path.join(os.path.dirname(__file__),file_name),'r') as alarms:
                        alarm_list =[item.strip() for item in alarms.readlines()]
                        return alarm_list      
        except IOError:
                return 'Error: File does not appear to exist.'


def random_value(ringer_list):
        '''generates a random number from 0 to the final index of
        the ringer list entry
        returns an integer value 
        '''
        try:
                value = random.randint(0,len(ringer_list)-1)
                return value
        except ValueError:
                return 'Error: Cannot generate integer'


def pick_random_ringer(ringer_list):
        '''uses a randomly generated number as an index for the 
        list of music urls to pick a random music for the alarm
        returns a random youtube url for a song
        '''
        try:
                value = random_value(ringer_list)
                ringer = ringer_list[value]
                return ringer
        except IndexError:
                return 'Error: File does not appear to be in the list.'

def play_alarm():
        '''uses a returned url to play a random song from youtube as 
        the alarm sound 
        no return value
        '''
        try:
                ringers = read_alarm_file('alarms.txt')
                clip=pick_random_ringer(ringers)
                video = pafy.new(clip) 
                time_arr = video.duration.split(':')
                time_sec = (int(time_arr[0])*3600)+(int(time_arr[1])*60)+(int(time_arr[2]))
                videolink= video.getbestaudio()
                media =vlc.MediaPlayer(videolink.url)
                media.play()
                time.sleep(time_sec+10)
        except RuntimeError:
                raise 'Error: Error while trying to fetch alarm!'
