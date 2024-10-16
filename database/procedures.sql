USE security_app;

-- Adds a device.
DROP PROCEDURE IF EXISTS add_device;
DELIMITER ;;
CREATE PROCEDURE add_device(
    i_device_id varchar(64),
    i_os_name varchar(64),
    i_os_version varchar(64),
    i_location varchar(32),
    i_ip_address varchar(32),
    i_last_active varchar(120),
    i_device_status varchar(32)
)
BEGIN
    START TRANSACTION;

    INSERT INTO device
        (device_id, os_name, os_version, location, ip_address, last_active, device_status)
    VALUES
        (i_device_id, i_os_name, i_os_version, i_location, i_ip_address, i_last_active, i_device_status)
    ;

    COMMIT; 
END
;;
DELIMITER ;

-- Adds an app.
DROP PROCEDURE IF EXISTS add_app;
DELIMITER ;;
CREATE PROCEDURE add_app(
    i_device_id varchar(64),
    i_app_name varchar(255),
    i_app_version varchar(255)
)
BEGIN

    START TRANSACTION;

    INSERT INTO app_list
        (device_id, app_name, app_version)
    VALUES
        (i_device_id, i_app_name, i_app_version)
    ;

    COMMIT;

END
;;
DELIMITER ;

-- Getter for specific device.
DROP PROCEDURE IF EXISTS get_device;
DELIMITER ;;
CREATE PROCEDURE get_device(
    i_device_id varchar(64)
)
BEGIN

    START TRANSACTION;
        SELECT * FROM device WHERE device_id = i_device_id;
    COMMIT;

END
;;
DELIMITER ;

-- Getter for all devices.
DROP PROCEDURE IF EXISTS get_all_devices;
DELIMITER ;;
CREATE PROCEDURE get_all_devices(
)
BEGIN

    START TRANSACTION;
        SELECT * FROM device;
    COMMIT;

END
;;
DELIMITER ;


-- Delete a device from app_list and device.
DROP PROCEDURE IF EXISTS remove_device;
DELIMITER ;;
CREATE PROCEDURE remove_device(
    i_device_id varchar(64)
)
BEGIN
    START TRANSACTION;
        DELETE FROM
            app_list 
        WHERE
            device_id = i_device_id
        ;
        DELETE FROM
            device
        WHERE
            device_id = i_device_id
        ;
    COMMIT;
END
;;
DELIMITER ;


-- Get all aps that got the same device_id.
DROP PROCEDURE IF EXISTS get_apps;
DELIMITER ;;
CREATE PROCEDURE get_apps(
    i_device_id varchar(64)
)
BEGIN
    START TRANSACTION;
        SELECT
            *
        FROM app_list
        WHERE
            device_id = i_device_id
        ;
    COMMIT;
END
;;
DELIMITER ;

-- Lets server know that user is online
DROP PROCEDURE IF EXISTS update_status;
DELIMITER ;;
CREATE PROCEDURE update_status(
    i_device_id varchar(64),
    i_device_status varchar(32)
)
BEGIN
    START TRANSACTION;
        UPDATE
            device
        SET
            last_active = NOW(),
            device_status = i_device_status
        WHERE
            device_id = i_device_id
        ;
    COMMIT;
END
;;
DELIMITER ;