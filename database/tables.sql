USE security_app;

DROP TABLE IF EXISTS device;
CREATE TABLE device
(
    id INT AUTO_INCREMENT NOT NULL,
    device_id varchar(64) NOT NULL UNIQUE,
    os_name varchar(64),
    os_version varchar(64),
    location varchar(32),
    ip_address varchar(32),
    last_active varchar(120),
    device_status varchar(32),   

    PRIMARY KEY (id)
);

DROP TABLE IF EXISTS app_list;
CREATE TABLE app_list
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    device_id varchar(64) NOT NULL,
    app_name varchar(255) NOT NULL,
    app_version varchar(255),

    FOREIGN KEY (device_id) REFERENCES device(device_id)
);