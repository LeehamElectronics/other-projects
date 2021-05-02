#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


z::KeyHistory

*!Volume_Down::Media_Prev
*!Volume_Up::Media_Next
*!Volume_Mute::Media_Play_Pause