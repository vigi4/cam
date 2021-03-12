
rtsp = {
    'rtsp1': 'rtsp://user:user@{}:{}',
    'rtsp2': 'rtsp://{}:{}/1/h264major',
    'rtsp3': '"rtsp://{}:{}/user=user&password=pass&channel=1&stream=0?.sdp"',
    'rtsp4': 'rtsp://admin:admin@{}:{}',
    'rtsp5': 'rtsp://user:user@{}:{}',
}

objects = {
    'xxxx': {
        'name': 'xxxxx',
        'ip': 'xxxxx',
        'ports': ['xxxx', 'xxxx'],
        'rtsp': rtsp['rtsp2']
    },

    'xxx': {
        'name': 'xxxxx',
        'ip': 'xxxxxx',
        'ports': ['xxxxxx', 'xxxxx'],
        'port2': ['xxxx'],  # Порты для rtsp2
        'rtsp': rtsp['rtsp3'],
        'rtsp2': rtsp['rtsp1']
    },
}
