Description
------------

A simple yet usefull debugging tool for applications
that run in loops (especially games and custom UI apps).

Example.
---------

Code:


    from vdebugger import *


    def test_console():
        vd("a", "B")
        vd("a", "B")
        vd("foo", 123)
        vd("blu", {"nope": "nonono"})
        vd("blu", {"nope": "nonono"})

Output:

    | -------------------- || -------------------- || -------------------- |
    | a                    || foo                  || blu                  |
    | -------------------- || -------------------- || -------------------- |
    | >>>2>>>              || >>>1>>>              || >>>2>>>              |
    | 'B'                  || 123                  || {'nope': 'nonono'}   |
    | -------------------- || -------------------- || -------------------- |
    `
