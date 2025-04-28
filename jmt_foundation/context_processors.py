def theme(request):
    """
    Add theme context to templates.
    """
    theme_setting = request.COOKIES.get('jmt_theme', 'light')
    return {'current_theme': theme_setting}