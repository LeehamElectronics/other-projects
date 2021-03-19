9::
Loop, {
	ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\dino ahk\test1.png
	if (ErrorLevel = 0) {
		Click, %x%, %y%
	}
}
Return

8::Pause