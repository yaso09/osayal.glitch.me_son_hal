import os, shutil

def getTickets():
    return os.listdir(
        os.path.join(__file__),
        "tickets"
    )

def oyver(ticket: str, aday: str):
    shutil.move(
        os.path.join(
            os.path.dirname(__file__),
            "tickets", ticket
        ),
        os.path.join(
            os.path.dirname(__file__),
            "oylar", aday, ticket
        )
    )

def isTicketUsed(ticket: str):
    if os.path.exists(
        os.path.join(
            os.path.dirname(__file__), "tickets", ticket
        )
    ): return False
    else: return True