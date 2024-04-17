create table hello_happy.user
(
    userId      int         not null
        primary key,
    firstName   varchar(25) null,
    lastName    varchar(25) null,
    email       varchar(50) not null,
    therapistId int         null,
    constraint email
        unique (email),
    constraint userfk
        foreign key (therapistId) references hello_happy.therapist (therapistId)
            on update cascade
);

