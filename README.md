# flare-on-2014
Solutions to Flare-on 2014 challenges

## Challenge 1
Exe file is a .NET executable that shows a picture upon startup. Clicking on Decode button gives gibberish. Use dnSpy to explore the exe.
The section to find is Form1.btnDecode_Click(). This loads Resources.dat_secret. Find that resource in dnSpy and save as file. Then runs some algorithm on the data.
Replicate that in Python (see challenge1.py). And we can find the string "3rmahg3rd.b0b.d0ge@flare-on.com".

## Challenge 2
HTML file with a PNG file. Open PNG file in HxD and find the PHP code at the end. Replicate that PHP code in Python (see challenge2.py). Iterate through the base64 decodes, and the final one with POST variable is done manually with an ASCII table. Final string is "a11DOTthatDOTjava5crapATflareDASHonDOTcom", which translates to "a11.that.java5crap@flare-on.com"

## Challenge 3
No coding needed. Initial analysis of file in HxD shows a typical PE header, so this is actually and executable. Load it up in IDA Free for static analysis. Function call at 0x40252A is of interest. In the function, a lot of bytes being written to stack, then 'call eax' at the end, which is actually executing the bytes that was loaded to stack. Load debugger at this point (using IDA debugger for simplicity) and trigger breakpoint at 'call eax'. Keep tracing and monitor memory changes with the xors, and finally get to a point where 'such.5h311010101@flare-on.com' is decoded in memory.

