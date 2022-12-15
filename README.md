# Logging

This sample code shows some information available in log records.

## To Run

```bash
python3 main.py
```

Will print out:

```
2022-12-15 10:05:26,646 level---INFO module---my_class filename---my_class.py lineno---6 funcName---foo In MyClass.foo()
Stack (most recent call last):
  File "/Users/jeantessier/language/Python/testing/python-logging-test/main.py", line 19, in <module>
    main()
  File "/Users/jeantessier/language/Python/testing/python-logging-test/main.py", line 12, in main
    my_class.foo()
  File "/Users/jeantessier/language/Python/testing/python-logging-test/my_class.py", line 6, in foo
    logging.info("In MyClass.foo()", stack_info=True)
2022-12-15 10:05:26,647 level---INFO module---other_class filename---other_class.py lineno---6 funcName---bar In OtherClass.bar()
Stack (most recent call last):
  File "/Users/jeantessier/language/Python/testing/python-logging-test/main.py", line 19, in <module>
    main()
  File "/Users/jeantessier/language/Python/testing/python-logging-test/main.py", line 15, in main
    other_class.bar()
  File "/Users/jeantessier/language/Python/testing/python-logging-test/other/other_class.py", line 6, in bar
    logging.info("In OtherClass.bar()", stack_info=True)
```
