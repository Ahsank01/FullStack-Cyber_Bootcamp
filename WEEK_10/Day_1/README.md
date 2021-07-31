# Red Team 11: Buffer Overflows

## OUTLINE
1. Memory
2. The Stack
3. The Key Players
4. DEP and ASLR
5. OSCP Buffer Overflows
6. Steps of performing a Buffer Overflow

<br>

## MEMORY
- Everything must be 1s and 0s
- Often shown in hexadecimal. 
- x86/x64 refers to the amount of data that can be processes in each register.  
1. Memory is requested by the application but distrubuted by the OS.
2. If the application doesn't properly ask for the right amount of memory, it is possible that the application might overflow outside of the designated area.

<br>

## THE STACK
The `stack` as a temporary storage area in RAM that allows the processor to quickly store and retrieve data in memory

<br>

## THE PLAYER
- x86 processors have eight 32-bit general purpose registers.
- The registers are used to store information (either values or references [pointers] to other locations in memory)
- Naming is historical - all essentially general purpose exceprt ESP/EBP (and EIP not listed)
1. A atack needs to pointer to indicate where in memory is the `Top` of the stack.
    - ESP Register
2. Since it is the job of ESP to maintain the top of the stack, another registers responsibility is to maintain the `Current Reading Frame`
    - That is the EIP Register

<br>

## DEP AND ASLR
1. Data Execution Prevention (DEP)
    - Memory can be declared as executale or `data for storage`
2. Address Space Layout Randomization (ASLR)
    - Memory is handled entirely by the OS and assigned upon request and is randomized in placement each time it is requested.

<br>

## OSCP BUFFER OVERFLOWS
1. You will only br responsible for BO againts a vulnerable windows machine
2. You will have a scaffold of non-exploitable code against that service.
3. You will not be responsible for bypassing ASLR or DEP


<br>

## STEPS OF PERFORMING BO - VERIFY
1. Run vulnerable application and attach it to Immunity Debugger.
2. Ensure you have a script that can normally communicate target protocol.
3. Perform Fuzzing on that script with a single character until application crashes.
    1. Figure out which registers contain memory addresses that are overridden.
    2. Figure out which registers are overridden themselves(this is only good if it is EIP)
4. Locate the bytes at which EIP was overridden.

<br>

## STEPS OF PERFORMING BO - EXECUTE
1. Ensure you have enough room to hide a payload that is your reverse shell but do not make it yet. > 350 bytes would be perfect!
2. Determine bad characters
3. Work on redirection, need to find DLL. Use mona!
    - Make sure you look for at lease 4 falses (first 4, hopefully 5).
4. Generate payload and update your exploit code
5. Exploit!
