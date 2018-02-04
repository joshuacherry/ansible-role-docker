# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

| Change Type   | Description                            |
| :------------ | :------------------------------------- |
| Added         | for new features.                      |
| Changed       | for changes in existing functionality. |
| Deprecated    | for soon-to-be removed features.       |
| Removed       | for now removed features.              |
| Fixed         | for any bug fixes.                     |
| Security      | in case of vulnerabilities.            |

## [Unreleased]

## [0.2.1] - 2018-02-03

### Changed

- Ansible version in dockerfiles set to latest for Xenial and Jessie

### Fixed

- Fixed Apt not updating cache before running in new systems
- Fixed Yum not having EPEL enabled for python-pip install

## [0.2.0] - 2017-12-01

### Changed

- Using pip for docker-compose instead of github repo

[Unreleased]: https://github.com/joshuacherry/ansible-role-grafana/compare/0.2.1...HEAD
[0.2.1]: https://github.com/joshuacherry/ansible-role-grafana/compare/0.2.0...0.2.1
[0.2.0]: https://github.com/joshuacherry/ansible-role-grafana/compare/0.1.0...0.2.0