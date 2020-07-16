import structlog
import structlog_round

structlog.configure(
    processors=[
        structlog_round.FloatRounder(digits=3),
        structlog.dev.ConsoleRenderer()
    ]
)
log = structlog.get_logger()

a = 1/3
b = 2/3
log.msg("Hello world", a=a, b=b)
print(a, b)
