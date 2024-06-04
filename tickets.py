import os

f = open(
    os.path.join(
        os.path.dirname(__file__),
        "tickets.txt"
    ), "r"
)

tickets = f.readlines()

for ticket in tickets:
    t = ticket.split("\n")[0]
    with open(
        os.path.join(
            os.path.dirname(__file__),
            "tickets",
            t
        ), "w"
    ) as tf:
        tf.write("31")



