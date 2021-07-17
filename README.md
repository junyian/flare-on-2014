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

## Challenge 4
This is a hard one for me, since it's my first time doing PDF malware analysis. First, searched for examples for this theme and eventually found https://blog.didierstevens.com/programs/pdf-tools/ and https://blog.didierstevens.com/2008/10/20/analyzing-a-malicious-pdf-file/. Following the example video we can extract the Javascript that contains the shellcode from the PDF. The script challenge4.js writes the shellcode to a binary file (install Node.js to run the script). It was terribly difficult to do static analysis on the file. I was using Online Disassembler (https://onlinedisassembler.com/static/home/index.html) and found suspicious xors and pushes at the end of the binary, but it's too difficult to analyze this statically. I needed a way to debug the binary somehow. More searching ended up with this old gem https://github.com/MarioVilas/shellcode_tools/blob/master/shellcode2exe.py. Downloaded it, installed the dependency InlineEgg from https://www.coresecurity.com/core-labs/open-source-tools/inlineegg-cs, and eventually converted the binary file to a proper exe. Back to IDA to disassemble, breakpoint at the xors/pushes, started debugging, and eventually see 'wa1ch.d3m.spl01ts@flare-on.com' written to stack.

## Challenge 5
File is a DLL (without the extension). Loading it in IDA shows DllEntryPoint which confirms it. IDA's debugger is not suitable here so I used x64dbg (well, x32dbg actually since it's 32-bit) to launch the DLL. After a LOT of tracing, finally found a piece of code that starts by calling GetAsyncKeyState to check what key is pressed. Then compares it to a huge switch table comparing the key to special chars (backspace, enter, etc.), numbers (0-9), characters (a-z) and symbols (dot, question mark, etc.). Each case calls a function for each char. Looking into each function, some just gets the offset, others write some sort of flag into a global var. And there are many of it. I realize that this logs the keys and setting a flag if the key is pressed. The code also resets other flags not related to its char. So use IDA, check cross references, and determine which is the only function that sets the flag. Luckily, all the vars are arranged in a set order, so we can finally see the chars are arranged as 'l0gging.ur.5tr0ke5@flare-on.com'
