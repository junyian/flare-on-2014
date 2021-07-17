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
This is a hard one for me. First, searched for PDF malware analysis and eventually found https://blog.didierstevens.com/programs/pdf-tools/ and https://blog.didierstevens.com/2008/10/20/analyzing-a-malicious-pdf-file/. Following the example video we can extract the Javascript that contains the shellcode from the PDF. The script challenge4.js writes the shellcode to a binary file (install Node.js to run the script). It was terribly difficult to do static analysis on the file. I was using Online Disassembler (https://onlinedisassembler.com/static/home/index.html) and found suspicious xors and pushes at the end of the binary, but it's too difficult to analyze this statically. I needed a way to debug the binary somehow. More searching ended up with this old gem https://github.com/MarioVilas/shellcode_tools/blob/master/shellcode2exe.py. Downloaded it, installed the dependency InlineEgg from https://www.coresecurity.com/core-labs/open-source-tools/inlineegg-cs, and eventually converted the binary file to a proper exe. Back to IDA to disassemble, breakpoint at the xors/pushes, and eventually see 'wa1ch.d3m.spl01ts@flare-on.com' written to stack.
