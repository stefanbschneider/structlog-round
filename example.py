import structlog
import structlog_round

structlog.configure(
    processors=[
        structlog_round.FloatRounder(digits=3),
        structlog.dev.ConsoleRenderer()
    ]
)
log = structlog.get_logger()


log.msg("Important logging", a=1/3, b=2/3)
