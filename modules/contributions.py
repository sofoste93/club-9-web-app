from flask import request, render_template


def get_contributions():
    # Ici, vous devez récupérer la liste des cotisations à partir de votre base de données.
    contributions = []
    return render_template('contributions.html', contributions=contributions)


def add_contribution():
    # Ici, vous devez ajouter une nouvelle cotisation à votre base de données.
    pass
