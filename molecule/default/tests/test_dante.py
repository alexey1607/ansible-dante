def test_dante_service_running(host):
    svc = host.service("danted")
    assert svc.is_running
    assert svc.is_enabled

def test_dante_listening(host):
    s = host.socket("tcp://0.0.0.0:1080")
    assert s.is_listening