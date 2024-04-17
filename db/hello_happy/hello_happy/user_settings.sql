create table hello_happy.user_settings
(
    userId           int                  null,
    notifications_on tinyint(1) default 0 null,
    contacts_on      tinyint(1) default 0 null,
    constraint fk4
        foreign key (userId) references hello_happy.user (userId)
);

