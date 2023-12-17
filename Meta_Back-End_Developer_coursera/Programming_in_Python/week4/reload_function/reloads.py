# # import sample
# # import sample
# import sample


# import importlib
#
# importlib.reload(sample)
# importlib.reload(sample)
# importlib.reload(sample)


import importlib
import filechanges


def changes():
    try:
        importlib.reload(filechanges)
        filechanges.print_changes()
    except:
        pass


for i in range(5):
    changes()
    input(f"Hit enter to reload... times count({i + 1})")
