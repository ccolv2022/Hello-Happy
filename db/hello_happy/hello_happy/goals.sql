create table hello_happy.goals
(
    goalId           int                  not null
        primary key,
    completionStatus tinyint(1) default 0 null,
    description      varchar(100)         null,
    userId           int                  null,
    constraint fk5
        foreign key (userId) references hello_happy.user (userId)
);

