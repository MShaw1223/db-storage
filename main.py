import sys

from db import DataBase


def main():
    d = DataBase()
    arg = sys.argv[1]
    match arg:
        case _ if arg == "insert":
            # d.insert_users("miller", "ms@foo.com", 18)
            # d.insert_users("test", "fooBar", 13)
            print("Insertion complete")
        case _ if arg == "select":
            # select method: .select(table, field, clause, var)
            # - the table param  must be specified.
            # - the field param defaults to a wildcard.
            #   - can be func ie avg(age) or a table col ie name
            # - the clause param defs to ID = ?
            #   - '-' means no clause; clauses can be: ID > 1, age >= 20, etc
            # - the var param defs to 1
            foo = d.select("Users", "Email", "-")
            print("Email only: ", foo)
            foo = d.select("Users")
            print("All results: ", d.select("Users"))
            print(
                f"Result names: 1. {d.select("Users")[0][1]} 2. {d.select("Users")[1][1]}"
            )
            print("Avg age: ", d.select("Users", "avg(Age)", "-")[0][0])

        case _ if arg == "update":
            # update method
            d.update("Users", "ID", 6)
            print()
            inp = input("Enter a new email to update: ")
            d.update("Users", "Email", inp, 2)
            print("Result: ", d.select("Users"))
        case _ if arg == "delete":
            # delete method
            d.delete("Users", "Email", "fooBar")
            print("Result of deletion: ", d.select("Users"))
        case _:
            print(f"Argument '{arg}' isn't recognised :/")


if __name__ == "__main__":
    main()
