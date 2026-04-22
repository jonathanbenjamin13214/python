def shutdown(a):
    if a == "yes":
        return "Shutting down"
    else:
        return "error"
print(shutdown("yes"))