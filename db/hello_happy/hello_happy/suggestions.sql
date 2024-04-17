create table hello_happy.suggestions
(
    sugId       int  not null
        primary key,
    description text null,
    therapistId int  null,
    userId      int  null,
    constraint fk7
        foreign key (userId) references hello_happy.user (userId),
    constraint suggestion_fk
        foreign key (therapistId) references hello_happy.therapist (therapistId)
);

