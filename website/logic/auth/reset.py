from website.utils.rendering import render, render_404
from website.utils.cache import request_entry_data, pop_entry
from website.data import user as udb
from flask import Response, request, flash, redirect


def handle_request(code: str) -> Response | str:
    uid = request_entry_data(code)
    if not uid:
        return render_404()

    user = udb.User.query.get(uid)
    if request.method == 'GET':
        return render('auth/reset.html', email=user.email)

    password = request.form.get('password')
    user.set_password(password)
    pop_entry(code)

    flash("Dein Passwort wurde erfolgreich geändert!", 'success')
    return redirect('/login')
