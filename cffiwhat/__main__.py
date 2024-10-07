
def cffi():
    from cffi import FFI

    ffi = FFI()
    ffi.set_source("_test", """
    #include <stdio.h>
    
    void cffihello(void) {
        printf("hello from cffi\\n");
    }
    
    """)
    ffi.cdef("""
    void cffihello(void);
    """)
    ffi.compile(verbose=99)
    from _test import lib  # import the compiled library

    lib.cffihello()


def main():
    print("hello")
    #cffi()


if __name__ == '__main__':
    main()

