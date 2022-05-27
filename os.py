from win32com.client import Dispatch

from time import sleep

speak='''Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo
Halamithi habi yandaa
Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo
Halamithi habibo

Malama pitha pithadhe
Malama pitha pithadhe
Mala pitha pithadhe
Malama pithadhe

Hey malama pitha pithadhe
Malama pitha pithadhe
Mala pitha pithadhe
Malama pithadhe

Holi holi
Pakathula sirikkum rangoli
Jolly jolly
Vekkathula mayangura doli
Gaali gaali
Mothathula avanum dhan gaali
Jolly jolly adipoli

Halamithi habibo
Halamithi mithi vandhaale
Halamithi habibo
Halamithi mithi vandhaale
Halamithi habibo
Halamithi mithi vandhaale
Halamithi habibo
Halamithi mithi oo

Oh cutie nee sweety
Un beauty adhil maati
Naa mellamma mellamma gaali
Adha sollala sollala podi
Madhal vaati padam kaati
Enna vaati kanna kaati
Love-a konjama konjama yethi
Enna senjita senjita oruthi


Ivan yaaro sokka vachanae
En manasukulla kuzhandhai
Pola konjikittanae love-a vachanae
Ivan yaaro kick-a vachanae
En vayasukulla mudhal mazhayaa
Feel-a vachanae

Halamithi habibo, halamithi
Halamithi habibo, halamithi
Halamithi habibo, halamithi
Halamithi habibo, halamithi
Habidaa

Hey beedha balihabi
Balibaadhi balihabi
Balihabeedha balihabi
Vallae vallae balihabi

Hey beedha balihabi
Balibaadhi balihabi
Balihabeedha balihabi
Vallae vallae balihabi

Halwa ee balubabeedhadhe
Ee balubabeedha
Halwa ee balubabeedhadhe
Eh vathaadhe
Halwa ee balubabeedhadhe
Ee balubabeedha
Halwa ee balubabeedhadhe
Eh vathaadhe

Holi holi
Pakathula sirikkum rangoli
Jolly jolly
Vekkathula mayangura doli
Gaali gaali
Mothathula avanum dhan gaali
Jolly jolly adipoli


Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo
Halamithi habi vandhaa
Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo
Halamithi habibo

Oh cutie nee sweety
Un beauty adhil maati
Naa mellamma mellamma gaali
Adha sollala sollala podi
Madhal vaati padam kaati
Enna vaati kanna kaati
Love-a konjama konjama yethi
Enna senjita senjita oruthi

Ivan yaaro sokka vachanae
En manasukulla kuzhandhai
Pola konjikittanae love-a vachanae
Ivan yaaro kick-a vachanae
En vayasukulla mudhal mazhayaa
Feel-a vachanae

Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo
Halamithi habi vandhaa
Halamithi habibo
Halamithi habi vandhaale
Halamithi habibo

Malama pitha pithadhe
Malama pitha pithadhe
Mala pitha pithadhe
Malama pithadhe
Hey malama pitha pithadhe
Malama pitha pithadhe
Mala pitha pithadhe
Malama pithadhe

Hey beedha balihabi
Balibaadhi balihabi
Balihabeedha balihabi
Vallae vallae balihabi

Halamithi habibo'''
# speaker = Dispatch("SAPI.SpVoice")
mp = Dispatch("WMPlayer.OCX")
# speaker.volume = 50
# speaker.rate = 3
# mp.settings.rate = 3

tune = mp.newMedia("Malama pitha pitha (Official video) Arabic Kuthu - Halamithi Habibo - Beast Movie - Thalapathy Vijay.mp4")
mp.currentPlaylist.appendItem(tune)
mp.controls.play()
sleep(1)

mp.controls.playItem(tune)
# speaker.Speak(speak)
input("Press Enter to stop playing")

mp.controls.stop()

