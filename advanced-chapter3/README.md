Chạy trên ubuntu 22 sẽ bị lỗi sau
```fatal: [poc-m2]: FAILED! => {"changed": false, "msg": "unable to find /root/.my.cnf. Exception message: (1698, \"Access denied for user 'root'@'localhost'\")"}```

Tham khảo cách fix sau đây:
    # - name: Change the authentication plugin of MySQL root user to mysql_native_password
    #   shell: mysql -u root -e 'UPDATE mysql.user SET plugin="mysql_native_password" WHERE user="root" AND host="localhost"'

    # - name: Flush Privileges
    #   shell: mysql -u root -e 'FLUSH PRIVILEGES'

    # - name: Set MySQL root password
    #   mysql_user:
    #     login_host: 'localhost'
    #     login_user: 'root'
    #     login_password: ''
    #     name: 'root'
    #     password: '{{ mysql_pass }}'
    #     state: present