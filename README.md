# structlog-round

A simple and light-weight [`structlog`](https://github.com/hynek/structlog) processor to round floats for prettier logging.

Are you using `structlog` for convenient, structured logging in your Python program?
Logging floats easily bloats your logs through many floating point digits?
`structlog-round` rounds your floats for prettier logging but lets you keep full float precision inside your program.

For example:

```python
import structlog 
log = structlog.get_logger()
log.msg("Important logging", a=1/3, b=2/3)
# prints long and ugly floats
# 2020-07-16 21:48.21 Important logging              a=0.3333333333333333 b=0.6666666666666666
```

Easier to read:



## Install

```
python setup.py install
```

## Usage





