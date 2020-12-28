# Xenon
    Lightweight, amateur web(currently) fuzzer written in Python.
# Uses
    python3 xenon.py <path to settings file>
# Settings file format
    vulnerability::<xss>
    url::<url>
    security::<low|medium|high>
    banner::<on|off>
    
    ! - If vulnerability or url are not present or empty, Xenon returns a error.
    ! - All keys are case insensitive
    ! - security defaults to low and banner defaults to on
