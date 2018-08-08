import os
import random
import json

#---------------------------------------
#   [Required]  Script Information
#---------------------------------------
ScriptName ="AutoShoutOut"
Website =""
Description ="Automatically shouts out streamers I have pre-approvedf"
Creator ="wolfcaller"
Version ="1.0.0.0"

#---------------------------------------
#   [Required] Intialize Data (Only called on Load)
#---------------------------------------
def Init():
    global streamerList, m_CommandPermission, m_Command, client_id
    m_Command = []
    client_id="yikcfiit4x1uq6h0wdv34r6889s64y"
    
    configFile = open('Services\Scripts\AutoShoutOut\config.txt', 'r')
    line = configFile.readline()
    while line:
        if not line[0] == '#':
            segments = line.split('=')
            
            if segments[0] == "trigger_words":
                for val in segments[1].split(","):
                    m_Command.append(val.strip())
            if segments[0] == "command_level":
                m_CommandPermission = segments[1].strip()
            
        line = configFile.readline()
    return

#---------------------------------------
#   [Required] Execute Data / Process Messages
#---------------------------------------
def Execute(data):
    if data.IsChatMessage():
        for val in m_Command:
            if data.User.lower() == val.lower():
                game = Parent.GetRequest("https://api.twitch.tv/kraken/channels/" + data.User + "?client_id=" + client_id, {})
                jsongame = json.loads(game)
                jsonres = json.loads(jsongame['response'])
                lastGame =  jsonres['game']
                m_Command.remove(val)
                Parent.SendTwitchMessage("Be sure to go follow " + data.User + " at https://twitch.tv/" + data.User + " . They were last seen playing " + lastGame + ". Check them out next time they go live!!!!")
                break
                
    return


#---------------------------------------
#   [Required] Tick Function
#---------------------------------------
def Tick():
    return



