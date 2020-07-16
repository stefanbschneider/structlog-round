# structlog-round

A simple and light-weight [`structlog`](https://github.com/hynek/structlog) processor to round floats for prettier logging.

Are you using `structlog` for convenient, structured logging in your Python program?
Logging floats easily bloats your logs through many floating point digits?
`structlog-round` rounds your floats for prettier logging but lets you keep full float precision inside your program.

For example:

```python
log.msg("Important logging", a=1/3, b=2/3)

# without structlog-round: prints long and ugly floats
# 2020-07-16 21:48.21 Important logging              a=0.3333333333333333 b=0.6666666666666666

# with structlog-round: floats are logged nicely rounded
# 2020-07-16 21:48.21 Important logging              a=0.333 b=0.667
```

Easier to read:



## Install

```
python setup.py install
```

## Usage

```python
import structlog
import structlog_round

structlog.configure(
    processors=[
        # importing and adding FloatRounder to your list of processors is all you have to do
        structlog_round.FloatRounder(digits=3),
        structlog.dev.ConsoleRenderer()
    ]
)
log = structlog.get_logger()

a = 1/3
b = 2/3
log.msg("Hello world", a=a, b=b)
# this log is easily readable with short, rounded floats
# Hello world                    a=0.333 b=0.667
print(a, b)
# the floats are still available in full precision and unrounded
# 0.3333333333333333 0.6666666666666666
```

`FloatRounder` has the following configuration options:

* `digits`: The number of digits to round to
* `only_fields`: A list of only fields that should be rounded
* `not_fields`: A list of fields that should not be rounded
* `np_array_to_list` (bool): Whether to cast `numpy` arrays to lists and round floats for prettier logging
