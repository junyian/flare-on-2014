# flare-on-2014
Solutions to Flare-on 2014 challenges
Last updated: 3 Aug 2021

This is meant to document my journey in completing the Flare-on 2014 Challenges.
I left a lot of details out as I feel it would be more beneficial to go over the
approach in solving the challenges, instead of explaining every little detail.
The solutions from Flare-on's website does a much better job of doing that
anyway. I admit that I also referred to the solutions after trying the
challenges on my own and getting stuck. Overall, it's been a really rewarding
learning journey. Maybe in the future I'll do a more in-depth study of the
challenges.

## Challenge 1
Exe file is a .NET executable that shows a picture upon startup. Clicking on 
Decode button gives gibberish. Use dnSpy to explore the EXE and find the code
that's triggered upon clicking the button, which is Form1.btnDecode_Click().
This loads Resources.dat_secret. Found that resource in dnSpy and save as file.
Then notice some algorithm being executed on the data. Replicate that in Python
(see challenge1.py) and we can resolve it to "3rmahg3rd.b0b.d0ge@flare-on.com".

## Challenge 2
HTML file with a PNG file. Open PNG file in HxD and find the PHP code at the 
end. Replicate that PHP code in Python (see challenge2.py). Iterate through the 
base64 decodes, and the final one with POST variable is done manually with an 
ASCII table. Final string is "a11DOTthatDOTjava5crapATflareDASHonDOTcom", which 
translates to "a11.that.java5crap@flare-on.com".

## Challenge 3
No coding needed. Initial analysis of file in HxD shows a typical PE header, so 
this is actually and executable. Load it up in IDA Free for static analysis. 
Function call at 0x40252A is of interest. In the function, a lot of bytes being 
written to stack, then 'call eax' at the end, which is actually executing the 
bytes that was loaded to stack. Load debugger at this point (using IDA debugger 
for simplicity) and trigger breakpoint at 'call eax'. Keep tracing and monitor 
memory changes with the xors, and finally get to a point where 
'such.5h311010101@flare-on.com' is decoded in memory.

