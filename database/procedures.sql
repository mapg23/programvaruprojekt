USE security_app;

DROP PROCEDURE IF EXISTS add_device;
DELIMITER ;;
CREATE PROCEDURE add_device(
    i_device_id varchar(64),
    i_os_name varchar(20),
    i_os_version varchar(20),
    i_location varchar(32),
    i_last_active varchar(120),
    i_device_status varchar(32)
)
BEGIN
    START TRANSACTION;

    INSERT INTO device
        (device_id, os_name, os_version, location, last_active, device_status)
    VALUES
        (i_device_id, i_os_name, i_os_version, i_location, i_last_active, i_device_status)
    ;

    COMMIT; 
END
;;
DELIMITER ;

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