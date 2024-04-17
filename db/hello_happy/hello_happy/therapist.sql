create table hello_happy.therapist
(
    therapistId int         not null
        primary key,
    firstName   varchar(25) null,
    lastName    varchar(25) null,
    email       varchar(50) not null,
    phone       varchar(50) not null,
    constraint email
        unique (email),
    constraint phone
        unique (phone)
);

