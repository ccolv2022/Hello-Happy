/*create table hello_happy.meeting
(
    meetingId   int                                  not null
        primary key,
    timestamp   datetime   default CURRENT_TIMESTAMP null,
    topic       varchar(30)                          null,
    isVirtual   tinyint(1) default 0                 null,
    therapistId int                                  null,
    userId      int                                  null,
    constraint fk6
        foreign key (userId) references hello_happy.user (userId)
            on update cascade on delete cascade,
    constraint meetingfk
        foreign key (therapistId) references hello_happy.therapist (therapistId)
            on update cascade on delete cascade
);

