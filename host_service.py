import psutil

def host_info():
    telemetry = {}
    telemetry['memory'] = psutil.virtual_memory().percent
    telemetry['cpu'] = psutil.cpu_percent(1)
    return telemetry

