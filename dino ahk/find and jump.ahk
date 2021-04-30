9::
MsgBox, start
Loop, {
	ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\dino ahk\test1.png
	if (ErrorLevel = 0) {
		MsgBox, found
		Click, %x%, %y%
	}
}
Return

8::Pause