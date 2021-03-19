7::FileAppend, Another line.`n, C:\Users\bmats\OneDrive\Documents\GitHub\dino ahk\Test.txt
 
9::    
Loop, { 
	ImageSearch, x, y, 0, 0, A_ScreenWidth, A_ScreenHeight, C:\Users\bmats\OneDrive\Documents\GitHub\dino ahk\test1.png
	if (ErrorLevel = 0) {
		send, {space down}{space up}
		FileAppend, c.`n, C:\Users\bmats\OneDrive\Documents\GitHub\dino ahk\Test.txt
	}
}
Return  

8::Pause 