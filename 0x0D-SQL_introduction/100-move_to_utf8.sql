-- converts hbtn_0c_0 database to UTF8
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE hbtn_0c_0.first_table CHARACTER SET utf8 COLLATE utf8_general_ci;
ALTER TABLE hbtn_0c_0.first_table MODIFY `name` VARCHAR(256) CHARACTER SET utf8 COLLATE utf8_general_ci;
