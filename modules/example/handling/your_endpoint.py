from flask import flash, redirect, request, url_for, render_template

from .. import NAME
from ..forms import ContactForm
from app.utils.translating import t


def handle_request():
    form = ContactForm()

    if form.validate_on_submit():
        #------------------------
        # TODO: Handle form data.
        #------------------------
        flash(t("Thanks! Your message has been received."), "success")
        return redirect(url_for(f"{NAME}.endpoint"))

    if request.method == "POST" and not form.validate():
        flash(t("Please check your inputs."), "error")

    return render_template("your_form.html", form=form)
