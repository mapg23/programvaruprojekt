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