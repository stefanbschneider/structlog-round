import structlog
import structlog_round

structlog.configure(
    processors=[
        structlog_round.FloatRounder(digits=3, only_fields=['a']),
        structlog.dev.ConsoleRenderer()
    ]
)
log = structlog.get_logger()

a = 1/3
b = 2/3
log.msg("Hello world", a=a, b=b)
print(a, b)

rounder = structlog_round.FloatRounder(only_fields=['p1'])
event_dict = rounder(None, None, {'p1': 1/3, 'p2': 2/3})
print(event_dict)
