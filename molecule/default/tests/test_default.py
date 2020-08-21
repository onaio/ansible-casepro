import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_casepro_services(host):
    casepro = host.service("casepro")
    assert casepro.is_running
    assert casepro.is_enabled

    celeryd = host.service("celeryd-casepro")
    assert celeryd.is_running
    assert celeryd.is_enabled

    celery_beat = host.service("celerybeat-casepro")
    assert celery_beat.is_running
    assert celery_beat.is_enabled

def test_casepro_app_files(host):
    app_dir = host.file("/home/casepro/app")
    assert app_dir.exists
    assert app_dir.user == "casepro"
    assert app_dir.group == "www-data"
    assert app_dir.is_symlink
    assert app_dir.linked_to == "/home/casepro/app-versioned/v1.3.8"

    app_versioned_dir = host.file("/home/casepro/app-versioned/v1.3.8")
    assert app_versioned_dir.exists
    assert app_versioned_dir.user == "casepro"
    assert app_versioned_dir.group == "www-data"
    assert app_versioned_dir.is_directory
    assert oct(app_versioned_dir.mode) == "0o755"

    virtualenv = host.file("/home/casepro/.virtualenvs/casepro")
    assert virtualenv.exists
    assert virtualenv.user == "casepro"
    assert virtualenv.group == "www-data"
    assert virtualenv.is_directory
    assert oct(virtualenv.mode) == "0o755"
