/*create table hello_happy.subscription
(
    subscriptionId   int            not null
        primary key,
    subscriptionType varchar(50)    not null,
    price            decimal(10, 2) not null,
    startDate        date           not null,
    userId           int            null,
    constraint fk9
        foreign key (userId) references hello_happy.user (userId)
);

