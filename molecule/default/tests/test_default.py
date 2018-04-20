"""
Runs Default tests
Available Modules: http://testinfra.readthedocs.io/en/latest/modules.html

"""
import os
import testinfra.utils.ansible_runner

TESTINFRA_HOSTS = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_docker_is_installed(host):
    """
    Tests that docker is installed
    """
    docker = host.package("docker-ce")
    assert docker.is_installed


def test_docker_running_and_enabled(host):
    """
    Tests that docker is running and enabled
    """
    docker = host.service("docker")
    assert docker.is_running
    assert docker.is_enabled


def test_docker_user(host):
    """
    Tests that docker set user groups correctly
    """
    user = host.user("testuser")
    assert user.groups == ['testuser', 'docker']
