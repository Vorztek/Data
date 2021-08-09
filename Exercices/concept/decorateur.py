user = "olividddder"

def mon_decorateur(fonction):

    def accept():
        print("Action acceptée")

    def no_accept():
        print("C'est mort")

    if user == "olivier":
        return accept

    if user != "oliver":
        return no_accept


    return fonction 


@mon_decorateur
def do_that():
    print("Execution des instructions")


print(do_that())