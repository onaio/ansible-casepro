onaio - CasePro [![Build Status](https://github.com/onaio/ansible-casepro/workflows/CI/badge.svg)](https://github.com/onaio/ansible-casepro/actions?query=workflow%3ACI)
=========

Installs and configures [CasePro](https://rapidpro.github.io/casepro).

Requirements
------------

CasePro has the following requirements:

- PostgreSQL
- Redis

Role Variables
--------------

Check the [defaults/main.yml](./defaults/main.yml) file for the full list of default variables.

```yml
# git tag/branch to install
casepro_git_branch: "v1.3.8"

# domain for CasePro
casepro_domain: casepro.example.com

# secret key
casepro_secret_key: "very-secret-key"
```

Dependencies
------------

Here's the list of role dependencies:

- [onaio.django](https://galaxy.ansible.com/onaio/django)

Example Playbook
----------------

The following example playbook sets up CasePro, PostgreSQL and Redis:

```yml
- hosts: all
  roles:
    - role: onaio.postgresql
      vars:
        postgresql_version: 10
        postgresql_users:
          - name: casepro
            pass: casepro
            encrypted: true
        postgresql_databases:
          - name: casepro
            owner: casepro
            encoding: UTF-8
            hstore: true
        postgresql_database_extensions:
          - db: casepro
            extensions:
              - hstore
        postgresql_backup_enabled: false

    - role: DavidWittman.redis
      vars:
        redis_version: "2.8.24"

    - role: ansible-casepro
      vars:
        casepro_postgresql_password: casepro
```

License
-------

Apache 2
