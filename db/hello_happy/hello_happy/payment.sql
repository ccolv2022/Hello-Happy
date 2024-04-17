create table hello_happy.payment
(
    paymentId   int            not null
        primary key,
    amount      decimal(10, 2) not null,
    paymentDate date           not null,
    dueDate     date           not null,
    userId      int            null,
    constraint fk10
        foreign key (userId) references hello_happy.user (userId)
);

