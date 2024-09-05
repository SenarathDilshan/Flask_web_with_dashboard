# from functools import wraps
# from flask import redirect, url_for, flash
# from flask_login import current_user



# def admin_required(f):
#     @wraps(f)
#     def decorated_function(*args, **kwargs):
#         if not current_user.is_admin:
#             flash('You do not have permission to access this page.', category='error')
#             return redirect(url_for('auth.adminsignup'))
#         return f(*args, **kwargs)
#     return decorated_function

    
# # from functools import wraps
# # from flask import redirect, url_for, flash
# # from flask_login import current_user

# # def admin_required(f):
# #     """
# #     Decorator to require admin privileges for a route.
# #     Redirects to the login page or a signup page with an error message if the user is not an admin.
# #     """
# #     @wraps(f)
# #     def decorated_function(*args, **kwargs):
# #         if not current_user.is_authenticated or not current_user.is_admin:
# #             flash('You do not have permission to access this page.', category='error')
# #             return redirect(url_for('auth.adminsignup'))  # Redirect to the admin signup page or login page
# #         return f(*args, **kwargs)  # Allow access to the route if the user is an admin
# #     return decorated_function
