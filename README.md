# flare-on-2014
Solutions to Flare-on 2014 challenges

## Challenge #1
Exe file is a .NET executable that shows a picture upon startup. Clicking on Decode button gives gibberish. Use dnSpy to explore the exe.
The section to find is Form1.btnDecode_Click(). This loads Resources.dat_secret. Find that resource in dnSpy and save as file. Then runs some algorithm on the data.
Replicate that in Python (see Challenge1 folder). And we can find the string "3rmahg3rd.b0b.d0ge@flare-on.com".
