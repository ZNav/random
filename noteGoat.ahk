#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.
#SingleInstance force
;On startup define click space variables
;Have settings windows open on call
;Be able to toggle and set:
;sleep time
;Calibration click
;Wol click
;Search bar click
;Scripture click


; on backslash begin capture of var, on \ use the var capture, click wol open, click search bar, type var, click enter, click scripture
:*:\::
; start recording keystrokes
; on , or - or \ stop recording
click 179, 45
Input , OutputVar, V T8, {\}
send {BackSpace}
;ADD
;store position of cursor
sleep 750
; click wol
click 22, 288
sleep 1250
; click search bar
click 631,162
sleep 1250
; type var
; type enter
send, %OutputVar%{ENTER}
; click scripture
sleep 1250
click 161, 399
sleep 1250
;ADD
;return to stored position of cursor
click 179, 45
return

; on alt s close the wol scripture tab
:*:/::
click 179, 45
click 22, 288
click 179, 45
return