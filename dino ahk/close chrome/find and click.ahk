1::
MsgBox, start
Loop, {
	ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\other-projects\close chrome\back1.jpg
	if (ErrorLevel = 0) {
		MsgBox, found
		ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\other-projects\close chrome\x.jpg
		if (ErrorLevel = 0) {
			Click, %x%, %y%
			MsgBox, click
		}
	}

	ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\other-projects\close chrome\forward1.jpg
	if (ErrorLevel = 0) {
		MsgBox, found
		ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\other-projects\close chrome\x.jpg
		if (ErrorLevel = 0) {
			Click, %x%, %y%
			MsgBox, click
		}
	}
}
Return  

8::Pause 