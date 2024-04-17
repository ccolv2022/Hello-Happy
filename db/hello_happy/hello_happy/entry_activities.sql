create table hello_happy.entry_activities
(
    entryId    int not null,
    activityId int not null,
    primary key (entryId, activityId),
    constraint activityfk
        foreign key (activityId) references hello_happy.activities (activityId)
            on update cascade on delete cascade,
    constraint entryfk
        foreign key (entryId) references hello_happy.entry (entryId)
            on update cascade on delete cascade
);

