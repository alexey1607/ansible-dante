# ansible-dante

Ansible‑роль для установки и базовой настройки Dante socks proxy server на Debian‑подобных системах.

Документация Dante socks proxy server https://www.inet.no/dante/

## Назначение

Эта роль позволяет:
- ходить в телегу через проксю

## Поддерживаемые ОС

- Debian 12

## Переменные роли

./defaults/main.yml

| Переменная            | Значение по‑умолчанию               | Описание                           |
|-----------------------|-------------------------------------|------------------------------------|
| `dante_config`        | `/etc/danted.conf`                  | путь к конфигу                     |
| `dante_logs`          | `/var/log/danted`                   | путь к директории с логами         |
| `dante_systemd_unit`  | `/lib/systemd/system/danted.service`| путь к systemd юниту               |
| `dante_interface`     | `0.0.0.0`                           | интерфейс на котором раотает dante |
| `dante_port`          | `1080`                              | порт, на котором слушает Dante     |
| `dante_users`         | `[]`                                | списко пользователей для прокси.   |


## Пример использования

Пример запуска плэйбука

```yaml
---
- name: Converge
  hosts: dante-server
  roles:
    - role: ansible-dante
      vars:
        dante_config: "/etc/danted.conf"
        dante_logs: "/var/log/danted"
        dante_systemd_unit: "/lib/systemd/system/danted.service"
        dante_interface: "0.0.0.0"
        dante_port: "1080"
        dante_users:
          - dante
          - dante-user1
          - dante-user2
