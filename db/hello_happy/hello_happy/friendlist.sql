/*create table hello_happy.friendlist
(
    userId   int not null,
    friendId int not null,
    primary key (userId, friendId),
    constraint fk2
        foreign key (friendId) references hello_happy.user (userId),
    constraint fk3
        foreign key (userId) references hello_happy.user (userId)
);

