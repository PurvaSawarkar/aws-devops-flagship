import json
import logging
import sys

EXTRA_FIELDS = ('method', 'path', 'status', 'duration_ms')


class JsonFormatter(logging.Formatter):
    def format(self, record):
        payload = {
            'ts': self.formatTime(record, datefmt='%Y-%m-%dT%H:%M:%S'),
            'level': record.levelname,
            'logger': record.name,
            'message': record.getMessage(),
        }

        for field in EXTRA_FIELDS:
            if hasattr(record, field):
                payload[field] = getattr(record, field)

        if record.exc_info:
            payload['exception'] = self.formatException(record.exc_info)

        return json.dumps(payload)


def setup_logging(level='INFO'):
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(JsonFormatter())

    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level.upper())
