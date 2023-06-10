# KCalc-project
Kcalc is an open source(GPL v3.0) calculator for desktop, it features basic arithmatical operations, such as addition, subtraction, multiplication, division, exponantion, and square root.

# CHANGE LOG
V1.0: Fixed "int literal" error, status: done

V2.0: Background optimization, bug fix, GUI medernization, added support for decimal numbers [example: 5.12], status: done

V3.0: Add new operation "^" a.k.a "x to the power of y", returns the old GUI, status: done

V4.0: Add new operation "√" a.k.a "square root of x", stratus: done

V5.0: Support for commas as seperator when inputting the numbers, example (one thousand = 1,000) but (one point zero = 1.0) and this, (one thousand point zero = 1,000.0), status: done

Modern GUI Update: GUI modernization using CTk(customtkinter) and a new naming system, status: done

New Life Update: Brought a new UI for the legacy and modern version to make it look like actual calculator. This update is a full rework for the code so be patient, status: on work...

# Known Errors
V3.0+: "int literal" error has comeback, its a non-fatal console error(this means that the app will work as intended even when the error is triggered), it won't be fixed

V5.0+ : you can separate by hundreds, tens, tens of thousands or even more! This is non-fatal GUI bug

V7.0+: you can code in a calculator, this is real bad, it's a top priority ****SECURITY VUNERABILITY****

# How to commit
1. First, you must know that the owner of this repository is a human and not active at all times to check your code.
2. Second, please make sure that the desciption and the tilte are clear, matching the whole body(description and title) and code.
3. Make sure that every feature developed for main_modern is compatible with main_legacy and *vice versa*
4. Name a source file(main.py) this way:
  1. GUI type, seperated using an underscore `_` with `main`. There's only **modern or legacy** GUI types. The result of this step is `main_modern.py` or `main_legacy.py`
  2. Version number, we will use the new version numbering scheme (see below for version numbering scheme explanation). A version number is inside square brackets `[]`. Inside the square bracket there's a capital V as an abreviation for version. After that there's the version number using a float, usually called decimal. Examples: `5.0`, `5.1`.
  3. Version number allowed to have only ***ONE*** number after the floating point
  4. ***DO NOT USE VERSION NUMBER THAT HAS BEEN USED***
  5. example of a final filename complying with all guidelines: main_modern[V5.0].py, main_legacy[V6.0].py, main_modern[V7.1].py

# Version Numbering Scheme Explanation
1. V1.0 to V4.0 is united, means there's only 1 file
2. V5.0 onwards will be separated, based on UI, between legacy and modern
3. Although the update that brings modern GUI is V6.0, it's name now is Modern GUI Update
4. main_modern.py and main_legacy.py will have the version number V5.0