## Challenge 4
This is a hard one for me, since it's my first time doing PDF malware analysis. 
First, searched for examples for this theme and eventually found 
https://blog.didierstevens.com/programs/pdf-tools/ and 
https://blog.didierstevens.com/2008/10/20/analyzing-a-malicious-pdf-file/. 
Following the example video we can extract the Javascript that contains the 
shellcode from the PDF. The script challenge4.js writes the shellcode to a 
binary file (install Node.js to run the script). It was terribly difficult to 
do static analysis on the file. I was using Online Disassembler 
(https://onlinedisassembler.com/static/home/index.html) and found suspicious
xors and pushes at the end of the binary, but it's too difficult to analyze 
this statically. I needed a way to debug the binary somehow. More searching 
ended up with this old gem 
https://github.com/MarioVilas/shellcode_tools/blob/master/shellcode2exe.py. 
Downloaded it, installed the dependency InlineEgg from 
https://www.coresecurity.com/core-labs/open-source-tools/inlineegg-cs, and 
eventually converted the binary file to a proper exe. Back to IDA to 
disassemble, breakpoint at the xors/pushes, started debugging, and eventually 
see 'wa1ch.d3m.spl01ts@flare-on.com' written to stack.

## Challenge 5
File is a DLL (without the extension). Loading it in IDA shows DllEntryPoint 
which confirms it. IDA's debugger is not suitable here so I used x64dbg (well, 
x32dbg actually since it's 32-bit) to launch the DLL. After a LOT of tracing, 
finally found a piece of code that starts by calling GetAsyncKeyState to check
what key is pressed. Then compares it to a huge switch table comparing the key 
to special chars (backspace, enter, etc.), numbers (0-9), characters (a-z) and 
symbols (dot, question mark, etc.). Each case calls a function for each char.
Looking into each function, some just gets the offset, others write some sort 
of flag into a global var. And there are many of it. I realize that this logs 
the keys and setting a flag if the key is pressed. The code also resets other 
flags not related to its char. So use IDA, check cross references, and determine
which is the only function that sets the flag. Luckily, all the variables
are arranged in a set order, so we can finally see the chars are arranged as 
'l0gging.ur.5tr0ke5@flare-on.com'

## Challenge 6
This is going to be a longer writeup. Simply because it's a lot more difficult
compared to the previous ones. And doing a brain dump helps me remember when I
look back at my previous works and recall what I have learnt from this.

This is extremely challenging by my standards. I don't do Linux so it took me a
while to set up a debugging environment using WSL with edb-debugger. And still
using IDA Free (in Windows) to view the disassembly and debug the binary
alongside it. The binary is highly obfuscated. There are a lot of instructions
that eventually leads to doing nothing (thankfully the demo decompiler in IDA
Free supports x64, so it's very easy to discern which subroutines are doing
nothing). The obvious thing to do is to find the correct call to trigger a
breakpoint and start analyzing from there. But the disassembly is not finding 
any libraries that I can use. In fact I actually gave up because I'm totally 
unfamiliar with Linux. The normal methods I'm familiar with didn't work, so I 
read some solutions online from fireeye.com to figure out what to look for and 
what tools can be used. And treat this as a learning experience. So here's a 
summary on how I could get to the answer.

The first thing I did was to run the executable, only to get a "no". I failed to
find this in the string window for tracing back to where this is referenced
from. But I should have also used the text search (lesson learned - disassembler
is not perfect!)  Using strace with -i flag, the offset of the syscall that
prints the string to console is found in the disassembly. So place breakpoint in
the debugger. When it gets triggered, backtrack the stack to see where this is
called from, and find where the conditional jump is. Very quickly I can find the
point where it compares argc==1.

So re-run the debugger with an extra arg. Then we get segmentation fault
warning. Using the same approach as before - breakpoint, backtrack, find the
conditional jump. And realize that this comes after a ptrace call. I guess this
is an anti-debugging method in Linux. So patch this part to jmps and move on.

Next step is to analyze where the "bad" output is from. From here, we can find
that the 1st arg must be 10 chars long. And each char must be xor'ed with 56h to
get the result bngcg`debd. So xor-ing the result again with 56h (for first
timers, xor-ing the same value twice gets back the previous value), we get the
string 4815162342.

After this, the binary hangs after a call to a VERY long nanosleep() of 3600s.
Same drill as before, we find the call where E10h is loaded. I patched this to 0
so effectively nanosleep is called with 0 seconds. And finally the binary exits
without anymore warnings. This is the part where it gets more tricky.

Throughout the dissassembly and the debugging session, I noticed a pattern
repetition where the first byte is taken from a string, and stored to a global
byte variable. The strings follow a pattern: a word that starts with numbers, or
A to Z, or a to z. Due to the obfuscation, it was terribly painful to figure
out what bytes go where. From reading other solutions then I realize this builds
a string that can be base64 decoded. The problem is, how do I know when the
string is fully built? I'm totally unfamiliar with IDA's IDC scripts so I opted
the hard way: step over the functions until the app quits. Note the last
function. Then rerun but step into that function. And repeat. Eventually I find
the entire string decoded just before a function that reads it and performs the
base64 decode, and call the decoded data. At this point I used edb-debugger and
dumped the memory contents to a file (either the string, or the decoded data). I
opted for the string so I know where's the start/end. Then use Python to decode
the string and write to a bin file, the same way I did to solve Challenge 4 (see
challenge6.py)

But, the shellcode2exe tool didn't work in this case, because the tool don't
support 64-bit. So I found an alternate tool that does the same job but with x64
support at https://github.com/accidentalrebel/shcode2exe (unfortunately IDA Free
do not support binary files, so converting this to Linux ELF format is the route
I decided to go with).

After getting the ELF output, IDA Free is used again to disassemble this. Here
I see the code taking some string byte by byte, perform some operations, and
compare to a value. In a debugger this is found to be the 2nd argument of the
binary's input. At this point it's clear that we have to reverse the algorithm
to get back the correct string. After fumbling around with different methods,
I finally decided to write the reverse in assembly (c6reverse.asm), and
eventually get the string 'l1nhax.hurt.u5.a1l@flare-on.com'.

## Challenge 7
This challenge is very interesting, and brought me back to the time I was
actively reversing (ahem ahem...) sharewares around 1998-2002. Some tricks are
new to me as well so I learnt a great deal from this challenge. This challenge
is generally to bypass the various anti-debugging, anti-VMs and some other
trivial checks. Depending on whether the check passes or fails, the code will
perform xors with different keys to a byte string. Then writes the byte string
to an EXE file and try to execute it. If the checks are bypassed correctly, we
get a working EXE file. Otherwise, the EXE is plain gibberish. Finally, figure
out the email address from the EXE.

After studying the disassembly and running it a few times with a debugger, we
can easily find the start of the anti-debug/anti-VM checks. To overcome these, I
patched the conditional jumps to force the flow that I want and allow the
challenge to write the EXE to disk. The checks are in this specific order:
1. Call to IsDebuggerPresent. This is from kernel32.dll, which checks the PEB
structure.
2. Checks the PEB structure for IsDebug to detect debugger. Basically emulating
IsDebuggerPresent.
3. VM check using Interrupt Descriptor Table. To be honest I got really confused
with this one and patched this wrongly. I had to the solutions to see if I'm
understanding this correctly.
4. VM check using the 'in' operand.
5. SetLastError->OutputDebugString->GetLastError debugger check. This is also
another confusing one. I wasn't sure if the behavior is as intended.
6. Count 0xCCs as debugger check. CC is the operand for Int 3, which is a very
common way for debuggers to trigger breakpoints.
7. Check the PEB structure for NtGlobalStatus to detect debugger.
8. Check if the day is Friday.
9. Check if the Exe name is 'backdoge.exe'. This is also a confusing one,
because it checks 'backdoge.exe' against the command line that I observed
always include the full path. So technically I don't see how this check will
ever pass without patching the EXE.
10. Check if www.dogecoin.com can be resolved, effectively checking if the VM or
machine is connected to the Internet.
11. Check if the hour is 5pm.
12. Not really a check, but simply Xor-ing the byte string with the command line
string. This should be the string 'backdoge.exe' instead of the command line,
taking the cue from check #9. I modified the offsets during debugging to pass
this check.
13. Resolve the IP address of e.root-servers.net and xor-ing the data with it.
Also effectively checking if the VM/machine have Internet access.
14. Connect to Fireeye's tweet, downloads the page, and search for 'Secluded
Hi', which is part of the string 'Secluded HijackRAT'. Then uses 'jackRAT' to 
Xor against the byte string. In my debugging sessions this always fail because 
the page detects that Javascript is not enabled, hence getting a error page. But
opening the page in a proper browser reveals the string. So I patched in memory 
with the string to force a passed check here.
15. Gets 2nd and 3rd command line argument and patch into the byte string. Based
on the position of where the patching is done, we know that the arguments should
be MZ and PE, i.e. the typical PE header.
Some solutions involved writing Python or Powershell scripts to brute force the
correct flow. I did write a Python script to test the different combinations
of the flow (challenge7a.py). The solutions were a brute forcer but I didn't go
that far.

After we get the EXE file, it shows a picture but no email address. We can
quickly see that this is a .NET assembly so load up the file in dnSpy. The form
displaying this can be found rather quickly. I realize that the labels on the
form don't add up. So I guess this must be the missing email address. The string
is encoded and the decoding algorithm can be found in the lulz class (also xors
exactly the same way the EXE was encoded in the challenge exe, but with
different xor strings). I wrote the decoder in Python (challenge7b.py) to get
the email address from the encoded string 'da7.f1are.finish.lin3@flare-on.com'
from the main form. In the lulz class there were other strings that were decoded
but it didn't mean anything. There was another email address but from reading 
the solutions, that email address is a bogus one.
