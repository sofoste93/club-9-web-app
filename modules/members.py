from flask import request, render_template


def get_members():
    # Ici, vous devez récupérer la liste des membres à partir de votre base de données.
    members = []
    return render_template('members.html', members=members)


def add_member():
    # Ici, vous devez ajouter un nouveau membre à votre base de données.
    pass
