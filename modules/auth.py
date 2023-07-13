from flask import request, render_template


def login():
    if request.method == 'POST':
        # Ici, vous devez vérifier les informations de l'utilisateur et le connecter s'ils sont correctes.
        pass
    return render_template('login.html')


def register():
    if request.method == 'POST':
        # Ici, vous devez vérifier les informations de l'utilisateur et le créer un nouveau compte s'ils sont correctes.
        pass
    return render_template('register.html')
