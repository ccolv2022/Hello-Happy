/*create table hello_happy.entry
(
    entryId           int                                  not null
        primary key,
    timestamp         datetime   default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP,
    dayRating         int                                  not null,
    goodDay           tinyint(1) default 1                 not null,
    moodRating        int                                  not null,
    peopleSeen        int                                  not null,
    meals             text                                 null,
    ozWater           int                                  null,
    hoursExercise     int                                  null,
    exerciseIntensity int                                  null,
    hoursSleep        int                                  null,
    people            text                                 null,
    wakeUpTime        datetime                             null,
    sleepTime         datetime                             null,
    weather           int                                  null,
    primaryLocation   varchar(30)                          null,
    visibility        tinyint(1) default 1                 null,
    userId            int                                  null,
    constraint entryweatherfk
        foreign key (weather) references hello_happy.weatherLookup (weatherId)
            on update cascade on delete cascade,
    constraint fk8
        foreign key (userId) references hello_happy.user (userId)
            on update cascade on delete cascade
);

