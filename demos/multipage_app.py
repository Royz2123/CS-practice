from st_pages import Page, Section, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what test should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("webpages/home_page.py", "דף הבית", "🏠"),
        Page("webpages/about_page.py", "איך מתחילים?", "❓"),
        # Page("webpages/about_page.py", "Page 2", ":books:"),
        Section("My section", icon="🎈️"),
        Page("webpages/exercise_page.py", "Page 3", ":books:"),
        Section("My section 2", icon="🎈️"),
    ]
)