from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .models import User

views = Blueprint("views", __name__)

@views.route("/home")
@login_required
def home():
    print(f"Current user: {current_user}")
    return render_template("home.html", name=current_user.username)

@views.route("/dashboard", endpoint="dashboard")
@login_required
def dashboard():
    if not current_user.is_admin:
        flash('You do not have permission to access the dashboard.', category='error')
        return redirect(url_for('views.home'))
    print(f"Current user: {current_user}")
    return render_template("dashboard.html")


# @views.route("/dashboard")
# @login_required
# #@admin_required
# def dashboard():
#     print(f"Current user: {current_user}, Is Admin: {current_user.is_admin}")
#     return render_template("dashboard.html", name=current_user.username)

# @views.route("/dashboard", methods=['GET', 'POST'])
# #@admin_required
# def admin_dashboard():
#     if request.method == 'POST':
#         is_admin = request.form.get(is_admin)
#         is_admin = User.query.filter_by(is_admin=True).first()
        
#         flash("Logged in Admin!", category='success')
#         #return redirect(url_for('views.admin_dashboard'))
#         return render_template("dashboard.html", name=current_user.username)
#     else:
#         flash("please signup as in Admin from views dashboard!", category='error')
#     #return render_template("adminlogin.html")
#     return redirect("/admin")
    


#views = Blueprint("views", __name__)

# @views.route("/dashboard", methods=['GET', 'POST'])
# @login_required
# @admin_required
# def dashboard():
#     if current_user:
#         if request.method == 'POST':
#             is_admin = request.form.get(is_admin)
#             is_admin = User.query.filter_by(is_admin=True).first()
#             current_user(User, remember=True, is_admin=True)

#             #new_user = User(email=email, username=username, is_admin=True)
            
#             # Handle POST request logic for admins
#             flash("Admin action performed successfully!", category='success')
#         return render_template("dashboard.html", name=current_user.username)
#         print(current_user.username)
#         # Handle GET request or non-POST situations
#         #return render_template("dashboard.html", name=current_user.username)
#     else:
#         flash("You must be an admin to access this page.", category='error')
#         return redirect(url_for('auth.admin'))  # Redirect to the admin login page

# @views.route("/dashboard", endpoint="dashboard")
# @login_required
#@admin_required  # Apply the custom decorator
# def dashboard():
#     print(f"Current user: {current_user}")
#     return render_template("dashboard.html", name=current_user.username)
        
# def dashboard():
#     if not current_user.is_admin:
#         flash('You do not have permission to access the dashboard.', category='error')
#         return redirect(url_for('auth.adminsignup'))
#     print(f"Current user: {current_user}")
#     return render_template("dashboard.html")

        
        
    # Admin dashboard logic
    #return render_template("dashboard.html")



#  @views.route("/dashboard", methods=['GET', 'POST'])
#  def dashboard():
#      if request.method == 'POST':
# #         email = request.form.get("email")
# #         password = request.form.get("password")
#          is_admin = request.form.get(is_admin)

# #         user = User.query.filter_by(email=email).first()
#          is_admin = User.query.filter_by(is_admin=True).first()
#          if user:
#     #         if check_password_hash(user.password, password):
#     #             flash("Logged in Admin!", category='success')
#     #             login_user(user, remember=True)
#     #             return redirect(url_for('views.dashboard')) # change to the dash board
#     #         else:
#     #             flash('Password is incorrect.', category='error')
#     #     else:
#     #         flash('Email does not exist.', category='error')

#     # return render_template("adminlogin.html")